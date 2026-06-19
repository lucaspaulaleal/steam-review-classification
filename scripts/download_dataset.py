import os
import glob
import pandas as pd

DATASET_NAME = "najzeko/steam-reviews-2021"
DESTINATION_FOLDER = "datasets"
FINAL_FILE_NAME = "steam_reviews_ptbr_top_game.csv"
REPORT_FILE_NAME = "dataset_report.txt"

# Reviews com menos de este limite de caracteres serão descartadas
MIN_REVIEW_LENGTH = 20


def download_dataset():
    """Baixa o dataset do Kaggle e descompacta na pasta datasets/."""
    from kaggle.api.kaggle_api_extended import KaggleApi
    
    print(f"[1/5] Iniciando download do dataset: {DATASET_NAME}...")
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(DATASET_NAME, path=DESTINATION_FOLDER, unzip=True)
    print("[1/5] Download concluído!")


def find_raw_csv():
    """
    Descobre dinamicamente qual arquivo CSV foi gerado após o unzip,
    ao invés de assumir um nome fixo que pode estar errado.
    """
    csv_files = glob.glob(os.path.join(DESTINATION_FOLDER, "*.csv"))

    # Ignora os arquivos que nós mesmos geramos
    our_files = [FINAL_FILE_NAME, REPORT_FILE_NAME]
    csv_files = [f for f in csv_files if os.path.basename(f) not in our_files]

    if not csv_files:
        print("Erro: Nenhum CSV encontrado na pasta datasets/ após o download.")
        print("Verifique se o dataset do Kaggle foi baixado e descompactado corretamente.")
        return None

    # Se houver múltiplos CSVs, pega o maior (provavelmente é o principal)
    biggest = max(csv_files, key=os.path.getsize)
    print(f"[2/5] Arquivo CSV detectado: {os.path.basename(biggest)} ({os.path.getsize(biggest) / (1024**2):.1f} MB)")
    return biggest


def filter_portuguese(raw_path):
    """
    Lê o CSV em chunks para não estourar a RAM,
    filtrando apenas reviews em português com texto válido.
    """
    print("[3/5] Filtrando reviews em Português...")

    chunk_size = 500_000
    ptbr_chunks = []
    total_rows_read = 0

    for chunk in pd.read_csv(raw_path, chunksize=chunk_size, low_memory=False):
        total_rows_read += len(chunk)

        # Filtra pelo idioma (trata NaN na coluna language)
        mask_lang = chunk['language'].fillna('').str.lower() == 'portuguese'
        chunk_ptbr = chunk[mask_lang].copy()

        # Remove reviews com texto vazio ou muito curto
        chunk_ptbr = chunk_ptbr[chunk_ptbr['review'].fillna('').str.len() >= MIN_REVIEW_LENGTH]

        if not chunk_ptbr.empty:
            ptbr_chunks.append(chunk_ptbr)

    if not ptbr_chunks:
        print("Erro: Nenhuma review em português encontrada no dataset!")
        return None, total_rows_read

    df_ptbr = pd.concat(ptbr_chunks, ignore_index=True)
    print(f"[3/5] Encontradas {len(df_ptbr):,} reviews em Português (de {total_rows_read:,} no total).")
    return df_ptbr, total_rows_read


def select_top_game(df_ptbr):
    """
    Identifica o jogo com mais reviews em PT-BR,
    mostra um ranking top 10 e retorna o DataFrame filtrado.
    """
    print("[4/5] Identificando o jogo mais avaliado em Português...")

    # Calcula o ranking uma única vez
    ranking = df_ptbr['app_name'].value_counts()
    top_10 = ranking.head(10)

    print("\n" + "=" * 60)
    print("  TOP 10 JOGOS MAIS AVALIADOS EM PORTUGUÊS")
    print("=" * 60)
    for i, (game, count) in enumerate(top_10.items(), 1):
        marker = " <<<" if i == 1 else ""
        print(f"  {i:2d}. {game:<35s} {count:>7,} reviews{marker}")
    print("=" * 60 + "\n")

    top_game = ranking.idxmax()
    top_count = ranking.max()

    print(f"[4/5] Selecionado: '{top_game}' com {top_count:,} reviews.")

    df_top = df_ptbr[df_ptbr['app_name'] == top_game].copy()
    return df_top, top_game, top_count, top_10


def generate_report(total_rows, total_ptbr, top_game, top_count, top_10, df_top):
    """Gera um relatório em texto com estatísticas úteis para o projeto."""
    report_path = os.path.join(DESTINATION_FOLDER, REPORT_FILE_NAME)

    lines = [
        "=" * 60,
        "  RELATÓRIO DO DATASET - STEAM REVIEWS (PT-BR)",
        "=" * 60,
        f"  Dataset original:          {total_rows:>12,} reviews",
        f"  Reviews em Português:      {total_ptbr:>12,} reviews",
        f"  Proporção PT-BR:           {total_ptbr / total_rows * 100:>11.2f}%",
        "",
        f"  Jogo selecionado:          {top_game}",
        f"  Reviews do jogo:           {top_count:>12,}",
        "",
        "  Distribuição recomendação:",
        f"    Positivas (recommended=True):  {df_top['recommended'].sum() if 'recommended' in df_top.columns else 'N/A'}",
        f"    Negativas (recommended=False): {(~df_top['recommended']).sum() if 'recommended' in df_top.columns else 'N/A'}",
        "",
        "  Tamanho médio das reviews:  "
        f"{df_top['review'].fillna('').str.len().mean():.0f} caracteres",
        "",
        "  TOP 10 JOGOS PT-BR:",
    ]
    for i, (game, count) in enumerate(top_10.items(), 1):
        lines.append(f"    {i:2d}. {game:<35s} {count:>7,}")

    lines.append("=" * 60)
    report_text = "\n".join(lines)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"\n{report_text}")
    print(f"\nRelatório salvo em: {report_path}")


def main():
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    # Passo 1: Download (pula se já houver CSVs na pasta)
    existing_csvs = glob.glob(os.path.join(DESTINATION_FOLDER, "*.csv"))
    if not existing_csvs:
        download_dataset()
    else:
        print("[1/5] Arquivos CSV já existem na pasta, pulando download...")

    # Passo 2: Detecta o CSV principal
    raw_path = find_raw_csv()
    if raw_path is None:
        return

    # Passo 3: Filtra português
    df_ptbr, total_rows = filter_portuguese(raw_path)
    if df_ptbr is None:
        return

    # Passo 4: Seleciona o top game
    df_top, top_game, top_count, top_10 = select_top_game(df_ptbr)

    # Passo 5: Salva e gera relatório
    final_path = os.path.join(DESTINATION_FOLDER, FINAL_FILE_NAME)
    df_top.to_csv(final_path, index=False)
    print(f"\n[5/5] Dataset final salvo em: {final_path}")

    generate_report(total_rows, len(df_ptbr), top_game, top_count, top_10, df_top)


if __name__ == "__main__":
    main()
