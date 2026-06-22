from backend.graph.builder import build_tripartite_graph, mock_documents, mock_seed_groups
from backend.propagation.label_propagation import classify_reviews, label_propagation


REALTIME_REVIEW_LABEL = "INPUT_REVIEW"


def _find_classification(classifications, review_label):
    for item in classifications:
        if item[0] == review_label:
            return item
    return None


def _find_token(tokens, target):
    for token in tokens:
        if token == target:
            return True
    return False


def _merge_tokens(primary_tokens, extra_tokens):
    merged = []

    for token in primary_tokens:
        if not _find_token(merged, token):
            merged.append(token)

    for token in extra_tokens:
        if not _find_token(merged, token):
            merged.append(token)

    return merged


def _simple_review_tokens(text):
    normalized = ""
    for char in text.lower():
        if char.isalnum():
            normalized += char
        else:
            normalized += " "

    tokens = []
    for token in normalized.split():
        if len(token) > 1 and not _find_token(tokens, token):
            tokens.append(token)
    return tokens


def _nlp_review_tokens(text):
    try:
        from backend.preprocessing.nlp import clean_text
    except ModuleNotFoundError:
        return []

    return clean_text(text)


def _response_from_classification(classification, tokens):
    review_label, category, score, category_scores, top_words = classification
    return {
        "review": review_label,
        "category": category,
        "score": score,
        "tokens": tokens,
        "top_words": [{"word": w, "influence": round(inf, 6)} for w, inf in top_words],
        "scores": [
            {"category": score_label, "score": score_value}
            for score_label, score_value in category_scores
        ],
    }


def classify_review_text(text, tf_idf_threshold=0.0, pmi_threshold=0.0, damping_factor=0.85):
    """
    Classifica uma review digitada em tempo real.
    """
    nlp_tokens = _nlp_review_tokens(text)
    simple_tokens = _simple_review_tokens(text)
    tokens = _merge_tokens(nlp_tokens, simple_tokens)

    if len(tokens) == 0:
        return None

    # Mapeamento reverso para não mostrar palavras feias (stems) no Frontend
    stem_map = {}
    import re
    raw_words = re.findall(r'[a-z0-9áéíóúâêîôûãõç]+', text.lower())
    try:
        from nltk.stem import RSLPStemmer
        stemmer = RSLPStemmer()
        for w in raw_words:
            if len(w) > 1:
                st = stemmer.stem(w)
                if st not in stem_map or len(w) < len(stem_map[st]):
                    stem_map[st] = w
    except:
        pass

    documents = mock_documents() + [(REALTIME_REVIEW_LABEL, tokens)]
    graph = build_tripartite_graph(documents, mock_seed_groups(), tf_idf_threshold=tf_idf_threshold, pmi_threshold=pmi_threshold)
    scores = label_propagation(graph, iterations=30, threshold=0.0001, damping_factor=damping_factor)
    classifications = classify_reviews(graph, scores)
    classification = _find_classification(classifications, REALTIME_REVIEW_LABEL)

    if classification is None:
        return None

    review_label, category, score, category_scores, top_words = classification
    mapped_top_words = []
    for w, inf in top_words:
        mapped_top_words.append((stem_map.get(w, w), inf))
        
    mapped_classification = (review_label, category, score, category_scores, mapped_top_words)

    return _response_from_classification(mapped_classification, tokens)
