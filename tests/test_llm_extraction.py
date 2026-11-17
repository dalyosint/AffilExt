import asyncio
import json

import pytest

import llm_extraction


@pytest.mark.parametrize("name", list(llm_extraction.PROMPTS))
def test_prompts_render_without_placeholders(name):
    latex = r"\author{A. B.\thanks{Univ {X}}} $^{1}$"
    prompt = llm_extraction.build_prompt(llm_extraction.PROMPTS[name], latex)
    assert latex in prompt  # LaTeX braces survive untouched
    rest = prompt.replace(latex, "")
    assert "{schema}" not in rest and "{text_input}" not in rest and "{{" not in rest


@pytest.mark.parametrize("name", ["Constrained_Prompt", "Super_Prompt"])
def test_constrained_prompts_contain_the_json_schema(name):
    prompt = llm_extraction.build_prompt(llm_extraction.PROMPTS[name], "x")
    assert json.dumps(llm_extraction.ExtractionResponse.model_json_schema()) in prompt


@pytest.mark.parametrize("cut", [r"\begin{abstract}", r"\section{Intro}", r"\section*{Intro}", r"\chapter{One}"])
def test_window_head_stops_at_document_body(cut):
    doc = r"\documentclass{article}\author{Alice}" + "\n" + cut + "BODY " * 3000
    head = llm_extraction.get_latex_metadata_windows(doc).split("--- START OF DOCUMENT TAIL")[0]
    assert "Alice" in head
    assert "BODY" not in head


def test_window_keeps_tail_and_limits_head():
    doc = "x" * 50_000 + r"\address{Tail Univ}\end{document}"
    window = llm_extraction.get_latex_metadata_windows(doc, head_chars=100, tail_chars=40)
    head, tail = window.split("--- START OF DOCUMENT TAIL ---\n")
    assert head.count("x") == 100
    assert tail.endswith(r"\address{Tail Univ}\end{document}")


def test_query_ollama_times_out(monkeypatch):
    async def slow_chat(self, **kwargs):
        await asyncio.sleep(5)

    monkeypatch.setattr(llm_extraction.AsyncClient, "chat", slow_chat)
    with pytest.raises(asyncio.TimeoutError):
        llm_extraction.query_ollama("prompt", timeout_seconds=0.1)


def test_query_ollama_validates_response(monkeypatch):
    async def chat(self, **kwargs):
        return {"message": {"content": '{"authors": [{"name": "Alice", "affiliations": ["Oxford"]}]}'}}

    monkeypatch.setattr(llm_extraction.AsyncClient, "chat", chat)
    response = llm_extraction.query_ollama("prompt")
    assert response.authors[0].name == "Alice"
    assert response.authors[0].affiliations == ["Oxford"]
