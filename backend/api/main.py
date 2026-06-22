# backend/api/main.py

from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os
from backend.classification.realtime import classify_review_text
from backend.graph.builder import build_tripartite_graph, mock_documents, mock_seed_groups
from backend.propagation.label_propagation import classify_reviews, label_propagation
from backend.utils import binary_search_tuples, sorted_insert_tuple
from backend.preprocessing.tf_idf import _build_df_table, calculate_tf_idf
from backend.graph.pmi import _build_cooccurrence_tables, calculate_pmi
from backend.graph.graph import Graph


class ReviewClassificationRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    tf_idf_threshold: float = Field(default=0.0, ge=0.0, description="Threshold for TF-IDF edges")
    pmi_threshold: float = Field(default=0.0, ge=0.0, description="Threshold for PMI edges")
    damping_factor: float = Field(default=0.85, ge=0.0, le=1.0, description="Damping factor for Label Propagation")

app = FastAPI(
    title="Steam Review Classification API",
    version="0.2.0",
    description="API para classificar reviews da Steam por aspecto técnico.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Steam Review Classification API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend",
    }


@app.get("/reviews/mock-classifications")
def mock_classifications(
    tf_idf_threshold: float = Query(0.0, ge=0.0, description="Threshold for TF-IDF edges"),
    pmi_threshold: float = Query(0.0, ge=0.0, description="Threshold for PMI edges"),
    damping_factor: float = Query(0.85, ge=0.0, le=1.0, description="Damping factor for Label Propagation"),
    iterations: int = Query(30, ge=1, le=100, description="Number of iterations")
):
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups(), tf_idf_threshold=tf_idf_threshold, pmi_threshold=pmi_threshold)
    scores = label_propagation(graph, iterations=iterations, threshold=0.0001, damping_factor=damping_factor)
    classifications = classify_reviews(graph, scores)
    response = []
    for review_label, category, score, category_scores, top_words in classifications:
        response.append(
            {
                "review": review_label,
                "category": category,
                "score": score,
                "top_words": [{"word": w, "influence": round(inf, 6)} for w, inf in top_words],
                "scores": [
                    {"category": score_label, "score": score_value}
                    for score_label, score_value in category_scores
                ],
            }
        )
    return {
        "items": response,
        "count": len(response),
    }


@app.get("/reviews/dataset")
def get_dataset_reviews(limit: int = 5):
    """Retorna as top reviews do dataset real baseado em votos úteis."""
    import json
    cache_path = "datasets/steam_reviews_cache.json"
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
            
    csv_path = "datasets/steam_reviews_ptbr_top_game.csv"
    if not os.path.exists(csv_path):
        return {"items": [], "count": 0, "message": "Dataset não encontrado."}
    
    try:
        df = pd.read_csv(csv_path)
        # Ordena pelas mais úteis
        if 'votes_helpful' in df.columns:
            df = df.sort_values(by='votes_helpful', ascending=False)
        
        import re
        records = []
        buckets = {
            "Performance": [],
            "Gameplay": [],
            "Gráfico": [],
            "Narrativa": [],
            "Outros": []
        }
        
        # Palavras indicativas de português vs ingles
        pt_words = r'\b(que|não|sim|jogo|muito|bom|ruim|mais|para|com|como|mas|ele|ela|uma|um|jogar|história|graficos|gráfico)\b'
        eng_words = r'\b(the|and|this|game|is|it|that|for|with|best|worst|ever)\b'
        
        from backend.classification.realtime import classify_review_text

        for _, row in df.iterrows():
            text = str(row['review'])
            
            # Filtro rígido de idioma (Pula se não tiver PT-BR ou se tiver muita palavra em INGLÊS)
            if len(text) < 15:
                continue
            if len(re.findall(pt_words, text.lower())) < 1:
                continue
            if len(re.findall(eng_words, text.lower())) >= 2:
                continue
                
            cls = classify_review_text(text)
            category = cls["category"] if cls else "Outros"
            top_words = cls["top_words"] if cls and "top_words" in cls else []
            
            # Normalização de nomenclatura
            if "grafic" in category.lower() or "gráfic" in category.lower():
                category = "Gráfico"
            
            if category not in buckets:
                buckets[category] = []
                
            buckets[category].append({
                "review_id": row['review_id'],
                "review": text,
                "recommended": row['recommended'],
                "votes_helpful": row['votes_helpful'],
                "category": category,
                "top_words": top_words,
            })
            
            total_collected = sum(len(v) for v in buckets.values())
            
            # Cotas mínimas (para garantir mais volume)
            has_min_quota = (
                len(buckets.get("Performance", [])) >= 15 and
                len(buckets.get("Gameplay", [])) >= 15 and
                len(buckets.get("Gráfico", [])) >= 15 and
                len(buckets.get("Narrativa", [])) >= 15
            )
            
            # Para de processar se atingiu as cotas E atingiu um bom limite
            if has_min_quota and total_collected >= 100:
                break
                
            # Segurança para não processar o CSV inteiro se as cotas não forem batidas
            if total_collected >= 250:
                break
                
        for cat_list in buckets.values():
            records.extend(cat_list)
            
        # Re-ordena as classificadas
        records = sorted(records, key=lambda x: x["votes_helpful"], reverse=True)
            
        result = {"items": records, "count": len(records)}
        
        # Salva o cache
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler CSV: {str(e)}")


