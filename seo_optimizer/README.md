# AI SEO Optimizer

A Streamlit app that analyzes an article against a target keyword, calculates real SEO metrics, and uses Gemini to generate practical, explained suggestions for improvement.

## What it does

Paste in an article and a target keyword. The app calculates:
- **Keyword density** — how often the keyword appears relative to total word count
- **Word count**
- **Heading count** — counts Markdown-style (`#`) headings
- **Readability score** — using the Flesch Reading Ease formula

It then sends those calculated metrics, along with the full article, to Gemini, which returns clear, practical SEO suggestions with reasoning for each one.

## Tech stack

- **Streamlit** — UI and app framework
- **Gemini API** (`google-genai`) — generates qualitative SEO suggestions
- **textstat** — readability scoring (Flesch Reading Ease)

## How it's structured

This project combines two different approaches deliberately:
- **Deterministic Python logic** calculates the factual metrics (keyword count, word count, headings, readability) — exact, countable things an LLM shouldn't be trusted to "guess."
- **Gemini** is used only for the judgment layer — interpreting those numbers and the content to give human, explained suggestions, which is what LLMs are actually good at.

## Setup

1. Clone this repo and navigate to the `seo-optimizer` folder
2. Install dependencies:
pip install -r requirements.txt

3. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/)
4. Set your API key as an environment variable:

setx GOOGLE_API_KEY "your-key-here"

5. Run the app:

streamlit run app.py


## Known limitations

- Heading detection only recognizes Markdown-style `#` headings — content pasted from Word/Google Docs/plain writing (which typically uses bold text instead of `#` symbols) won't be detected as headings unless manually reformatted.
- Keyword matching is exact-text based — it won't catch variations in spacing, hyphenation, or phrasing.

## What I learned building this

- Combining deterministic logic with LLM-generated suggestions in a single tool, instead of relying on an LLM for everything
- Writing and debugging boolean conditions correctly (caught and fixed an inverted `or`/`not` condition)
- Understanding `st.session_state` as a general "don't rebuild expensive things on every rerun" pattern, not something tied specifically to chat history
- Building multi-line f-string prompts that combine labeled data with free-text content
- Integrating an external library (`textstat`) instead of reinventing a hard sub-problem (syllable counting) from scratch