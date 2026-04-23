import pandas as pd
import json
import re
import match_data

# Import our tools
from approach1_spacy_ner import extract_org_name_with_spacy
from approach2_sbert import get_matched_affiliation_sbert


def get_best_chunk_match(raw_string: str, ror_orgs: list):
    """
    Splits the string into chunks, processes each with spaCy and SBERT,
    and returns the best matching chunk ALONG WITH the list of generated chunks.
    """
    # Split the string by commas, semicolons, or the word "and"
    chunks = re.split(r'[,;]|\band\b', raw_string)

    # Clean up whitespace and drop tiny chunks (like "NY")
    chunks = [c.strip() for c in chunks if len(c.strip()) > 3]

    # Fallback just in case splitting destroyed the string
    if not chunks:
        chunks = [raw_string]

    best_score = -1
    best_ror_id = None
    best_chunk_raw = ""
    best_chunk_spacy = ""

    # Test every single chunk independently
    for chunk in chunks:
        # 1. Run spaCy on the isolated chunk
        cleaned_chunk = extract_org_name_with_spacy(chunk)
        if not cleaned_chunk.strip():
            cleaned_chunk = chunk  # fallback if spaCy strips everything

        # 2. Run SBERT on the spaCy-cleaned chunk
        _, (ror_id, score) = get_matched_affiliation_sbert(cleaned_chunk, ror_orgs)

        # 3. Keep the one that generates the highest confidence score
        if score > best_score:
            best_score = score
            best_ror_id = ror_id
            best_chunk_raw = chunk
            best_chunk_spacy = cleaned_chunk

    # --- NEW: We now return the 'chunks' list as the 5th variable ---
    return best_chunk_raw, best_chunk_spacy, best_ror_id, best_score, chunks


# =====================================================================
# RUN TEST
# =====================================================================
if __name__ == "__main__":
    df = pd.read_parquet('first_100_failed_matches.parquet')

    print("Loading the full ROR dataset...")
    ror_dataset = match_data._get_ror_dataset()
    full_ror_orgs = match_data._process_ror_orgs(ror_dataset)

    print(f"Testing APPROACH 4: CHUNKING + HYBRID PIPELINE...")
    print("-" * 80)

    count = 0
    for _, row in df.iterrows():
        matched_info = json.loads(row['matched_info'])
        for author in matched_info.get('matched_authors', []):
            for aff in author.get('affiliations', []):
                raw = aff.get('ext_name', '')
                if not raw or '@' in raw: continue

                # Run our new chunking function (now catching 5 variables)
                best_raw, best_spacy, ror_id, score, all_chunks = get_best_chunk_match(raw, full_ror_orgs)

                # Look up the name of the ROR ID we matched
                matched_name = next((name for tid, name in full_ror_orgs if tid == ror_id), "Unknown")

                print(f"1. RAW STRING:  {raw}")
                # --- NEW: Print the list of chunks ---
                print(f"2. CHUNKS MADE: {all_chunks}")
                print(f"3. BEST CHUNK:  {best_raw}")
                print(f"4. SPACY SAW:   {best_spacy}")
                print(f"5. SBERT MATCH: {matched_name}")
                print(f"   SCORE:       {score:.2f}")
                print("-" * 80)

                count += 1
                if count >= 15: break
            if count >= 15: break
        if count >= 15: break