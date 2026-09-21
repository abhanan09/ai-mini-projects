import os #noqa

import streamlit as st
from huggingface_hub import InferenceClient 


hf_token = os.environ.get("HF_TOKEN") 

st.set_page_config(page_title ="Thumbnail Generator" , page_icon= "🖼️")
st.title("AI Thumbnail Generator")
st.caption("Turn a simple idea into a scroll-stopping thumbnail. ")

if "Client" not in st.session_state:
    st.session_state.Client = InferenceClient(
        provider="hf-inference",
        token=hf_token)  

user_input = st.text_input("Enter the prompt to generate thumbnails")
generate_clicked = st.button("Generate")  

if generate_clicked:  
    if not user_input:
        st.warning("Please enter the prompt first.")

    else:
        with st.spinner("Generating your thumbnail..."):
            try:
                image = st.session_state.Client.text_to_image(
                    prompt=user_input,
                    model="stabilityai/stable-diffusion-3-medium-diffusers"
                )
                st.image(image)

            except Exception as e: #noqa
                st.error(f"Something went wrong{e}")    
                