@app.get("/graph/mock-data")
def mock_graph_data(
    tf_idf_threshold: float = Query(0.0, ge=0.0, description="Threshold for TF-IDF edges"),
    pmi_threshold: float = Query(0.0, ge=0.0, description="Threshold for PMI edges")
):
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups(), tf_idf_threshold=tf_idf_threshold, pmi_threshold=pmi_threshold)

    nodes = []
    for idx in range(graph.size()):
        nodes.append(
            {
                "id": graph.labels[idx],
                "label": graph.labels[idx],
                "type": graph.node_types[idx],
            }
        )

    links = []
    for source_idx in range(graph.size()):
        source_type = graph.node_types[source_idx]
        for target_idx, weight in graph.get_neighbors_by_idx(source_idx):
            target_type = graph.node_types[target_idx]
            edge_type = "tfidf"

            if source_type == "word" and target_type == "word":
                edge_type = "pmi"
            elif source_type == "word" and target_type == "category":
                edge_type = "seed"

            links.append(
                {
                    "source": graph.labels[source_idx],
                    "target": graph.labels[target_idx],
                    "type": edge_type,
                    "weight": weight,
                }
            )

    return {
        "nodes": nodes,
        "links": links,
    }


@app.post("/reviews/classify")
def classify_review(request: ReviewClassificationRequest):
    result = classify_review_text(
        request.text, 
        tf_idf_threshold=request.tf_idf_threshold, 
        pmi_threshold=request.pmi_threshold, 
        damping_factor=request.damping_factor
    )

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="A review precisa conter pelo menos uma palavra relevante.",
        )

    return result


# ─────────────────────────────────────────────────────────────
# ROTA DE DEMONSTRAÇÃO DA ISSUE #3
# ─────────────────────────────────────────────────────────────

@app.get(
    "/demo/binary-search",
    summary="Demonstração — Issue #3: Busca Binária no Grafo + TF-IDF + PMI",
    tags=["Demo Issue #3"],
)
def demo_binary_search(
    palavra: str = Query(
        default="fps",
        description="Palavra para demonstrar a busca binária nas três estruturas.",
    )
):
    """
    Demonstra as quatro otimizações da Issue #3 usando os documentos mock.

    - **Passo 1** — `binary_search_tuples` na df_table (TF-IDF)
    - **Passo 2** — `_find_node_idx` via node_map ordenado (Grafo)
    - **Passo 3** — `_build_df_table` com passagem única (TF-IDF)
    - **Passo 4** — `_build_cooccurrence_tables` com busca binária (PMI)
    """
    documents = mock_documents()
    from backend.preprocessing.nlp import clean_text
    tokens = clean_text(palavra)
    palavra_buscada = tokens[0] if tokens else palavra.lower()

    # ── PASSO 1 & 3 — df_table (TF-IDF) ──────────────────────────────────
    df_table = _build_df_table(documents)
    df_pos = binary_search_tuples(df_table, palavra_buscada)

    df_result = {
        "tabela_ordenada": [{"token": t, "df": c} for t, c in df_table],
        "busca_por": palavra_buscada,
        "posicao_encontrada": df_pos,
        "document_frequency": df_table[df_pos][1] if df_pos != -1 else None,
        "encontrado": df_pos != -1,
    }

    # ── PASSO 2 — node_map do Grafo ───────────────────────────────────────
    graph = build_tripartite_graph(documents, mock_seed_groups())

    node_label = "word:" + palavra_buscada
    node_idx = graph._find_node_idx(node_label)
    vizinhos = []
    if node_idx != -1:
        for v_idx, weight in graph.adj[node_idx]:
            vizinhos.append({
                "vizinho": graph.labels[v_idx],
                "peso": round(weight, 6),
                "idx_numerico": v_idx,
            })

    graph_result = {
        "node_map_primeiros_10": [
            {"label": lbl, "idx": idx}
            for lbl, idx in graph.node_map[:10]
        ],
        "total_nos": graph.size(),
        "busca_por": node_label,
        "idx_encontrado": node_idx,
        "encontrado": node_idx != -1,
        "vizinhos_ordenados_por_idx": vizinhos,
    }

    # ── PASSO 4 — cooccurrence tables (PMI) ───────────────────────────────
    word_counts, pair_counts = _build_cooccurrence_tables(documents)

    wc_pos = binary_search_tuples(word_counts, palavra_buscada)

    pares_com_palavra = []
    for par, contagem in pair_counts:
        if palavra_buscada in par:
            outra = par[1] if par[0] == palavra_buscada else par[0]
            pares_com_palavra.append({
                "par": list(par),
                "outra_palavra": outra,
                "coocorrencias": contagem,
            })

    pmi_result = {
        "word_counts_ordenado": [{"palavra": w, "docs": c} for w, c in word_counts],
        "busca_por": palavra_buscada,
        "posicao_em_word_counts": wc_pos,
        "total_docs_com_palavra": word_counts[wc_pos][1] if wc_pos != -1 else None,
        "encontrado": wc_pos != -1,
        "pares_que_contem_a_palavra": pares_com_palavra,
        "total_pares_no_corpus": len(pair_counts),
    }

    # ── TF-IDF completo por review ─────────────────────────────────────────
    tfidf_result = calculate_tf_idf(documents)
    reviews_com_palavra = []
    for review_label, termos in tfidf_result:
        pos = binary_search_tuples(termos, palavra_buscada)
        # termos não são ordenados após cálculo, então fazemos busca linear aqui
        score = next((s for t, s in termos if t == palavra_buscada), None)
        if score is not None:
            reviews_com_palavra.append({
                "review": review_label,
                "tf_idf_score": round(score, 6),
            })

    return {
        "palavra_buscada": palavra_buscada,
        "passo_1_e_3_tf_idf_df_table": df_result,
        "passo_2_grafo_node_map": graph_result,
        "passo_4_pmi_cooccurrence": pmi_result,
        "tfidf_por_review": {
            "reviews_que_contem_a_palavra": reviews_com_palavra,
            "total_reviews": len(tfidf_result),
        },
    }
