"use client";

import { FormEvent, useMemo, useState } from "react";
import Image from "next/image";
import SteamGraph from "../components/steam-graph";
import styles from "./page.module.css";

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
      <div className={styles.header}>
        <div>
            <Image src="/logo.svg" alt="Steam Review Classification" width={40} height={40} />
            <p>Steam Review Classification</p>
        </div>
      </div>

      <main className={styles.main}>
        <div className={styles.TituloJogo}>
          <p>Análise de usuários para</p>
          <h1 className={styles.NomeJogo}>Grand Theft Auto V</h1>
        </div>

        <div className={styles.analiseGeral}>
          <div className={styles.containerGeral}>
            <p>ANÁLISES EM PT-BR</p>
            <h2 className={styles.positiveAnalises}>Muito positivas</h2>
            <p>2.000 análises</p>
          </div>
          <div className={styles.containerGeralMenor}>
            <div className={styles.containerGeral}>
              <p>Análise em todos os idiomas: <span>124.874</span></p>
              <p className={styles.positiveAnalises}>Muito positivas</p>
            </div>
            <div className={styles.containerGeral}>
              <p>Análise em todos os idiomas: <span>124.874</span></p>
              <p className={styles.positiveAnalises}>Muito positivas</p>
            </div>
          </div>
        </div>

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

        <div className={styles.ContainerFiltro}>
          <p>FILTROS DE ANÁLISE</p>
          <div className={styles.buttonSection}>
            <button className={styles.button}>Idiomas</button>
            <button className={styles.button}>Ordenar por: Data de publicação</button>
            <button className={styles.button}>Recomendação: ambas</button>
          </div>
          <hr />
          <div className={styles.containerCategorias}>
            <p>Categorias</p>
            <button>Todas</button>
            <button>Narrativa</button>
            <button>Performance</button>
            <button>Gráfico</button>
            <button>Gameplay</button>
          </div>
        </div>

        <div className={styles.graphPanel}>
          <SteamGraph />
        </div>

        <div className={styles.ContainerReviews}>
          <h2>Análises mais úteis</h2>

          <div className={styles.ReviewCard}>
            <div className={styles.ReviewCardHeader}>
              <Image src="/like.svg" alt="" width={48} height={48} />
              <div>
                <p className={styles.ReviewRecomendation}>Não recomenda</p>
                <p className={styles.ReviewId}>Review #0123</p>
                <div className={styles.ReviewMarcadores}>
                  <div className={styles.ReviewMarcador}>Categoria 1</div>
                  <div className={styles.ReviewMarcador}>Categoria 2</div>
                </div>
              </div>
            </div>

            <div className={styles.ReviewContent}>
              <p>
                Estou deixando esta análise negativa porque o jogo tem uma base cooperativa brilhante,
                mas falta variedade. Depois de algumas runs, a sensação é de que a campanha repete os
                mesmos encontros e não entrega conteúdo suficiente para manter o grupo voltando.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
