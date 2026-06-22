(globalThis["TURBOPACK"] || (globalThis["TURBOPACK"] = [])).push([typeof document === "object" ? document.currentScript : undefined,
"[project]/src/components/steam-graph.jsx [app-client] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "default",
    ()=>SteamGraph
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/jsx-dev-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$compiler$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/compiler-runtime.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/index.js [app-client] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2f$src$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$locals$3e$__ = __turbopack_context__.i("[project]/node_modules/d3/src/index.js [app-client] (ecmascript) <locals>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$selection$2f$src$2f$select$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__select$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-selection/src/select.js [app-client] (ecmascript) <export default as select>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$simulation$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceSimulation$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/simulation.js [app-client] (ecmascript) <export default as forceSimulation>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceLink$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/link.js [app-client] (ecmascript) <export default as forceLink>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$manyBody$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceManyBody$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/manyBody.js [app-client] (ecmascript) <export default as forceManyBody>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$x$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceX$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/x.js [app-client] (ecmascript) <export default as forceX>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$y$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceY$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/y.js [app-client] (ecmascript) <export default as forceY>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$collide$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceCollide$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-force/src/collide.js [app-client] (ecmascript) <export default as forceCollide>");
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$drag$2f$src$2f$drag$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__drag$3e$__ = __turbopack_context__.i("[project]/node_modules/d3-drag/src/drag.js [app-client] (ecmascript) <export default as drag>");
;
var _s = __turbopack_context__.k.signature();
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
    _s();
    const $ = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$compiler$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["c"])(24);
    if ($[0] !== "10efe5b9b2c4c574708e1645fda7980ea040518189557e1b5690ace5b33b7f85") {
        for(let $i = 0; $i < 24; $i += 1){
            $[$i] = Symbol.for("react.memo_cache_sentinel");
        }
        $[0] = "10efe5b9b2c4c574708e1645fda7980ea040518189557e1b5690ace5b33b7f85";
    }
    const svgRef = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useRef"])(null);
    const simRef = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useRef"])(null);
    let t0;
    if ($[1] === Symbol.for("react.memo_cache_sentinel")) {
        t0 = {
            tfidf: true,
            pmi: true,
            seed: true
        };
        $[1] = t0;
    } else {
        t0 = $[1];
    }
    const [filter, setFilter] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])(t0);
    const [hovered, setHovered] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])(null);
    const [graphData, setGraphData] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])(null);
    const [loading, setLoading] = (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useState"])(true);
    let t1;
    if ($[2] === Symbol.for("react.memo_cache_sentinel")) {
        t1 = ({
            "SteamGraph[toggle]": (key)=>{
                setFilter({
                    "SteamGraph[toggle > setFilter()]": (f)=>({
                            ...f,
                            [key]: !f[key]
                        })
                }["SteamGraph[toggle > setFilter()]"]);
            }
        })["SteamGraph[toggle]"];
        $[2] = t1;
    } else {
        t1 = $[2];
    }
    const toggle = t1;
    let t2;
    let t3;
    if ($[3] === Symbol.for("react.memo_cache_sentinel")) {
        t2 = ({
            "SteamGraph[useEffect()]": ()=>{
                fetch("http://localhost:8000/graph/mock-data").then(_SteamGraphUseEffectAnonymous).then({
                    "SteamGraph[useEffect() > (anonymous)()]": (data)=>{
                        setGraphData(data);
                        setLoading(false);
                    }
                }["SteamGraph[useEffect() > (anonymous)()]"]).catch({
                    "SteamGraph[useEffect() > (anonymous)()]": (err)=>{
                        console.error("Failed to fetch graph data:", err);
                        setLoading(false);
                    }
                }["SteamGraph[useEffect() > (anonymous)()]"]);
            }
        })["SteamGraph[useEffect()]"];
        t3 = [];
        $[3] = t2;
        $[4] = t3;
    } else {
        t2 = $[3];
        t3 = $[4];
    }
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useEffect"])(t2, t3);
    let t4;
    let t5;
    if ($[5] !== filter || $[6] !== graphData) {
        t4 = ({
            "SteamGraph[useEffect()]": ()=>{
                const el = svgRef.current;
                if (!el || !graphData) {
                    return;
                }
                const svg = __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$selection$2f$src$2f$select$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__select$3e$__["select"](el);
                svg.selectAll("*").remove();
                const nodes = graphData.nodes.map(_SteamGraphUseEffectGraphDataNodesMap);
                const links = graphData.links.filter({
                    "SteamGraph[useEffect() > graphData.links.filter()]": (l)=>filter[l.type]
                }["SteamGraph[useEffect() > graphData.links.filter()]"]).map(_SteamGraphUseEffectAnonymous2);
                const defs = svg.append("defs");
                defs.append("filter").attr("id", "glow").append("feGaussianBlur").attr("stdDeviation", "3").attr("result", "blur");
                [
                    "tfidf",
                    "pmi",
                    "seed"
                ].forEach({
                    "SteamGraph[useEffect() > (anonymous)()]": (t)=>{
                        defs.append("marker").attr("id", `arr-${t}`).attr("viewBox", "0 -4 8 8").attr("refX", 24).attr("refY", 0).attr("markerWidth", 5).attr("markerHeight", 5).attr("orient", "auto").append("path").attr("fill", E[t] || "#fff").attr("d", "M0,-4L8,0L0,4");
                    }
                }["SteamGraph[useEffect() > (anonymous)()]"]);
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
                colLabels.forEach({
                    "SteamGraph[useEffect() > colLabels.forEach()]": (t6)=>{
                        const { x, label, color } = t6;
                        svg.append("text").attr("x", x).attr("y", 18).attr("text-anchor", "middle").attr("fill", color).attr("opacity", 0.35).attr("font-size", "9px").attr("letter-spacing", "2px").attr("font-family", "monospace").text(label);
                    }
                }["SteamGraph[useEffect() > colLabels.forEach()]"]);
                const sim = __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$simulation$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceSimulation$3e$__["forceSimulation"](nodes).force("link", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$link$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceLink$3e$__["forceLink"](links).id(_SteamGraphUseEffectAnonymous3).distance(85).strength(0.3)).force("charge", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$manyBody$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceManyBody$3e$__["forceManyBody"]().strength(-160)).force("x", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$x$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceX$3e$__["forceX"](_SteamGraphUseEffectD3ForceX).strength(0.85)).force("y", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$y$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceY$3e$__["forceY"](250).strength(0.04)).force("collision", __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$force$2f$src$2f$collide$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__forceCollide$3e$__["forceCollide"](26));
                simRef.current = sim;
                const linkG = svg.append("g");
                const linkSel = linkG.selectAll("line").data(links).enter().append("line").attr("stroke", _SteamGraphUseEffectAnonymous4).attr("stroke-opacity", 0.5).attr("stroke-width", 1.4).attr("marker-end", _SteamGraphUseEffectAnonymous5);
                const nodeG = svg.append("g");
                const nodeSel = nodeG.selectAll("g").data(nodes).enter().append("g").style("cursor", "grab").call(__TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$d3$2d$drag$2f$src$2f$drag$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__$3c$export__default__as__drag$3e$__["drag"]().on("start", {
                    "SteamGraph[useEffect() > (anonymous)()]": (e, d_3)=>{
                        if (!e.active) {
                            sim.alphaTarget(0.3).restart();
                        }
                        d_3.fx = d_3.x;
                        d_3.fy = d_3.y;
                    }
                }["SteamGraph[useEffect() > (anonymous)()]"]).on("drag", _SteamGraphUseEffectAnonymous6).on("end", {
                    "SteamGraph[useEffect() > (anonymous)()]": (e_1, d_5)=>{
                        if (!e_1.active) {
                            sim.alphaTarget(0);
                        }
                        d_5.fx = null;
                        d_5.fy = null;
                    }
                }["SteamGraph[useEffect() > (anonymous)()]"])).on("mouseenter", {
                    "SteamGraph[useEffect() > (anonymous)()]": (_, d_6)=>setHovered(d_6)
                }["SteamGraph[useEffect() > (anonymous)()]"]).on("mouseleave", {
                    "SteamGraph[useEffect() > (anonymous)()]": ()=>setHovered(null)
                }["SteamGraph[useEffect() > (anonymous)()]"]);
                nodeSel.filter(_SteamGraphUseEffectNodeSelFilter).append("rect").attr("width", 52).attr("height", 26).attr("x", -26).attr("y", -13).attr("rx", 5).attr("fill", _SteamGraphUseEffectAnonymous7).attr("stroke", _SteamGraphUseEffectAnonymous8).attr("stroke-width", 1.5);
                nodeSel.filter(_SteamGraphUseEffectNodeSelFilter2).append("circle").attr("r", 19).attr("fill", _SteamGraphUseEffectAnonymous9).attr("stroke", _SteamGraphUseEffectAnonymous10).attr("stroke-width", 1.5);
                nodeSel.filter(_SteamGraphUseEffectNodeSelFilter3).append("circle").attr("r", 31).attr("fill", _SteamGraphUseEffectAnonymous11).attr("stroke", _SteamGraphUseEffectAnonymous12).attr("stroke-width", 2);
                nodeSel.append("text").text(_SteamGraphUseEffectAnonymous13).attr("text-anchor", "middle").attr("dominant-baseline", "central").attr("fill", _SteamGraphUseEffectAnonymous14).attr("font-size", _SteamGraphUseEffectAnonymous15).attr("font-family", "monospace").attr("font-weight", "600").style("pointer-events", "none");
                sim.on("tick", {
                    "SteamGraph[useEffect() > sim.on()]": ()=>{
                        linkSel.attr("x1", _SteamGraphUseEffectSimOnLinkSelAttr).attr("y1", _SteamGraphUseEffectSimOnAnonymous).attr("x2", _SteamGraphUseEffectSimOnAnonymous2).attr("y2", _SteamGraphUseEffectSimOnAnonymous3);
                        nodeSel.attr("transform", _SteamGraphUseEffectSimOnNodeSelAttr);
                    }
                }["SteamGraph[useEffect() > sim.on()]"]);
                return ()=>sim.stop();
            }
        })["SteamGraph[useEffect()]"];
        t5 = [
            filter,
            graphData
        ];
        $[5] = filter;
        $[6] = graphData;
        $[7] = t4;
        $[8] = t5;
    } else {
        t4 = $[7];
        t5 = $[8];
    }
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useEffect"])(t4, t5);
    if (loading) {
        let t6;
        if ($[9] === Symbol.for("react.memo_cache_sentinel")) {
            t6 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
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
                lineNumber: 186,
                columnNumber: 12
            }, this);
            $[9] = t6;
        } else {
            t6 = $[9];
        }
        return t6;
    }
    let t6;
    let t7;
    let t8;
    let t9;
    if ($[10] === Symbol.for("react.memo_cache_sentinel")) {
        t6 = {
            background: "#080f1e",
            minHeight: "100vh",
            padding: "16px 12px",
            fontFamily: "monospace",
            color: "#e2e8f0"
        };
        t7 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
            style: {
                textAlign: "center",
                marginBottom: "14px"
            },
            children: [
                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                    style: {
                        fontSize: "13px",
                        fontWeight: 700,
                        color: "#e2e8f0",
                        letterSpacing: "1px"
                    },
                    children: "GRAFO TRIPARTIDO — STEAM REVIEWS"
                }, void 0, false, {
                    fileName: "[project]/src/components/steam-graph.jsx",
                    lineNumber: 215,
                    columnNumber: 8
                }, this),
                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                    style: {
                        fontSize: "10px",
                        color: "#475569",
                        marginTop: "2px"
                    },
                    children: "Label Propagation via Reviews → Palavras → Categorias"
                }, void 0, false, {
                    fileName: "[project]/src/components/steam-graph.jsx",
                    lineNumber: 220,
                    columnNumber: 48
                }, this)
            ]
        }, void 0, true, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 212,
            columnNumber: 10
        }, this);
        t8 = {
            display: "flex",
            gap: "8px",
            justifyContent: "center",
            marginBottom: "10px",
            flexWrap: "wrap"
        };
        t9 = [
            [
                "tfidf",
                "TF-IDF  review\u2192palavra"
            ],
            [
                "pmi",
                "PMI  palavra\u2194palavra"
            ],
            [
                "seed",
                "Seed  palavra\u2192categoria"
            ]
        ];
        $[10] = t6;
        $[11] = t7;
        $[12] = t8;
        $[13] = t9;
    } else {
        t6 = $[10];
        t7 = $[11];
        t8 = $[12];
        t9 = $[13];
    }
    let t10;
    if ($[14] !== filter) {
        t10 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
            style: t8,
            children: t9.map({
                "SteamGraph[(anonymous)()]": (t11)=>{
                    const [key_0, label_0] = t11;
                    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("button", {
                        onClick: {
                            "SteamGraph[(anonymous)() > <button>.onClick]": ()=>toggle(key_0)
                        }["SteamGraph[(anonymous)() > <button>.onClick]"],
                        style: {
                            padding: "3px 10px",
                            borderRadius: "3px",
                            fontSize: "10px",
                            cursor: "pointer",
                            border: `1.5px solid ${filter[key_0] ? E[key_0] : "#1e293b"}`,
                            color: filter[key_0] ? E[key_0] : "#334155",
                            background: filter[key_0] ? E[key_0] + "12" : "transparent",
                            transition: "all 0.15s",
                            letterSpacing: "0.5px"
                        },
                        children: label_0
                    }, key_0, false, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 248,
                        columnNumber: 18
                    }, this);
                }
            }["SteamGraph[(anonymous)()]"])
        }, void 0, false, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 245,
            columnNumber: 11
        }, this);
        $[14] = filter;
        $[15] = t10;
    } else {
        t10 = $[15];
    }
    let t11;
    let t12;
    if ($[16] === Symbol.for("react.memo_cache_sentinel")) {
        t11 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
            ref: svgRef,
            viewBox: "0 0 820 500",
            style: {
                width: "100%",
                height: "auto",
                display: "block"
            }
        }, void 0, false, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 271,
            columnNumber: 11
        }, this);
        t12 = {
            textAlign: "center",
            minHeight: "18px",
            fontSize: "11px",
            color: "#94a3b8",
            margin: "4px 0"
        };
        $[16] = t11;
        $[17] = t12;
    } else {
        t11 = $[16];
        t12 = $[17];
    }
    let t13;
    if ($[18] !== hovered) {
        t13 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
            style: t12,
            children: hovered ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        style: {
                            color: C[hovered.type] || "#fff",
                            fontWeight: 700
                        },
                        children: hovered.label
                    }, void 0, false, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 291,
                        columnNumber: 45
                    }, this),
                    hovered.desc && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        style: {
                            color: "#64748b"
                        },
                        children: [
                            " — ",
                            hovered.desc
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/steam-graph.jsx",
                        lineNumber: 294,
                        columnNumber: 51
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 291,
                columnNumber: 39
            }, this) : /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    color: "#1e293b"
                },
                children: "passe o mouse sobre um nó"
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 296,
                columnNumber: 47
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 291,
            columnNumber: 11
        }, this);
        $[18] = hovered;
        $[19] = t13;
    } else {
        t13 = $[19];
    }
    let t14;
    if ($[20] === Symbol.for("react.memo_cache_sentinel")) {
        t14 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
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
            ].map(_SteamGraphAnonymous)
        }, void 0, false, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 306,
            columnNumber: 11
        }, this);
        $[20] = t14;
    } else {
        t14 = $[20];
    }
    let t15;
    if ($[21] !== t10 || $[22] !== t13) {
        t15 = /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
            style: t6,
            children: [
                t7,
                t10,
                t11,
                t13,
                t14
            ]
        }, void 0, true, {
            fileName: "[project]/src/components/steam-graph.jsx",
            lineNumber: 319,
            columnNumber: 11
        }, this);
        $[21] = t10;
        $[22] = t13;
        $[23] = t15;
    } else {
        t15 = $[23];
    }
    return t15;
}
_s(SteamGraph, "GVDNE07OQWM7IvXos8RMP4QO7KA=");
_c = SteamGraph;
function _SteamGraphAnonymous(t0) {
    const [type, shape, label_1] = t0;
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        style: {
            display: "flex",
            alignItems: "center",
            gap: "6px"
        },
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                style: {
                    width: shape === "rect" ? "14px" : "10px",
                    height: "10px",
                    borderRadius: shape === "circle" ? "50%" : "2px",
                    border: `1.5px solid ${C[type]}`,
                    background: C[type] + "25"
                }
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 334,
                columnNumber: 6
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                style: {
                    fontSize: "10px",
                    color: "#475569"
                },
                children: label_1
            }, void 0, false, {
                fileName: "[project]/src/components/steam-graph.jsx",
                lineNumber: 340,
                columnNumber: 10
            }, this)
        ]
    }, type, true, {
        fileName: "[project]/src/components/steam-graph.jsx",
        lineNumber: 330,
        columnNumber: 10
    }, this);
}
function _SteamGraphUseEffectSimOnNodeSelAttr(d_23) {
    return `translate(${Math.max(40, Math.min(780, d_23.x))},${Math.max(30, Math.min(480, d_23.y))})`;
}
function _SteamGraphUseEffectSimOnAnonymous3(d_22) {
    return d_22.target.y;
}
function _SteamGraphUseEffectSimOnAnonymous2(d_21) {
    return d_21.target.x;
}
function _SteamGraphUseEffectSimOnAnonymous(d_20) {
    return d_20.source.y;
}
function _SteamGraphUseEffectSimOnLinkSelAttr(d_19) {
    return d_19.source.x;
}
function _SteamGraphUseEffectAnonymous15(d_18) {
    return d_18.type === "category" ? "10.5px" : "9.5px";
}
function _SteamGraphUseEffectAnonymous14(d_17) {
    return C[d_17.type] || "#fff";
}
function _SteamGraphUseEffectAnonymous13(d_16) {
    return d_16.label;
}
function _SteamGraphUseEffectAnonymous12(d_15) {
    return C[d_15.type] || "#fff";
}
function _SteamGraphUseEffectAnonymous11(d_14) {
    return (C[d_14.type] || "#fff") + "22";
}
function _SteamGraphUseEffectNodeSelFilter3(d_13) {
    return d_13.type === "category";
}
function _SteamGraphUseEffectAnonymous10(d_12) {
    return C[d_12.type] || "#fff";
}
function _SteamGraphUseEffectAnonymous9(d_11) {
    return (C[d_11.type] || "#fff") + "18";
}
function _SteamGraphUseEffectNodeSelFilter2(d_10) {
    return d_10.type === "word";
}
function _SteamGraphUseEffectAnonymous8(d_9) {
    return C[d_9.type] || "#fff";
}
function _SteamGraphUseEffectAnonymous7(d_8) {
    return (C[d_8.type] || "#fff") + "20";
}
function _SteamGraphUseEffectNodeSelFilter(d_7) {
    return d_7.type === "review";
}
function _SteamGraphUseEffectAnonymous6(e_0, d_4) {
    d_4.fx = e_0.x;
    d_4.fy = e_0.y;
}
function _SteamGraphUseEffectAnonymous5(d_2) {
    return `url(#arr-${d_2.type})`;
}
function _SteamGraphUseEffectAnonymous4(d_1) {
    return E[d_1.type] || "#fff";
}
function _SteamGraphUseEffectD3ForceX(d_0) {
    return X[d_0.type] || 410;
}
function _SteamGraphUseEffectAnonymous3(d) {
    return d.id;
}
function _SteamGraphUseEffectAnonymous2(l_0) {
    return {
        ...l_0
    };
}
function _SteamGraphUseEffectGraphDataNodesMap(n) {
    return {
        ...n
    };
}
function _SteamGraphUseEffectAnonymous(res) {
    return res.json();
}
var _c;
__turbopack_context__.k.register(_c, "SteamGraph");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(__turbopack_context__.m, globalThis.$RefreshHelpers$);
}
}),
]);

//# sourceMappingURL=src_components_steam-graph_jsx_1izbgax._.js.map