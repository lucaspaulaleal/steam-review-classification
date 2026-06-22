module.exports = [
"[project]/src/components/steam-graph.jsx [app-ssr] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "default",
    ()=>SteamGraph
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/server/route-modules/app-page/vendored/ssr/react-jsx-dev-runtime.js [app-ssr] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/server/route-modules/app-page/vendored/ssr/react.js [app-ssr] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2f$src$2f$index$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__ = __turbopack_context__.i("[project]/node_modules/d3/src/index.js [app-ssr] (ecmascript) <locals>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$selection$2f$src$2f$select$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__select$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-selection/src/select.js [app-ssr] (ecmascript) <export default as select>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$simulation$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceSimulation$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/simulation.js [app-ssr] (ecmascript) <export default as forceSimulation>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$link$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceLink$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/link.js [app-ssr] (ecmascript) <export default as forceLink>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$manyBody$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceManyBody$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/manyBody.js [app-ssr] (ecmascript) <export default as forceManyBody>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$x$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceX$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/x.js [app-ssr] (ecmascript) <export default as forceX>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$y$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceY$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/y.js [app-ssr] (ecmascript) <export default as forceY>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$collide$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceCollide$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/collide.js [app-ssr] (ecmascript) <export default as forceCollide>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$drag$2f$src$2f$drag$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__drag$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-drag/src/drag.js [app-ssr] (ecmascript) <export default as drag>");
"use client";
;
;
;
const C = {
    review: "#818cf8",
    word: "#22d3ee",
    category: "#fbbf24"
};
const E = {
    tfidf: "#4ade80",
    pmi: "#e879f9",
    seed: "#fb923c"
};
const X = {
    review: 130,
    word: 400,
    category: 680
};
function SteamGraph() {
    const svgRef = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useRef"])(null);
    const simRef = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useRef"])(null);
    const [filter, setFilter] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useState"])({
        tfidf: true,
        pmi: true,
        seed: true
    });
    const [hovered, setHovered] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useState"])(null);
    const [graphData, setGraphData] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useState"])(null);
    const [loading, setLoading] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useState"])(true);
    const toggle = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useCallback"])((key)=>{
        setFilter((f)=>({
                ...f,
                [key]: !f[key]
            }));
    }, []);
    // Fetch data from FastAPI
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useEffect"])(()=>{
        fetch("http://localhost:8000/graph/mock-data").then((res)=>res.json()).then((data)=>{
            setGraphData(data);
            setLoading(false);
        }).catch((err)=>{
            console.error("Failed to fetch graph data:", err);
            setLoading(false);
        });
    }, []);
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useEffect"])(()=>{
        const el = svgRef.current;
        if (!el || !graphData) return;
        const svg = __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$selection$2f$src$2f$select$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__select$3e$__["select"](el);
        svg.selectAll("*").remove();
        const W = 820, H = 500;
        const nodes = graphData.nodes.map((n)=>({
                ...n
            }));
        const links = graphData.links.filter((l)=>filter[l.type]).map((l)=>({
                ...l
            }));
        // Defs: arrow markers + glow filter
        const defs = svg.append("defs");
        defs.append("filter").attr("id", "glow").append("feGaussianBlur").attr("stdDeviation", "3").attr("result", "blur");
        [
            "tfidf",
            "pmi",
            "seed"
        ].forEach((t)=>{
            defs.append("marker").attr("id", `arr-${t}`).attr("viewBox", "0 -4 8 8").attr("refX", 24).attr("refY", 0).attr("markerWidth", 5).attr("markerHeight", 5).attr("orient", "auto").append("path").attr("fill", E[t] || "#fff").attr("d", "M0,-4L8,0L0,4");
        });
        // Column labels
        const colLabels = [
            {
                x: X.review,
                label: "REVIEWS",
                color: C.review
            },
            {
                x: X.word,
                label: "PALAVRAS",
                color: C.word
            },
            {
                x: X.category,
                label: "CATEGORIAS",
                color: C.category
            }
        ];
        colLabels.forEach(({ x, label, color })=>{
            svg.append("text").attr("x", x).attr("y", 18).attr("text-anchor", "middle").attr("fill", color).attr("opacity", 0.35).attr("font-size", "9px").attr("letter-spacing", "2px").attr("font-family", "monospace").text(label);
        });
        // Simulation
        const sim = __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$simulation$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceSimulation$3e$__["forceSimulation"](nodes).force("link", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$link$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceLink$3e$__["forceLink"](links).id((d)=>d.id).distance(85).strength(0.3)).force("charge", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$manyBody$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceManyBody$3e$__["forceManyBody"]().strength(-160)).force("x", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$x$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceX$3e$__["forceX"]((d)=>X[d.type] || W / 2).strength(0.85)).force("y", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$y$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceY$3e$__["forceY"](H / 2).strength(0.04)).force("collision", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$collide$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__forceCollide$3e$__["forceCollide"](26));
        simRef.current = sim;
        // Links
        const linkG = svg.append("g");
        const linkSel = linkG.selectAll("line").data(links).enter().append("line").attr("stroke", (d)=>E[d.type] || "#fff").attr("stroke-opacity", 0.5).attr("stroke-width", 1.4).attr("marker-end", (d)=>`url(#arr-${d.type})`);
        // Nodes
        const nodeG = svg.append("g");
        const nodeSel = nodeG.selectAll("g").data(nodes).enter().append("g").style("cursor", "grab").call(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$drag$2f$src$2f$drag$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$export__default__as__drag$3e$__["drag"]().on("start", (e, d)=>{
            if (!e.active) sim.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }).on("drag", (e, d)=>{
            d.fx = e.x;
            d.fy = e.y;
        }).on("end", (e, d)=>{
            if (!e.active) sim.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        })).on("mouseenter", (_, d)=>setHovered(d)).on("mouseleave", ()=>setHovered(null));
        // Review nodes — rounded rectangles
        nodeSel.filter((d)=>d.type === "review").append("rect").attr("width", 52).attr("height", 26).attr("x", -26).attr("y", -13).attr("rx", 5).attr("fill", (d)=>(C[d.type] || "#fff") + "20").attr("stroke", (d)=>C[d.type] || "#fff").attr("stroke-width", 1.5);
        // Word nodes — circles
        nodeSel.filter((d)=>d.type === "word").append("circle").attr("r", 19).attr("fill", (d)=>(C[d.type] || "#fff") + "18").attr("stroke", (d)=>C[d.type] || "#fff").attr("stroke-width", 1.5);
        // Category nodes — larger circles with glow
        nodeSel.filter((d)=>d.type === "category").append("circle").attr("r", 31).attr("fill", (d)=>(C[d.type] || "#fff") + "22").attr("stroke", (d)=>C[d.type] || "#fff").attr("stroke-width", 2);
        // Labels
        nodeSel.append("text").text((d)=>d.label).attr("text-anchor", "middle").attr("dominant-baseline", "central").attr("fill", (d)=>C[d.type] || "#fff").attr("font-size", (d)=>d.type === "category" ? "10.5px" : "9.5px").attr("font-family", "monospace").attr("font-weight", "600").style("pointer-events", "none");
        sim.on("tick", ()=>{
            linkSel.attr("x1", (d)=>d.source.x).attr("y1", (d)=>d.source.y).attr("x2", (d)=>d.target.x).attr("y2", (d)=>d.target.y);
            nodeSel.attr("transform", (d)=>`translate(${Math.max(40, Math.min(W - 40, d.x))},${Math.max(30, Math.min(H - 20, d.y))})`);
        });
        return ()=>sim.stop();
    }, [
        filter,
        graphData
    ]);
    if (loading) {
        return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
            style: {
                background: "#080f1e",
                minHeight: "100vh",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                color: "#e2e8f0"
            },
            children: "Carregando grafo..."
        }, void 0, false, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 170,
            columnNumber: 7
        }, this);
    }
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            background: "#080f1e",
            minHeight: "100vh",
            padding: "16px 12px",
            fontFamily: "monospace",
            color: "#e2e8f0"
        },
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    textAlign: "center",
                    marginBottom: "14px"
                },
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        style: {
                            fontSize: "13px",
                            fontWeight: 700,
                            color: "#e2e8f0",
                            letterSpacing: "1px"
                        },
                        children: "GRAFO TRIPARTIDO — STEAM REVIEWS"
                    }, void 0, false, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 180,
                        columnNumber: 9
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        style: {
                            fontSize: "10px",
                            color: "#475569",
                            marginTop: "2px"
                        },
                        children: "Label Propagation via Reviews → Palavras → Categorias"
                    }, void 0, false, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 183,
                        columnNumber: 9
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 179,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    display: "flex",
                    gap: "8px",
                    justifyContent: "center",
                    marginBottom: "10px",
                    flexWrap: "wrap"
                },
                children: [
                    [
                        "tfidf",
                        "TF-IDF  review→palavra"
                    ],
                    [
                        "pmi",
                        "PMI  palavra↔palavra"
                    ],
                    [
                        "seed",
                        "Seed  palavra→categoria"
                    ]
                ].map(([key, label])=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("button", {
                        onClick: ()=>toggle(key),
                        style: {
                            padding: "3px 10px",
                            borderRadius: "3px",
                            fontSize: "10px",
                            cursor: "pointer",
                            border: `1.5px solid ${filter[key] ? E[key] : "#1e293b"}`,
                            color: filter[key] ? E[key] : "#334155",
                            background: filter[key] ? E[key] + "12" : "transparent",
                            transition: "all 0.15s",
                            letterSpacing: "0.5px"
                        },
                        children: label
                    }, key, false, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 191,
                        columnNumber: 11
                    }, this))
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 189,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                ref: svgRef,
                viewBox: "0 0 820 500",
                style: {
                    width: "100%",
                    height: "auto",
                    display: "block"
                }
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 205,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    textAlign: "center",
                    minHeight: "18px",
                    fontSize: "11px",
                    color: "#94a3b8",
                    margin: "4px 0"
                },
                children: hovered ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                    children: [
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                            style: {
                                color: C[hovered.type] || "#fff",
                                fontWeight: 700
                            },
                            children: hovered.label
                        }, void 0, false, {
                            fileName: "[project]/src/components/steam-graph.jsx",
                            lineNumber: 215,
                            columnNumber: 13
                        }, this),
                        hovered.desc && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                            style: {
                                color: "#64748b"
                            },
                            children: [
                                " — ",
                                hovered.desc
                            ]
                        }, void 0, true, {
                            fileName: "[project]/src/components/steam-graph.jsx",
                            lineNumber: 216,
                            columnNumber: 30
                        }, this)
                    ]
                }, void 0, true, {
                    fileName: "[project]/src/components/steam-graph.jsx",
                    lineNumber: 214,
                    columnNumber: 11
                }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                    style: {
                        color: "#1e293b"
                    },
                    children: "passe o mouse sobre um nó"
                }, void 0, false, {
                    fileName: "[project]/src/components/steam-graph.jsx",
                    lineNumber: 219,
                    columnNumber: 11
                }, this)
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 212,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    display: "flex",
                    gap: "16px",
                    justifyContent: "center",
                    marginTop: "6px",
                    flexWrap: "wrap"
                },
                children: [
                    [
                        "review",
                        "rect",
                        "Review (documento)"
                    ],
                    [
                        "word",
                        "circle",
                        "Palavra (token)"
                    ],
                    [
                        "category",
                        "circle",
                        "Categoria (seed)"
                    ]
                ].map(([type, shape, label])=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        style: {
                            display: "flex",
                            alignItems: "center",
                            gap: "6px"
                        },
                        children: [
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                style: {
                                    width: shape === "rect" ? "14px" : "10px",
                                    height: "10px",
                                    borderRadius: shape === "circle" ? "50%" : "2px",
                                    border: `1.5px solid ${C[type]}`,
                                    background: C[type] + "25"
                                }
                            }, void 0, false, {
                                fileName: "[project]/src/components/steam-graph.jsx",
                                lineNumber: 231,
                                columnNumber: 13
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                style: {
                                    fontSize: "10px",
                                    color: "#475569"
                                },
                                children: label
                            }, void 0, false, {
                                fileName: "[project]/src/components/steam-graph.jsx",
                                lineNumber: 238,
                                columnNumber: 13
                            }, this)
                        ]
                    }, type, true, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 230,
                        columnNumber: 11
                    }, this))
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 224,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/src/components/steam-graph.jsx",
        lineNumber: 177,
        columnNumber: 5
    }, this);
}
}),
];

//# sourceMappingURL=src_components_steam-graph_jsx_0r26zvy._.js.map