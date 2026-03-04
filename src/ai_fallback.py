import logging
import ollama
# new library
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

# text_content: str =  input
# ExtAuthorInfo = output
def extract_with_ollama(text_content: str, arxiv_metadata, model_name: str = "gemma3:1b") -> ExtAuthorInfo:
    """
    Sends text to Ollama and enforces a structured JSON response.
    Returns an ExtAuthorInfo object to maintain compatibility with the pipeline.
    """
    _logger.info(f"AI Fallback extraction using Ollama for {arxiv_metadata.arxiv_id}")

    # Setting a length limit for the prompt ( authors are usually at the top )
    # where in latex files could find the part that we need ( it ques here try another method)
    text_input = text_content[:12000]

    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'system',
                    'content': (
                        # take a look Language Models are Few-Shot Learners
                        # example ( snippet ) and give also the output
                        # try different snippet
                        # feed mt pydantic model to the prompt
                        "You are a precise data extraction assistant. "
                        "Extract all authors and their affiliations from the provided LaTeX text. "
                        "Respond ONLY with the JSON format requested."
                    )
                },
                {
                    'role': 'user',
                    'content': text_input
                }
            ],
            # This forces AI to follow the  structure
            # add a temperature
            format=ExtractionResponse.model_json_schema()
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
# manually inspect the sucees rate
# see the time for every row
# generate a new new parquet file that see the average time
# try different prompt
# imaginary
