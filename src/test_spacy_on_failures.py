import pandas as pd
import json

# Import your matching tools
from approach1_spacy_ner import extract_org_name_with_spacy, get_matched_affiliation_spacy
import match_data

print("Loading ROR dataset for fuzzy matching...")
# Load ROR dataset and prepare it using the existing functions in match_data.py
ror_dataset = match_data._get_ror_dataset()
ror_orgs = match_data._process_ror_orgs(ror_dataset)
ror_orgs_dict = match_data._process_ror_orgs_to_dict(ror_dataset)

# Load the parquet file
df = pd.read_parquet('first_100_failed_matches.parquet')

print(f"Loaded {len(df)} failed matches. Testing spaCy NER + RapidFuzz...\n")
print("-" * 80)

count = 0
for index, row in df.iterrows():
    try:
        # The data is serialized as a JSON string in the 'matched_info' column
        matched_info_str = row['matched_info']
        if not matched_info_str:
            continue

        # Parse the JSON string into a Python dictionary
        matched_info = json.loads(matched_info_str)

        # Dig into the nested dictionaries to find the affiliations
        authors = matched_info.get('matched_authors', [])
        for author in authors:
            affiliations = author.get('affiliations', [])
            for aff in affiliations:
                # Get the raw string that RapidFuzz struggled with
                raw_string = aff.get('ext_name', '')

                if not raw_string:
                    continue

                # Get the cleaned string just to display it
                cleaned_string = extract_org_name_with_spacy(raw_string)

                # Run the full pipeline: NER cleaning -> RapidFuzz matching
                # Returns: (original_affiliation, (best_ror_id, score))
                _, (ror_id, score) = get_matched_affiliation_spacy(raw_string, ror_orgs)

                # Look up the matched ROR organization's actual name to display
                if ror_id in ror_orgs_dict and ror_orgs_dict[ror_id].names:
                    matched_org_name = ror_orgs_dict[ror_id].names[0]
                else:
                    matched_org_name = "Unknown"

                print(f"FAILED RAW:   {raw_string}")
                print(f"CLEANED:      {cleaned_string}")
                print(f"FUZZY MATCH:  {matched_org_name} (ROR ID: {ror_id})")
                print(f"MATCH SCORE:  {score:.2f}")
                print("-" * 80)

                count += 1
                if count >= 20:  # Limit to 20 for readability
                    break
            if count >= 20:
                break
    except Exception as e:
        print(f"Error parsing row {index}: {e}")

    if count >= 20:
        break

print("\n[Evaluation Complete]")
