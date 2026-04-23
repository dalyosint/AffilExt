import pandas as pd
import json
import re
import match_data

from approach1_spacy_ner import extract_org_name_with_spacy
from approach2_sbert import get_matched_affiliation_sbert

# =====================================================================
# SET YOUR THRESHOLD HERE
# =====================================================================
# Any match below this score will be rejected as "No Match"
CONFIDENCE_THRESHOLD = 75.0


def get_best_chunk_match(raw_string: str, ror_orgs: list):
    chunks = re.split(r'[,;]|\band\b', raw_string)
    chunks = [c.strip() for c in chunks if len(c.strip()) > 3]

    if not chunks:
        chunks = [raw_string]

    best_score = -1
    best_ror_id = None
    best_chunk_raw = ""
    best_chunk_spacy = ""

    for chunk in chunks:
        cleaned_chunk = extract_org_name_with_spacy(chunk)
        if not cleaned_chunk.strip():
            cleaned_chunk = chunk

        _, (ror_id, score) = get_matched_affiliation_sbert(cleaned_chunk, ror_orgs)

        if score > best_score:
            best_score = score
            best_ror_id = ror_id
            best_chunk_raw = chunk
            best_chunk_spacy = cleaned_chunk

    return best_chunk_raw, best_chunk_spacy, best_ror_id, best_score, chunks


# =====================================================================
# EVALUATION SCRIPT
# =====================================================================
if __name__ == "__main__":
    print("Loading ROR dataset for evaluation...")
    ror_dataset = match_data._get_ror_dataset()
    full_ror_orgs = match_data._process_ror_orgs(ror_dataset)

    df = pd.read_parquet('first_100_failed_matches.parquet')

    print(f"Evaluating Approach 4 with a Threshold of {CONFIDENCE_THRESHOLD}...")
    print("This may take a minute...\n")

    # Tracking Metrics
    total_evaluated = 0

    # Threshold Metrics
    confident_matches = 0
    rejected_matches = 0

    # Comparison Metrics
    improved_count = 0
    worsened_count = 0

    for index, row in df.iterrows():
        try:
            matched_info = json.loads(row['matched_info'])
            for author in matched_info.get('matched_authors', []):
                aff_matches = author.get('aff_matches', author.get('affiliations', []))

                for aff in aff_matches:
                    raw_string = aff.get('ext_name', '')
                    if not raw_string or '@' in raw_string:
                        continue

                    old_score = aff.get('score', 0.0)

                    # Get the new score
                    _, _, new_ror_id, new_score, _ = get_best_chunk_match(raw_string, full_ror_orgs)

                    total_evaluated += 1

                    # --- THRESHOLD LOGIC ---
                    if new_score >= CONFIDENCE_THRESHOLD:
                        confident_matches += 1
                    else:
                        rejected_matches += 1
                        # If we reject it, the effective score is 0 because we drop it
                        new_score = 0.0

                        # --- COMPARISON LOGIC ---
                    if new_score > (old_score + 0.1):
                        improved_count += 1
                    elif new_score < (old_score - 0.1):
                        worsened_count += 1

        except Exception as e:
            continue

    # --- PRINT FINAL EVALUATION REPORT ---
    print("=" * 60)
    print(" APPROACH 4: EVALUATION RESULTS ")
    print("=" * 60)
    print(f"Total Affiliations Evaluated:    {total_evaluated}")
    print(f"Confidence Threshold Set to:     {CONFIDENCE_THRESHOLD}")
    print("-" * 60)
    print(f"✅ Confident Matches (Passed):   {confident_matches} ({(confident_matches / total_evaluated) * 100:.1f}%)")
    print(f"❌ Rejected Matches (Failed):    {rejected_matches} ({(rejected_matches / total_evaluated) * 100:.1f}%)")
    print("-" * 60)
    print(f"📈 Better than old RapidFuzz:    {improved_count} ({(improved_count / total_evaluated) * 100:.1f}%)")
    print(f"📉 Worse than old RapidFuzz:     {worsened_count} ({(worsened_count / total_evaluated) * 100:.1f}%)")
    print("=" * 60)