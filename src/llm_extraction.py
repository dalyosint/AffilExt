"""Shared building blocks for LLM-based author/affiliation extraction:
response schema, prompts, LaTeX text windowing and the Ollama call.

Used by ai_fallback.py (pipeline) and experiments/experiment_llm.py.
"""
import asyncio
import json
import re

from ollama import AsyncClient
from pydantic import BaseModel


class AuthorModel(BaseModel):
    name: str
    affiliations: list[str]


class ExtractionResponse(BaseModel):
    authors: list[AuthorModel]


# Prompt templates are filled with str.format(): {schema} and {text_input} are placeholders,
# literal braces are written as {{ }}.
PROMPT_BASE = """Extract the authors and affiliations from this LaTeX text and return it as JSON.
{text_input}
"""

PROMPT_CONSTRAINED = """You are an academic data extraction AI.
Extract authors and affiliations from a LaTeX preamble.
Return JSON matching:
{schema}
Extraction Rules:
1. Strict Literal Extraction: Extract only author names and institutional affiliations explicitly present in the text.
2. Marker-Based Mapping: Utilize explicit textual markers (superscripts, asterisks, footnotes) or structural proximity to accurately map each author to their respective affiliations.
3. Exclude Metadata: Do not include email addresses, job titles, funding acknowledgments, or academic degrees in the author or affiliation fields.
4. Multiple Affiliations: If an author belongs to multiple institutions, list each explicitly linked affiliation in their array.
5. Orphaned Authors: If an author has no identifiable affiliation, return an empty array [] for that author. Zero inference is permitted.
6. Clean Strings: Remove all linking markers, footnote symbols, and LaTeX structural commands from the final output strings.


<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE>
"""

PROMPT_SUPER = r"""You are an expert academic data extraction AI. Extract authors and affiliations from a LaTeX preamble.
Return JSON matching:
{schema}
Extraction Rules:
1. Strict Literal Extraction: Extract only author names and institutional affiliations explicitly present in the text.
2. Marker-Based Mapping: Utilize explicit textual markers (superscripts, asterisks, footnotes) or structural proximity to accurately map each author to their respective affiliations.
3. Exclude Metadata: Do not include email addresses, job titles, funding acknowledgments, or academic degrees in the author or affiliation fields.
4. Multiple Affiliations: If an author belongs to multiple institutions, list each explicitly linked affiliation in their array.
5. Orphaned Authors: If an author has no identifiable affiliation, return an empty array [] for that author. Zero inference is permitted.
6. Clean Strings: Remove all linking markers, footnote symbols, and LaTeX structural commands from the final output strings.


EXAMPLE 1
Input:
\begin{{center}}
{{\large\textbf{{ON THE PSEUDOSPECTRUM OF ELLIPTIC QUADRATIC DIFFERENTIAL OPERATORS}}\\
\bigskip
\medskip
Karel \textsc{{Pravda-Starov}}\\
\bigskip
University of California, Berkeley}}
\end{{center}}

Output:
{{"authors":[
  {{"name":"Karel Pravda-Starov","affiliations":["University of California, Berkeley"]}}
]}}

EXAMPLE 2
Input:
\begin{{large}}
{{J. Harnad}}$^{{\dagger \ddagger}}$\footnote{{harnad@crm.umontreal.ca}}
and
{{A. Yu. Orlov}}$^{{\star}}$\footnote{{orlovs@wave.sio.rssi.ru}}
\end{{large}} \\
\bigskip
\begin{{small}}
$^{{\dagger}}$ {{\em Centre de recherches math\'ematiques, Universit\'e de Montr\'eal\\
C.~P.~6128, succ. centre ville, Montr\'eal, Qu\'ebec, Canada H3C 3J7}} \\
\smallskip
$^{{\ddagger}}$ {{\em Department of Mathematics and Statistics, Concordia University\\
7141 Sherbrooke W., Montr\'eal, Qu\'ebec, Canada H4B 1R6}} \\
\smallskip
$^{{\star}}$ {{\em Nonlinear Wave Processes Laboratory, \\
Oceanology Institute, 36 Nakhimovskii Prospect\\
Moscow 117997, Russia}} \\
\end{{small}}

Output:
{{"authors":[
  {{"name":"J. Harnad","affiliations":["Centre de recherches mathématiques, Université de Montréal, C. P. 6128, succ. centre ville, Montréal, Québec, Canada H3C 3J7","Department of Mathematics and Statistics, Concordia University, 7141 Sherbrooke W., Montréal, Québec, Canada H4B 1R6"]}},
  {{"name":"A. Yu. Orlov","affiliations":["Nonlinear Wave Processes Laboratory, Oceanology Institute, 36 Nakhimovskii Prospect, Moscow 117997, Russia"]}}
]}}

<LATEX_PREAMBLE>
{text_input}
</LATEX_PREAMBLE>
"""

PROMPTS = {
    "Base_Prompt": PROMPT_BASE,
    "Constrained_Prompt": PROMPT_CONSTRAINED,
    "Super_Prompt": PROMPT_SUPER,
}

DEFAULT_MODEL = "qwen2.5:0.5b"
DEFAULT_PROMPT = PROMPT_CONSTRAINED

_SCHEMA_JSON = json.dumps(ExtractionResponse.model_json_schema())


def build_prompt(template: str, text_input: str) -> str:
    """Fills a prompt template with the response JSON schema and the LaTeX text."""
    return template.format(schema=_SCHEMA_JSON, text_input=text_input)


# The author block ends where the document body starts
_HEAD_CUT_PATTERN = re.compile(r"\\begin\{abstract\}|\\abstract\{|\\section\*?\{|\\chapter\*?\{", re.IGNORECASE)

DEFAULT_HEAD_CHARS = 10000
DEFAULT_TAIL_CHARS = 2000


def get_latex_metadata_windows(text_content: str, head_chars: int = DEFAULT_HEAD_CHARS,
                               tail_chars: int = DEFAULT_TAIL_CHARS) -> str:
    """Cuts the LaTeX source down to the parts that contain author information.

    Head: everything before the abstract/first section (at most the last `head_chars` characters of it),
          which holds \\author, \\affiliation, \\maketitle blocks etc.
    Tail: the last `tail_chars` characters, which catches \\address{} blocks right before \\end{document}.
    """
    head_match = _HEAD_CUT_PATTERN.search(text_content)
    if head_match:
        head_text = text_content[:head_match.start()][-head_chars:]
    else:
        head_text = text_content[:head_chars]

    tail_text = text_content[-tail_chars:]

    return (
        "--- START OF DOCUMENT HEAD ---\n"
        f"{head_text}\n\n"
        "--- START OF DOCUMENT TAIL ---\n"
        f"{tail_text}"
    )


def query_ollama(prompt: str, model_name: str = DEFAULT_MODEL, temperature: float = 0.0,
                 timeout_seconds: float = 15) -> ExtractionResponse:
    """Sends the prompt to Ollama with the JSON schema enforced and returns the validated response.

    Raises:
        asyncio.TimeoutError: the model did not answer within timeout_seconds (the request is cancelled)
        pydantic.ValidationError: the answer does not match ExtractionResponse
        Exception: Ollama connection / API errors
    """
    async def _chat():
        return await AsyncClient().chat(
            model=model_name,
            messages=[{"role": "system", "content": prompt}],
            format=ExtractionResponse.model_json_schema(),
            options={"temperature": temperature, "top_p": 0.1 if temperature == 0.0 else 0.9},
        )

    response = asyncio.run(asyncio.wait_for(_chat(), timeout=timeout_seconds))
    return ExtractionResponse.model_validate_json(response["message"]["content"])
