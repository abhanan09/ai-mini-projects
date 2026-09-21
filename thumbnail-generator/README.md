# AI Thumbnail Generator

A simple Streamlit app that generates thumbnail images from a text prompt, using Hugging Face's Inference API (Stable Diffusion 3 Medium via the `hf-inference` provider).

## What it does

Enter a description of the thumbnail you want (e.g. *"bright colorful YouTube thumbnail for a video about learning Python"*), and the app generates an image based on that prompt.

## Tech stack

- **Streamlit** — UI and app framework
- **Hugging Face Inference API** (`huggingface_hub`) — image generation
- **Model:** `stabilityai/stable-diffusion-3-medium-diffusers`

## Setup

1. Clone this repo and navigate to the `thumbnail-generator` folder
2. Install dependencies:

pip install -r requirements.txt

3. Get a free Hugging Face account and access token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) — make sure to enable **"Make calls to Inference Providers"** permission on the token
4. Set your token as an environment variable:

setx HF_TOKEN "your-token-here"

5. Run the app:

streamlit run app.py


## Known limitations

- **Text rendering inside generated images is unreliable** — this is a common limitation of open-source image models compared to closed models like DALL-E 3. Prompts asking for legible text/titles inside the image may produce garbled results.
- Uses the free Hugging Face Inference tier, which has rate limits under heavy use.

## What I learned building this

- Working with a new type of API (image generation vs. text generation)
- Debugging real-world API integration issues: authentication, provider routing, token permission scopes, and deprecated model handling
- Streamlit UI patterns for single-shot generation (as opposed to conversational chat apps)