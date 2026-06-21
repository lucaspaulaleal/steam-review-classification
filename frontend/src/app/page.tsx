import SteamGraph from "../components/steam-graph";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
        {/* Header */}
        <div className={styles.header}>
            <img src="/logo.svg" alt="imagem" />
            <p>Steam Review Classification</p>
        </div>

        {/* Body*/}
        <main className={styles.main}>
            {/* Título */}
            <div className={styles.TituloJogo}>
                <p>Análise de usuários para </p>
                <h1 className={styles.NomeJogo}>NOME DO JOGO</h1>
            </div>
            
            {/* Análise Geral */}
            <div className={styles.analiseGeral}>
                {/* Blocos de resumo */}
                <div className={styles.containerGeral}>
                    {/* Resumo Pt-br */}
                    <p>ANÁLISES EM PT-BR</p>
                    <h2 className={styles.positiveAnalises}>Muito positivas</h2>
                    <p>2.000 análises</p>
                </div>
                <div className={styles.containerGeralMenor}>
                    {/* Análises todos os idiomas */}
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

            {/* Filtro de Análise */}
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

            {/* Visualização do Grafo */}
            <div style={{ marginTop: "40px", border: "1px solid #1e293b", borderRadius: "8px", overflow: "hidden" }}>
                <SteamGraph />
            </div>

            {/* Reviews */}
            <div className={styles.ContainerReviews} style={{ marginTop: "40px" }}>
                <h2>Análises mais úteis</h2>

                {/* Reviews */}
                <div>
                    {/* Reviews individuais */}
                    <div className={styles.ReviewCard}>
                        {/* cabeçalho reviews */}
                        <div className={styles.ReviewCardHeader}>
                            {/* imagem like ou dislike */}

                            <img src="/like.svg" alt="" />       
                            <div>
                                <p className={styles.ReviewRecomendation}>Não recomenda</p>
                                <p className={styles.ReviewId}>Review #0123</p>
                                {/* Categorias da review */}
                                <div className={styles.ReviewMarcadores}>
                                    <div className={styles.ReviewMarcador}>Categoria 1</div>
                                    <div className={styles.ReviewMarcador}>Categoria 2</div>
                                </div>
                            </div>

                            
                        </div>

                        {/* Conteúdo review*/}
                        <div className={styles.ReviewContent}>
                            <p>Estou deixando esta análise negativa porque o jogo tem uma base cooperativa brilhante, mas falta variedade. Depois de algumas runs, a sensação é de que a campanha repete os mesmos encontros e não entrega conteúdo suficiente para manter o grupo voltando.

                            </p>
                        </div>
                    </div>

                    {/* Reviews individuais */}

                </div>
            </div>
        </main>
      </div>
  );
}
