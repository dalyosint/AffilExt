import logging
import ollama
from pydantic import BaseModel
from typing import List


from definition.data.Author import Author as AIExtAuthor

_logger = logging.getLogger(__name__)


# Pydantic Models
class AuthorModel(BaseModel):
    name: str
    affiliations: List[str]


class ExtractionResponse(BaseModel):
    authors: List[AuthorModel]


def extract_with_ollama(text_content: str, model_name: str = "llama3.2") -> List[AIExtAuthor]:
    """
    Sends text to Ollama and enforces a structured JSON response containing authors and affiliations.
    """
    _logger.info(" Extraction using Ollama")
    print(" test ")

    # setting a length limits
    text_input = text_content[:12000]

    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'system',
                    'content': (
                        "You are a precise data extraction assistant. "
                        "Extract all authors and their affiliations from the provided LaTeX text."

                    )
                },
                {
                    'role': 'user',
                    'content': text_input
                }
            ],
            #  super important
            format=ExtractionResponse.model_json_schema()
        )

        # The library returns the JSON content as a string in the message
        json_content = response['message']['content']

        # Parse it using Pydantic
        parsed_data = ExtractionResponse.model_validate_json(json_content)
        print("parse data ", parsed_data)
@
    except Exception as e: _logger.error(e)

text_content = "hello "
extract_with_ollama(text_content)