"use client";

import { FormEvent, useEffect, useMemo, useState } from "react";
import Image from "next/image";
import SteamGraph from "../components/steam-graph";
import styles from "./page.module.css";

type DatasetReview = {
  review_id: number;
  review: string;
  recommended: boolean;
  votes_helpful: number;
  category: string;
};

type CategoryScore = {
  category: string;
  score: number;
};

type ClassificationResult = {
  review: string;
  category: string;
  score: number;
  tokens: string[];
  scores: CategoryScore[];
};

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

function percent(value: number) {
  return Math.round(value * 100);
}

function categoryClass(category: string) {
  const normalized = category.toLowerCase();
  if (normalized.includes("performance")) return styles.performance;
  if (normalized.includes("graf")) return styles.graficos;
  if (normalized.includes("gameplay")) return styles.gameplay;
  if (normalized.includes("narrativa")) return styles.narrativa;
  return "";
}

export default function Home() {
  const [reviewText, setReviewText] = useState("");
  const [result, setResult] = useState<ClassificationResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [datasetReviews, setDatasetReviews] = useState<DatasetReview[]>([]);
  const [filterCategory, setFilterCategory] = useState("Todas");
  const [sortOrder, setSortOrder] = useState<"desc" | "asc">("desc");

  useEffect(() => {
    async function loadDataset() {
      try {
        const res = await fetch(`${API_URL}/reviews/dataset?limit=100`);
        const data = await res.json();
        if (data.items) {
          setDatasetReviews(data.items);
        }
      } catch (err) {
        console.error("Erro ao carregar dataset:", err);
      }
    }
    loadDataset();
  }, []);

  const canSubmit = useMemo(
    () => reviewText.trim().length > 0 && !isLoading,
    [reviewText, isLoading],
  );

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!canSubmit) return;

    setIsLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/reviews/classify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: reviewText }),
      });

      const body = await response.json();
      if (!response.ok) {
        throw new Error(body.detail ?? "Não foi possível classificar a review.");
      }

      setResult(body);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Não foi possível classificar a review.");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <div>
          <Image src="/logo.svg" alt="Steam Review Classification" width={40} height={40} />
          <p>Steam Review Classification</p>
        </div>
      </header>

      <main className={styles.main}>
        <div className={styles.gridContainer}>
          
          {/* COLUNA ESQUERDA: Conteúdo Principal */}
          <div className={styles.leftColumn}>
            
            <div className={styles.TituloJogo}>
              <p>Análise de usuários para</p>
              <h1 className={styles.NomeJogo}>Grand Theft Auto V</h1>
            </div>

            <div className={styles.analiseGeral}>
              <div className={styles.containerGeral}>
                <p>ANÁLISES DA COMUNIDADE (Kaggle)</p>
                <h2 className={styles.positiveAnalises}>Ligeiramente Positivas</h2>
                <p>2.800 análises processadas</p>
              </div>
              <div className={styles.containerGeralMenor}>
                <div className={styles.containerGeral}>
                  <p>Análises Totais (Steam): <span>+ 1.6 Milhões</span></p>
                  <p className={styles.positiveAnalises}>Muito Positivas</p>
                </div>
                <div className={styles.containerGeral}>
                  <p>Lançamento (PC): <span>14 de Abril de 2015</span></p>
                  <p className={styles.positiveAnalises}>Rockstar Games</p>
                </div>
              </div>
            </div>

            <div className={styles.ContainerFiltro}>
              <p>FILTROS DE ANÁLISE</p>
              <div className={styles.buttonSection}>
                <button 
                  className={styles.button}
                  onClick={() => setSortOrder(prev => prev === "desc" ? "asc" : "desc")}
                >
                  Ordenar por: Votos Úteis ({sortOrder === "desc" ? "Maior para Menor" : "Menor para Maior"})
                </button>
              </div>
              <hr />
              <div className={styles.containerCategorias}>
                <p>Categorias</p>
                {["Todas", "Narrativa", "Performance", "Gráfico", "Gameplay"].map((cat) => (
                  <button 
                    key={cat} 
                    className={`${styles.filterPill} ${filterCategory === cat ? styles.filterPillActive : ""}`}
                    onClick={() => setFilterCategory(cat)}
                  >
                    {cat}
                  </button>
                ))}
              </div>
            </div>

            <div className={styles.ContainerReviews}>
              <h2>Análises mais úteis do Kaggle</h2>

              {datasetReviews.length === 0 && (
                <p style={{ marginTop: "1rem", color: "var(--light-gray)" }}>
                  Carregando análises do dataset...
                </p>
              )}

              {datasetReviews
                .filter(rev => rev.category !== "Outros") // Remove a categoria Outros por completo
                .filter(rev => filterCategory === "Todas" || rev.category.toLowerCase().includes(filterCategory.toLowerCase()))
                .sort((a, b) => sortOrder === "desc" ? b.votes_helpful - a.votes_helpful : a.votes_helpful - b.votes_helpful)
                .map((rev) => (
                    <div key={rev.review_id} className={styles.ReviewCard}>
                        <div className={styles.ReviewCardHeader}>
                            <div className={styles.ReviewIconContainer}>
                                <Image 
                                    src={rev.recommended ? "/like.svg" : "/dislike.svg"} 
                                    alt="" 
                                    width={32} 
                                    height={32} 
                                    className={rev.recommended ? styles.iconLike : styles.iconDislike}
                                />
                            </div>

                                   
                            <div className={styles.ReviewInfo}>
                                <p className={rev.recommended ? styles.ReviewRecomendationPos : styles.ReviewRecomendationNeg}>
                                    {rev.recommended ? "Recomenda" : "Não recomenda"}
                                </p>
                                <p className={styles.ReviewId}>
                                    Review #{rev.review_id} ({rev.votes_helpful} votos úteis)
                                </p>
                            </div>
                                    
                            <div className={styles.ReviewMarcadores}>
                                <p className={`${styles.ReviewMarcador} ${categoryClass(rev.category)}`}>
                                    {rev.category}
                                </p>
                            </div>
    
                        </div>

                        <div className={styles.ReviewContent}>
                            <p>{rev.review}</p>
                        </div>
                    </div>
                ))}
            </div>
            
          </div>

          {/* COLUNA DIREITA: Ferramentas (Grafo e Classificador) */}
          <div className={styles.rightColumn}>

            <section className={styles.realtimeClassifier}>
              <div className={styles.realtimeHeader}>
                <div>
                  <p className={styles.sectionEyebrow}>CLASSIFICAÇÃO EM TEMPO REAL</p>
                  <h2>Review manual</h2>
                </div>
                {result ? (
                  <span className={`${styles.categoryBadge} ${categoryClass(result.category)}`}>
                    {result.category}
                  </span>
                ) : null}
              </div>

              <form className={styles.classifierForm} onSubmit={handleSubmit}>
                <textarea
                  className={styles.reviewInput}
                  value={reviewText}
                  onChange={(event) => setReviewText(event.target.value)}
                  placeholder="Digite uma review da Steam..."
                  maxLength={5000}
                />
                <div className={styles.formFooter}>
                  <span>{reviewText.length}/5000</span>
                  <button className={styles.classifyButton} disabled={!canSubmit} type="submit">
                    {isLoading ? "Classificando..." : "Classificar"}
                  </button>
                </div>
              </form>

              {error ? <p className={styles.errorMessage}>{error}</p> : null}

              {result ? (
                <div className={styles.resultPanel}>
                  <div className={styles.resultSummary}>
                    <span>Categoria predominante</span>
                    <strong>{result.category}</strong>
                    <p>{percent(result.score)}% de confiança relativa</p>
                  </div>

                  <div className={styles.scoreList}>
                    {result.scores.map((item) => {
                      const scorePercent = percent(item.score);
                      return (
                        <div className={styles.scoreItem} key={item.category}>
                          <div className={styles.scoreHeader}>
                            <span>{item.category}</span>
                            <strong>{scorePercent}%</strong>
                          </div>
                          <div className={styles.scoreTrack}>
                            <div
                              className={`${styles.scoreFill} ${categoryClass(item.category)}`}
                              style={{ width: `${scorePercent}%` }}
                            />
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  <div className={styles.tokenList}>
                    {result.tokens.slice(0, 12).map((token) => (
                      <span key={token}>{token}</span>
                    ))}
                  </div>
                </div>
              ) : null}
            </section>

            <div className={styles.graphPanel}>
              <SteamGraph />
            </div>

          </div>
          
        </div>
      </main>
    </div>
  );
}
