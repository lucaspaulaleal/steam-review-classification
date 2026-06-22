"use client";

import { useEffect, useRef, useState, useCallback, memo } from "react";
import * as d3 from "d3";

const RAW_NODES = [
  { id: "r1", type: "review", label: "R1", desc: "Ótimos gráficos, fps baixo" },
  { id: "r2", type: "review", label: "R2", desc: "Gameplay viciante, controles fluidos" },
  { id: "r3", type: "review", label: "R3", desc: "História incrível, enredo envolvente" },
  { id: "r4", type: "review", label: "R4", desc: "Crashes frequentes, lag constante" },
  { id: "fps",       type: "word", label: "fps" },
  { id: "lag",       type: "word", label: "lag" },
  { id: "crash",     type: "word", label: "crash" },
  { id: "textura",   type: "word", label: "textura" },
  { id: "resolucao", type: "word", label: "resolução" },
  { id: "controles", type: "word", label: "controles" },
  { id: "diversao",  type: "word", label: "diversão" },
  { id: "historia",  type: "word", label: "história" },
  { id: "enredo",    type: "word", label: "enredo" },
  { id: "cat_perf",  type: "category", label: "Performance" },
  { id: "cat_graf",  type: "category", label: "Gráficos" },
  { id: "cat_game",  type: "category", label: "Gameplay" },
  { id: "cat_narr",  type: "category", label: "Narrativa" },
];

const ALL_LINKS = [
  // TF-IDF: review → word
  { source: "r1", target: "fps",       type: "tfidf" },
  { source: "r1", target: "textura",   type: "tfidf" },
  { source: "r1", target: "resolucao", type: "tfidf" },
  { source: "r2", target: "controles", type: "tfidf" },
  { source: "r2", target: "diversao",  type: "tfidf" },
  { source: "r3", target: "historia",  type: "tfidf" },
  { source: "r3", target: "enredo",    type: "tfidf" },
  { source: "r4", target: "crash",     type: "tfidf" },
  { source: "r4", target: "lag",       type: "tfidf" },
  // PMI: word ↔ word
  { source: "fps",     target: "lag",       type: "pmi" },
  { source: "fps",     target: "crash",     type: "pmi" },
  { source: "lag",     target: "crash",     type: "pmi" },
  { source: "textura", target: "resolucao", type: "pmi" },
  { source: "controles", target: "diversao", type: "pmi" },
  { source: "historia",  target: "enredo",   type: "pmi" },
  // Seeds: word → category
  { source: "fps",       target: "cat_perf", type: "seed" },
  { source: "lag",       target: "cat_perf", type: "seed" },
  { source: "crash",     target: "cat_perf", type: "seed" },
  { source: "textura",   target: "cat_graf", type: "seed" },
  { source: "resolucao", target: "cat_graf", type: "seed" },
  { source: "controles", target: "cat_game", type: "seed" },
  { source: "diversao",  target: "cat_game", type: "seed" },
  { source: "historia",  target: "cat_narr", type: "seed" },
  { source: "enredo",    target: "cat_narr", type: "seed" },
];

const C = {
  review:   "#818cf8",
  word:     "#22d3ee",
  category: "#fbbf24",
};
const E = {
  tfidf: "#4ade80",
  pmi:   "#e879f9",
  seed:  "#fb923c",
};
const X = { review: 130, word: 400, category: 680 };

