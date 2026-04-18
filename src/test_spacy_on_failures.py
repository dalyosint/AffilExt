import pandas as pd
import json
from approach1_spacy_ner import extract_org_name_with_spacy

# Load the parquet file
df = pd.read_parquet('first_100_failed_matches.parquet')

print(f"Loaded {len(df)} failed matches. Testing spaCy NER cleaning...\n")
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

                # Run Approach 1!
                cleaned_string = extract_org_name_with_spacy(raw_string)

                print(f"FAILED RAW: {raw_string}")
                print(f"CLEANED:    {cleaned_string}")
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
print("Look at the CLEANED strings. Did spaCy successfully remove the street addresses and junk?")