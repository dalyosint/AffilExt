import pandas as pd
import json
from approach2_sbert import get_matched_affiliation_sbert

# Load the same 100 failed matches used for spaCy
df = pd.read_parquet('first_100_failed_matches.parquet')

# For this test, we use a small 'mock' ROR list to see if SBERT
# can find the needle in the haystack of a messy string.
mock_ror = [
    ("https://ror.org/0337v0011", "universitat de barcelona"),
    ("https://ror.org/00hj8s172", "columbia university"),
    ("https://ror.org/01aff2v68", "university of waterloo"),
    ("https://ror.org/0161v9041", "university of maryland")
]

print(f"Testing SBERT Semantic Matching on {len(df)} samples...")
print("-" * 80)

count = 0
for _, row in df.iterrows():
    matched_info = json.loads(row['matched_info'])
    for author in matched_info.get('matched_authors', []):
        for aff in author.get('affiliations', []):
            raw = aff.get('ext_name', '')
            if not raw or '@' in raw: continue

            # Run the SBERT match
            _, (ror_id, score) = get_matched_affiliation_sbert(raw, mock_ror)

            # Find the name for the ID to print it
            matched_name = next(name for tid, name in mock_ror if tid == ror_id)

            print(f"RAW:   {raw}")
            print(f"SBERT MATCH: {matched_name} (Score: {score:.4f})")
            print("-" * 80)

            count += 1
            if count >= 15: break
        if count >= 15: break
    if count >= 15: break