"""
Testes para o script de download e filtragem do dataset.
Usa um CSV fake pequeno para simular o comportamento sem precisar do Kaggle.
"""
import os
import sys
import pytest
import pandas as pd

# Adiciona o diretório raiz ao path para importar o script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from scripts.download_dataset import (
    filter_portuguese,
    select_top_game,
    MIN_REVIEW_LENGTH,
    DESTINATION_FOLDER,
)

FAKE_CSV_PATH = os.path.join(os.path.dirname(__file__), "fake_steam_reviews.csv")


@pytest.fixture(autouse=True)
def create_fake_csv():
    """Cria um CSV fake antes de cada teste e remove depois."""
    data = {
        "app_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "app_name": [
            "Counter-Strike", "Counter-Strike", "Counter-Strike",
            "Counter-Strike", "Counter-Strike",
            "Dota 2", "Dota 2",
            "GTA V", "GTA V", "GTA V",
        ],
        "review_id": list(range(100, 110)),
        "language": [
            "portuguese", "portuguese", "portuguese",
            "english", "portuguese",
            "portuguese", "portuguese",
            "portuguese", "portuguese", "english",
        ],
        "review": [
            "Jogo muito bom, gosto muito de jogar com meus amigos online",
            "Péssimo, muitos hackers estraga a diversão do jogo completamente",
            "Melhor FPS que já joguei na minha vida inteira sem sombra de dúvida",
            "Great game, love it so much, best FPS ever made in history",
            "Lag demais, servidor brasileiro sempre caindo sem parar nunca funciona",
            "Jogo complexo e estratégico, adoro jogar ranked com a galera",
            "Comunidade tóxica mas o jogo é bom vale a pena jogar bastante",
            "Gráficos incríveis, mundo aberto sensacional vale cada centavo pago",
            "a",       # Review muito curta, deve ser filtrada
            "Good game",  # Inglês, deve ser filtrada
        ],
        "voted_up": [True, False, True, True, False, True, False, True, True, True],
    }
    df = pd.DataFrame(data)
    df.to_csv(FAKE_CSV_PATH, index=False)

    yield

    if os.path.exists(FAKE_CSV_PATH):
        os.remove(FAKE_CSV_PATH)


def test_filter_portuguese_returns_only_portuguese():
    """Deve retornar apenas reviews com language == 'portuguese'."""
    df_ptbr, total = filter_portuguese(FAKE_CSV_PATH)

    assert df_ptbr is not None
    assert total == 10  # Total de linhas no CSV fake

    # Todas as reviews retornadas devem ser em português
    languages = df_ptbr['language'].str.lower().unique().tolist()
    assert languages == ['portuguese']


def test_filter_portuguese_removes_short_reviews():
    """Deve descartar reviews com menos de MIN_REVIEW_LENGTH caracteres."""
    df_ptbr, _ = filter_portuguese(FAKE_CSV_PATH)

    for review_text in df_ptbr['review'].tolist():
        assert len(review_text) >= MIN_REVIEW_LENGTH


def test_filter_portuguese_count():
    """
    Das 10 linhas: 8 são português, mas 1 delas ('a') é muito curta.
    Resultado esperado: 7 reviews.
    """
    df_ptbr, _ = filter_portuguese(FAKE_CSV_PATH)
    assert len(df_ptbr) == 7


def test_select_top_game_picks_most_reviewed():
    """Deve selecionar Counter-Strike (4 reviews válidas em PT-BR)."""
    df_ptbr, _ = filter_portuguese(FAKE_CSV_PATH)
    df_top, top_game, top_count, top_10 = select_top_game(df_ptbr)

    assert top_game == "Counter-Strike"
    assert top_count == 4
    assert len(df_top) == 4


def test_select_top_game_ranking_order():
    """O ranking deve estar em ordem decrescente."""
    df_ptbr, _ = filter_portuguese(FAKE_CSV_PATH)
    _, _, _, top_10 = select_top_game(df_ptbr)

    counts = list(top_10.values)
    assert counts == sorted(counts, reverse=True)