export default memo(function SteamGraph() {
  const svgRef = useRef(null);
  const simRef = useRef(null);
  const [filter, setFilter] = useState({ tfidf: true, pmi: true, seed: true });
  const [hovered, setHovered] = useState(null);

  const toggle = useCallback((key) => {
    setFilter(f => ({ ...f, [key]: !f[key] }));
  }, []);

  useEffect(() => {
    const el = svgRef.current;
    if (!el) return;

    const svg = d3.select(el);
    svg.selectAll("*").remove();

    const W = 820, H = 500;
    const nodes = RAW_NODES.map(n => ({ ...n }));
    const links = ALL_LINKS.filter(l => filter[l.type]).map(l => ({ ...l }));

    // Defs: arrow markers + glow filter
    const defs = svg.append("defs");

    defs.append("filter").attr("id", "glow")
      .append("feGaussianBlur").attr("stdDeviation", "3").attr("result", "blur");

    ["tfidf", "pmi", "seed"].forEach(t => {
      defs.append("marker")
        .attr("id", `arr-${t}`)
        .attr("viewBox", "0 -4 8 8")
        .attr("refX", 24).attr("refY", 0)
        .attr("markerWidth", 5).attr("markerHeight", 5)
        .attr("orient", "auto")
        .append("path")
        .attr("fill", E[t])
        .attr("d", "M0,-4L8,0L0,4");
    });

    // Column labels (drawn in SVG for precise placement)
    const colLabels = [
      { x: X.review,   label: "REVIEWS",    color: C.review },
      { x: X.word,     label: "PALAVRAS",   color: C.word },
      { x: X.category, label: "CATEGORIAS", color: C.category },
    ];
    colLabels.forEach(({ x, label, color }) => {
      svg.append("text")
        .attr("x", x).attr("y", 18)
        .attr("text-anchor", "middle")
        .attr("fill", color)
        .attr("opacity", 0.35)
        .attr("font-size", "9px")
        .attr("letter-spacing", "2px")
        .attr("font-family", "monospace")
        .text(label);
    });

    // Simulation
    const sim = d3.forceSimulation(nodes)
      .force("link",      d3.forceLink(links).id(d => d.id).distance(85).strength(0.3))
      .force("charge",    d3.forceManyBody().strength(-160))
      .force("x",         d3.forceX(d => X[d.type]).strength(0.85))
      .force("y",         d3.forceY(H / 2).strength(0.04))
      .force("collision", d3.forceCollide(26));

    simRef.current = sim;

    // Links
    const linkG = svg.append("g");
    const linkSel = linkG.selectAll("line")
      .data(links).enter().append("line")
      .attr("stroke", d => E[d.type])
      .attr("stroke-opacity", 0.5)
      .attr("stroke-width", 1.4)
      .attr("marker-end", d => `url(#arr-${d.type})`);

    // Nodes
    const nodeG = svg.append("g");
    const nodeSel = nodeG.selectAll("g")
      .data(nodes).enter().append("g")
      .style("cursor", "grab")
      .call(
        d3.drag()
          .on("start", (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
          .on("drag",  (e, d) => { d.fx = e.x; d.fy = e.y; })
          .on("end",   (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; })
      )
      .on("mouseenter", (_, d) => setHovered(d))
      .on("mouseleave", () => setHovered(null));

    // Review nodes — rounded rectangles
    nodeSel.filter(d => d.type === "review")
      .append("rect")
      .attr("width", 52).attr("height", 26)
      .attr("x", -26).attr("y", -13).attr("rx", 5)
      .attr("fill",         d => C[d.type] + "20")
      .attr("stroke",       d => C[d.type])
      .attr("stroke-width", 1.5);

    // Word nodes — circles
    nodeSel.filter(d => d.type === "word")
      .append("circle").attr("r", 19)
      .attr("fill",         d => C[d.type] + "18")
      .attr("stroke",       d => C[d.type])
      .attr("stroke-width", 1.5);

    // Category nodes — larger circles with glow
    nodeSel.filter(d => d.type === "category")
      .append("circle").attr("r", 31)
      .attr("fill",         d => C[d.type] + "22")
      .attr("stroke",       d => C[d.type])
      .attr("stroke-width", 2);

    // Labels
    nodeSel.append("text")
      .text(d => d.label)
      .attr("text-anchor", "middle")
      .attr("dominant-baseline", "central")
      .attr("fill", d => C[d.type])
      .attr("font-size", d => d.type === "category" ? "10.5px" : "9.5px")
      .attr("font-family", "monospace")
      .attr("font-weight", "600")
      .style("pointer-events", "none");

    sim.on("tick", () => {
      linkSel
        .attr("x1", d => d.source.x).attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
      nodeSel.attr("transform", d => `translate(${Math.max(40, Math.min(W - 40, d.x))},${Math.max(30, Math.min(H - 20, d.y))})`);
    });

    return () => sim.stop();
  }, [filter]);

  return (
    <div style={{ background: "transparent", minHeight: "450px", height: "100%", padding: "16px 12px", fontFamily: "monospace", color: "#e2e8f0", display: "flex", flexDirection: "column" }}>

      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: "14px" }}>
        <div style={{ fontSize: "16px", fontWeight: 700, color: "#e2e8f0", letterSpacing: "1px" }}>
          GRAFO TRIPARTIDO — STEAM REVIEWS
        </div>
        <div style={{ fontSize: "13px", color: "#475569", marginTop: "2px" }}>
          Label Propagation via Reviews → Palavras → Categorias
        </div>
      </div>

      {/* Edge type toggles */}
      <div style={{ display: "flex", gap: "8px", justifyContent: "center", marginBottom: "10px", flexWrap: "wrap" }}>
        {[["tfidf", "TF-IDF  review→palavra"], ["pmi", "PMI  palavra↔palavra"], ["seed", "Seed  palavra→categoria"]].map(([key, label]) => (
          <button key={key} onClick={() => toggle(key)} style={{
            padding: "3px 10px", borderRadius: "3px", fontSize: "13px", cursor: "pointer",
            border: `1.5px solid ${filter[key] ? E[key] : "#1e293b"}`,
            color: filter[key] ? E[key] : "#334155",
            background: filter[key] ? E[key] + "12" : "transparent",
            transition: "all 0.15s",
            letterSpacing: "0.5px",
          }}>
            {label}
          </button>
        ))}
      </div>

      {/* SVG canvas */}
      <div style={{ flex: 1, minHeight: "350px", width: "100%", position: "relative" }}>
        <svg
          ref={svgRef}
          viewBox="0 0 820 500"
          style={{ width: "100%", height: "100%", display: "block", position: "absolute", inset: 0 }}
        />
      </div>

      {/* Hover info */}
      <div style={{ textAlign: "center", minHeight: "18px", fontSize: "13px", color: "#94a3b8", margin: "4px 0" }}>
        {hovered ? (
          <span>
            <span style={{ color: C[hovered.type], fontWeight: 700 }}>{hovered.label}</span>
            {hovered.desc && <span style={{ color: "#64748b" }}> — {hovered.desc}</span>}
          </span>
        ) : (
          <span style={{ color: "#1e293b" }}>passe o mouse sobre um nó</span>
        )}
      </div>

      {/* Node type legend */}
      <div style={{ display: "flex", gap: "16px", justifyContent: "center", marginTop: "auto", flexWrap: "wrap" }}>
        {[
          ["review",   "rect",   "Review (documento)"],
          ["word",     "circle", "Palavra (token)"],
          ["category", "circle", "Categoria (seed)"],
        ].map(([type, shape, label]) => (
          <div key={type} style={{ display: "flex", alignItems: "center", gap: "6px" }}>
            <div style={{
              width: shape === "rect" ? "14px" : "10px",
              height: "10px",
              borderRadius: shape === "circle" ? "50%" : "2px",
              border: `1.5px solid ${C[type]}`,
              background: C[type] + "25",
            }} />
            <span style={{ fontSize: "12px", color: "#475569" }}>{label}</span>
          </div>
        ))}
      </div>
    </div>
  );
});
