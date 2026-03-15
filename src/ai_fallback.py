import logging
import ollama
# new library

import re
from pydantic import BaseModel
from typing import List
from definition.data.Author import Author as AIExtAuthor
from definition.data.ExtAuthorData import ExtAuthorInfo, ExtResults

_logger = logging.getLogger(__name__)

# define the AuthorModel to pydantic
class AuthorModel(BaseModel):
    name: str
    affiliations: List[str]

# Validate AI output.
class ExtractionResponse(BaseModel):
    authors: List[AuthorModel]

def get_latex_preamble(text_content: str) -> str:
        """
        Extracts everything before \begin{document} or the main content.
        This guarantees we capture authors/affiliations without the massive paper body.
        """
        # Look for common start markers of the actual paper
        match = re.search(r'\\begin\{document\}|\\maketitle|\\begin\{abstract\}', text_content)

        if match:
            preamble = text_content[:match.start()]
            # Fallback to character limit if the preamble is inexplicably huge
            return preamble[:8000]

            # If no document start is found, fall back to character truncation
        return text_content[:8000]


# text_content: str =  input
# ExtAuthorInfo = output
def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = "llama3.2") -> ExtAuthorInfo:
    """
    Sends text to Ollama and enforces a structured JSON response.
    Returns an ExtAuthorInfo object to maintain compatibility with the pipeline.
    """
    _logger.info(f"AI Fallback extraction using Ollama for {arxiv_metadata.arxiv_id}")

    # Setting a length limit for the prompt ( authors are usually at the top )
    # where in latex files could find the part that we need ( it ques here try another method)
    text_input = get_latex_preamble(text_content)

    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'system',
                    'content': (
                        f"""You are a precise data extraction assistant.
        Your task is to extract all authors and their specific affiliations from the provided LaTeX text.

        You must return the data strictly adhering to the following JSON schema:
        {ExtractionResponse.model_json_schema()}  

        
        INPUT:
        \\author{{Alice Smith$^{{1,2}}$ and Bob Jones$^{{2}}$}}
        \\affiliation{{$^{{1}}$Department of Physics, MIT}}
        \\affiliation{{$^{{2}}$CERN, Geneva, Switzerland}}

        EXPECTED OUTPUT:
        {{
          "authors": [
            {{
              "name": "Alice Smith",
              "affiliations": [
                "Department of Physics, MIT", 
                "CERN, Geneva, Switzerland"
              ]
            }},
            {{
              "name": "Bob Jones",
              "affiliations": [
                "CERN, Geneva, Switzerland"
              ]
            }}
          ]
        }}
        

        Analyze the user's LaTeX input and respond ONLY with the valid JSON matching the schema. Do not include markdown blocks or conversational text.
        """

                    )
                },
                {
                    'role': 'user',
                    'content': text_input
                }
            ],
            # This forces AI to follow the  structure
            # add a temperature
            format=ExtractionResponse.model_json_schema(),
            # this force the model to be deterministic and not creative
            options = {
            "temperature": 0.0,
            "top_p": 0.1 }

        )

        # getting the AI response
        json_content = response['message']['content']
        # validate response ( valid or not )
        parsed_data = ExtractionResponse.model_validate_json(json_content)

        # Convert Pydantic models back to the project's Author objects
        authors = [AIExtAuthor(name=a.name, affiliations=a.affiliations) for a in parsed_data.authors]

        if authors:
            # We wrap it in ExtResults with a score of 1.0 (AI confidence) to match the pipeline's expected structure
            ext_results = [ExtResults(scheme_name="Ollama_AI_Fallback", authors=authors, score=1.0)]
            # return the final object
            return ExtAuthorInfo(ext_type="ai_fallback", extractions=ext_results)

    except Exception as e:
        _logger.error(f"Ollama extraction failed: {e}")

    return None


# resume logic because it will take 3.3 day to process the whole 12 GB , after 6 days
# smaller context windows
# less token pass it ( use the right tokenizer )
# Mistral
# manually inspect the sucess rate
# see the time for every row
# generate a new parquet file that see the average time
# try different prompt
# imaginary
