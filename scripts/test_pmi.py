import pandas as pd
df = pd.read_csv('datasets/steam_reviews_ptbr_top_game.csv').dropna(subset=['clean_tokens']).sample(n=500, random_state=42)
docs = list(zip(df['review_id'].astype(str), df['clean_tokens'].apply(lambda x: str(x).split())))

from backend.graph.pmi import calculate_pmi
pmi_edges = calculate_pmi(docs)

from backend.graph.builder import mock_seed_groups
seed_groups = mock_seed_groups()

counts = {cat: 0 for cat, _ in seed_groups}
cat_map = {s: cat for cat, seeds in seed_groups for s in seeds}

for a, b, w in pmi_edges:
    if a in cat_map:
        counts[cat_map[a]] += 1
    if b in cat_map:
        counts[cat_map[b]] += 1

print("PMI Edge Counts for Seed Words:")
print(counts)
