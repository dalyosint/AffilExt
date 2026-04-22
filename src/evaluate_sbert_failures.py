import pandas as pd
import json

# Import the SBERT approach instead of NER
from approach2_sbert import get_matched_affiliation_sbert
import match_data

print("Loading ROR dataset... (This might take a moment to initialize SBERT)")
ror_dataset = match_data._get_ror_dataset()
ror_orgs = match_data._process_ror_orgs(ror_dataset)

# Load the 100 failed matches
df = pd.read_parquet('first_100_failed_matches.parquet')

SUCCESS_THRESHOLD = 70.0  # Define what score counts as a "fix"

stats = {
    "total_evaluated": 0,
    "rescued_by_sbert": 0,
    "regressions_made_worse": 0,
    "persistent_failures": 0,
    "flagged_as_noise": 0  # Tracks items below the 40.0 SBERT threshold
}

print("Evaluating 100 baseline failures against SBERT approach...\n")

for index, row in df.iterrows():
    try:
        matched_info_str = row['matched_info']
        if not matched_info_str: continue
        matched_info = json.loads(matched_info_str)

        for author in matched_info.get('matched_authors', []):
            for aff in author.get('affiliations', []):
                raw_string = aff.get('ext_name', '')
                baseline_score = aff.get('score', 0.0)  # The original failing RapidFuzz score

                # Basic cleaning: ignore empties or raw emails
                if not raw_string or '@' in raw_string: continue

                # Run the new SBERT approach
                _, (ror_id, sbert_score) = get_matched_affiliation_sbert(raw_string, ror_orgs)

                stats["total_evaluated"] += 1

                # Track if SBERT caught it as a "garbage" string (e.g. Grants)
                if sbert_score < 40.0:
                    stats["flagged_as_noise"] += 1

                # Categorize the result
                if sbert_score >= SUCCESS_THRESHOLD:
                    stats["rescued_by_sbert"] += 1
                elif sbert_score < baseline_score:
                    stats["regressions_made_worse"] += 1
                else:
                    stats["persistent_failures"] += 1

    except Exception as e:
        pass

print("=" * 60)
print("SBERT vs BASELINE: FINAL IMPACT REPORT")
print("=" * 60)
print(f"Total Affiliations Evaluated: {stats['total_evaluated']}")
print(f"🟢 Rescued by SBERT (Score >= {SUCCESS_THRESHOLD}): {stats['rescued_by_sbert']}")
print(f"🔴 Regressions (SBERT scored lower than baseline): {stats['regressions_made_worse']}")
print(f"🟡 Persistent Failures (Still failed): {stats['persistent_failures']}")
print("-" * 60)
print(f"🗑️ Flagged as Noise/Grants (Score < 40.0): {stats['flagged_as_noise']}")
print("=" * 60)

if stats['total_evaluated'] > 0:
    rescue_rate = (stats['rescued_by_sbert'] / stats['total_evaluated']) * 100
    print(f"CONCLUSION: The SBERT approach fixed {rescue_rate:.1f}% of the baseline failures.")
else:
    print("No affiliations were evaluated.")