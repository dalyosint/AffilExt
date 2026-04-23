import pandas as pd
import json
from approach2_sbert import get_matched_affiliation_sbert
import match_data  # Import match_data to load the real ROR dataset

# Load the same 100 failed matches used for spaCy
df = pd.read_parquet('first_100_failed_matches.parquet')

print("Loading the full ROR dataset...")
# Retrieve the full ROR dataset and process it into the [(ror_id, name)] format SBERT expects
ror_dataset = match_data._get_ror_dataset()
full_ror_orgs = match_data._process_ror_orgs(ror_dataset)

print(f"Testing SBERT Semantic Matching on {len(df)} samples against full ROR dataset...")
print("-" * 80)

count = 0
for _, row in df.iterrows():
    matched_info = json.loads(row['matched_info'])
    for author in matched_info.get('matched_authors', []):
        for aff in author.get('affiliations', []):
            raw = aff.get('ext_name', '')
            if not raw or '@' in raw: continue

            # Run the SBERT match against the FULL list
            # Note: This will automatically load `ror_embeddings_cache.npz` via approach2_sbert.py
            _, (ror_id, score) = get_matched_affiliation_sbert(raw, full_ror_orgs)

            # Find the name for the matched ID to print it
            matched_name = next((name for tid, name in full_ror_orgs if tid == ror_id), "Unknown")

            print(f"RAW:   {raw}")
            print(f"SBERT MATCH: {matched_name} (Score: {score:.4f})")
            print("-" * 80)

            count += 1
            if count >= 15: break
        if count >= 15: break
    if count >= 15: break