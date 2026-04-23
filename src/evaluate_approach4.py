import pandas as pd
import json
import re
import match_data

# Import our tools
from approach1_spacy_ner import extract_org_name_with_spacy
from approach2_sbert import get_matched_affiliation_sbert


def get_best_chunk_match(raw_string: str, ror_orgs: list):
    """
    Chunking + spaCy + SBERT Hybrid logic.
    """
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
    ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

    # Load the failed matches
    df = pd.read_parquet('first_100_failed_matches.parquet')

    print("Evaluating Approach 4 (Chunking) against original RapidFuzz baseline...")
    print("This may take a minute...\n")

    # Tracking Metrics
    total_evaluated = 0
    improved_count = 0
    worsened_count = 0
    unchanged_count = 0

    old_score_total = 0.0
    new_score_total = 0.0

    for index, row in df.iterrows():
        try:
            matched_info = json.loads(row['matched_info'])
            for author in matched_info.get('matched_authors', []):

                # Handle different key names from older versions of the pipeline
                aff_matches = author.get('aff_matches', author.get('affiliations', []))

                for aff in aff_matches:
                    raw_string = aff.get('ext_name', '')
                    if not raw_string or '@' in raw_string:
                        continue

                    # --- GET OLD RAPIDFUZZ SCORE ---
                    old_score = aff.get('score', 0.0)

                    # --- GET NEW CHUNKING + SBERT SCORE ---
                    _, _, new_ror_id, new_score, _ = get_best_chunk_match(raw_string, full_ror_orgs)

                    # --- TRACK METRICS ---
                    total_evaluated += 1
                    old_score_total += old_score
                    new_score_total += new_score

                    # We consider a difference of < 0.1 to be essentially "No Change" due to floating point math
                    if new_score > (old_score + 0.1):
                        improved_count += 1
                    elif new_score < (old_score - 0.1):
                        worsened_count += 1
                    else:
                        unchanged_count += 1

        except Exception as e:
            continue

    # --- PRINT FINAL EVALUATION REPORT ---
    print("=" * 60)
    print(" APPROACH 4: EVALUATION RESULTS ")
    print("=" * 60)
    print(f"Total Affiliations Evaluated:  {total_evaluated}")
    print("-" * 60)
    print(f"✅ Improved Matches:           {improved_count} ({(improved_count / total_evaluated) * 100:.1f}%)")
    print(f"❌ Worsened Matches:           {worsened_count} ({(worsened_count / total_evaluated) * 100:.1f}%)")
    print(f"➖ Unchanged Matches:          {unchanged_count} ({(unchanged_count / total_evaluated) * 100:.1f}%)")
    print("-" * 60)
    print(f"Average Old Score (RapidFuzz): {old_score_total / total_evaluated:.2f}")
    print(f"Average New Score (Approach 4):{new_score_total / total_evaluated:.2f}")
    print("=" * 60)