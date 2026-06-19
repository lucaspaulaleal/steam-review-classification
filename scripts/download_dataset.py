import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET_NAME = "najzeko/steam-reviews-2021"
DESTINATION_FOLDER = "datasets"
RAW_FILE_NAME = "steam_reviews.csv"
FINAL_FILE_NAME = "steam_reviews_ptbr_top_game.csv"

def download_dataset():
    print(f"[1/4] Iniciando download do dataset: {DATASET_NAME}...")
    api = KaggleApi()
    api.authenticate()
    
    # Download e unzip automático
    api.dataset_download_files(DATASET_NAME, path=DESTINATION_FOLDER, unzip=True)
    print("[1/4] Download concluído!")

def process_and_filter():
    raw_path = os.path.join(DESTINATION_FOLDER, RAW_FILE_NAME)
    final_path = os.path.join(DESTINATION_FOLDER, FINAL_FILE_NAME)
    
    if not os.path.exists(raw_path):
        print(f"Erro: Arquivo {raw_path} não encontrado após o download.")
        return

    print("[2/4] Filtrando apenas as reviews em Português...")
    
    # Processamento em chunks (pedaços) para não estourar a memória (o dataset tem 21M de linhas)
    chunk_size = 500000
    ptbr_reviews = []
    
    # O dataset najzeko/steam-reviews-2021 tem a coluna 'language' e 'app_name' (ou 'app_id')
    for chunk in pd.read_csv(raw_path, chunksize=chunk_size, low_memory=False):
        # Filtra pelo idioma português (pode estar como 'portuguese' ou 'pt-br', geralmente 'portuguese')
        chunk_ptbr = chunk[chunk['language'].str.lower() == 'portuguese']
        ptbr_reviews.append(chunk_ptbr)
        
    df_ptbr = pd.concat(ptbr_reviews, ignore_index=True)
    print(f"[2/4] Encontradas {len(df_ptbr)} reviews em Português no total.")

    print("[3/4] Identificando o jogo com a maior quantidade de reviews em Português...")
    # Agrupa pelo nome do jogo e conta as reviews
    top_game = df_ptbr['app_name'].value_counts().idxmax()
    top_game_reviews_count = df_ptbr['app_name'].value_counts().max()
    
    print(f"[3/4] O jogo mais avaliado em PT-BR é: '{top_game}' com {top_game_reviews_count} reviews!")

    print(f"[4/4] Gerando dataset final apenas para o jogo: {top_game}...")
    df_top_game = df_ptbr[df_ptbr['app_name'] == top_game]
    
    # Salva o arquivo CSV apenas com as avaliações desse jogo
    df_top_game.to_csv(final_path, index=False)
    print(f"[4/4] Dataset final salvo em: {final_path}")
    
    # Opcional: deletar o CSV massivo cru para liberar espaço
    # os.remove(raw_path)

if __name__ == "__main__":
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)
    
    # Se o arquivo RAW já existir, pula o download (útil para testes locais)
    if not os.path.exists(os.path.join(DESTINATION_FOLDER, RAW_FILE_NAME)):
        download_dataset()
    else:
        print("[1/4] O arquivo bruto já existe, pulando download...")
        
    process_and_filter()
