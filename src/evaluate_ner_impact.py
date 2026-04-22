import pandas as pd
import json
from approach1_spacy_ner import get_matched_affiliation_spacy
import match_data

print("Loading ROR dataset...")
ror_dataset = match_data._get_ror_dataset()
ror_orgs = match_data._process_ror_orgs(ror_dataset)

# Load the 100 failed matches
df = pd.read_parquet('first_100_failed_matches.parquet')

SUCCESS_THRESHOLD = 50.0  # Define what score counts as a "fix"

stats = {
    "total_evaluated": 0,
    "rescued_by_ner": 0,
    "regressions_made_worse": 0,
    "persistent_failures": 0
}

print("Evaluating 100 baseline failures against NER approach...\n")

for index, row in df.iterrows():
    try:
        matched_info_str = row['matched_info']
        if not matched_info_str: continue
        matched_info = json.loads(matched_info_str)

        for author in matched_info.get('matched_authors', []):
            for aff in author.get('affiliations', []):
                raw_string = aff.get('ext_name', '')
                baseline_score = aff.get('score', 0.0)  # The original failing score

                if not raw_string: continue

                # Run the new NER approach
                _, (ror_id, ner_score) = get_matched_affiliation_spacy(raw_string, ror_orgs)

                stats["total_evaluated"] += 1

                # Categorize the result
                if ner_score >= SUCCESS_THRESHOLD:
                    stats["rescued_by_ner"] += 1
                elif ner_score < baseline_score:
                    stats["regressions_made_worse"] += 1
                else:
                    stats["persistent_failures"] += 1

    except Exception as e:
        pass

print("=" * 50)
print("NER vs BASELINE: FINAL IMPACT REPORT")
print("=" * 50)
print(f"Total Affiliations Evaluated: {stats['total_evaluated']}")
print(f"🟢 Rescued by NER (Score > {SUCCESS_THRESHOLD}): {stats['rescued_by_ner']}")
print(f"🔴 Regressions (NER scored lower than baseline): {stats['regressions_made_worse']}")
print(f"🟡 Persistent Failures (Still failed): {stats['persistent_failures']}")
print("=" * 50)

rescue_rate = (stats['rescued_by_ner'] / stats['total_evaluated']) * 100
print(f"CONCLUSION: The NER approach fixed {rescue_rate:.1f}% of the baseline failures.")