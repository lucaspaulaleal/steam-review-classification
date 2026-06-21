# backend/preprocessing/nlp.py

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

# Variáveis globais para inicialização lazy (evita recarregar a cada linha processada)
_is_initialized = False
_stop_words = set()
_stemmer = None

def _initialize_nltk():
    """Baixa os recursos do NLTK apenas uma vez quando necessário."""
    global _is_initialized, _stop_words, _stemmer
    if _is_initialized:
        return

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
        
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab', quiet=True)

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

    try:
        nltk.data.find('stemmers/rslp')
    except LookupError:
        nltk.download('rslp', quiet=True)

    _stop_words = set(stopwords.words('portuguese'))
    # Adicionando termos comuns que podem ser ruido, ou que o RSLP pode ter problemas
    _stop_words.update(["é", "pra", "q", "ta", "pro", "tá", "aí", "ai"]) 
    
    _stemmer = RSLPStemmer()
    _is_initialized = True


def clean_text(text: str) -> list[str]:
    """
    Recebe um texto puro (review), limpa pontuações, converte para minúsculo,
    remove stop-words em português e extrai o radical das palavras (Stemming).
    Retorna uma lista de tokens.
    """
    if not isinstance(text, str) or not text.strip():
        return []

    _initialize_nltk()

    # 1. Lowercase e remoção de pontuação/números usando regex
    # Mantém apenas letras minúsculas (incluindo acentuadas).
    text = text.lower()
    text = re.sub(r'[^a-záéíóúâêîôûãõç]+', ' ', text)

    # 2. Tokenização
    tokens = word_tokenize(text, language='portuguese')

    # 3. Remoção de Stop-words e 4. Stemming (Lematização básica)
    processed_tokens = []
    for word in tokens:
        if word not in _stop_words and len(word) > 2:
            stemmed = _stemmer.stem(word)
            processed_tokens.append(stemmed)

    return processed_tokens

def clean_text_to_string(text: str) -> str:
    """
    Variante que retorna uma string separada por espaços,
    ideal para gravar no CSV diretamente.
    """
    return " ".join(clean_text(text))
