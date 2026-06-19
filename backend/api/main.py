#backend/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.graph.builder import build_tripartite_graph, mock_documents, mock_seed_groups
from backend.propagation.label_propagation import classify_reviews, label_propagation


app = FastAPI(
    title="Steam Review Classification API",
    version="0.1.0",
    description="API inicial para classificar reviews da Steam por aspecto tecnico.",
)

#Permite que o frontend local consiga chamar a API durante desenvolvimento.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    #Endpoint minimo para confirmar que a API respondeu.
    return {
        "message": "Steam Review Classification API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    #Endpoint pensado para teste rapido de comunicacao com o frontend.
    return {
        "status": "ok",
        "service": "backend",
    }


@app.get("/reviews/mock-classifications")
def mock_classifications():
    #Executa a pipeline mockada atual e devolve dados prontos para uma tela inicial.
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups())
    scores = label_propagation(graph, iterations=30, threshold=0.0001)
    classifications = classify_reviews(graph, scores)

    response = []
    for review_label, category, score, category_scores in classifications:
        response.append(
            {
                "review": review_label,
                "category": category,
                "score": score,
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
