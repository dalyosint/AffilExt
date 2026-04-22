import pandas as pd
import json
from approach2_sbert import get_matched_affiliation_sbert

# IMPORT the functions needed to load the real ROR dataset
from match_data import _get_ror_dataset, _process_ror_orgs

# Load the same 100 failed matches used for spaCy
df = pd.read_parquet('first_100_failed_matches.parquet')

print("Loading full ROR dataset... (This might take a moment)")
# Load and process the FULL ROR dataset instead of the mock list
ror_dataset = _get_ror_dataset()
full_ror = _process_ror_orgs(ror_dataset)

print(f"Testing SBERT Semantic Matching on {len(df)} samples against {len(full_ror)} ROR institutions...")
print("-" * 80)

count = 0
for _, row in df.iterrows():
    matched_info = json.loads(row['matched_info'])
    for author in matched_info.get('matched_authors', []):
        for aff in author.get('affiliations', []):
            raw = aff.get('ext_name', '')
            if not raw or '@' in raw: continue

            # Run the SBERT match using the FULL dataset
            _, (ror_id, score) = get_matched_affiliation_sbert(raw, full_ror)

            # Find the name for the ID to print it (adding a default fallback just in case)
            matched_name = next((name for tid, name in full_ror if tid == ror_id), "Unknown")

            print(f"RAW:   {raw}")
            print(f"SBERT MATCH: {matched_name} (Score: {score:.4f})")

            # Optional: Flag strings that fall below the 40.0 noise threshold
            if score < 40.0:
                print("-> [FLAGGED AS NOISE/NON-INSTITUTION]")

            print("-" * 80)

            count += 1
            if count >= 15: break
        if count >= 15: break
    if count >= 15: break