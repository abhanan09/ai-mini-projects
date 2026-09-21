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