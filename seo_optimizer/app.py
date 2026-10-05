import os #noqa
import streamlit as st
import textstat
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="SEO Optimizer" , page_icon="📈")
st.title("AI SEO Optimizer")
st.caption("Smart SEO, faster rankings: Let AI handle the algorithm while you capture the traffic.")

if "Client" not in st.session_state:
    st.session_state.Client = genai.Client(api_key=api_key)

keyword_input = st.text_input("Enter the keyword you want to rank for").lower()
article_input = st.text_area("Paste your article or content here").lower()
st.caption("For accurate heading detection, format headings with # symbols (e.g., # Main Title, ## Subheading)")
generate_clicked = st.button("Analyze")

if generate_clicked: #noqa
    if not keyword_input or not article_input:
        st.warning("Please enter input first")

    else:
        with st.spinner("Analyzing..."):    

            try:
                total_keywords = article_input.count(keyword_input)
                total_words = len(article_input.split())
                lines = article_input.split("\n")
                
                keyword_density = (total_keywords/total_words)*100

                headings = 0

                for line in lines:
                    if line .startswith("#"):
                        headings += 1

                readability = textstat.flesch_reading_ease(article_input)   

                
                st.metric("Keyword Density" , f"{keyword_density:.2f}%")
                st.metric("Word Count" ,f"{total_words}" )
                st.metric("Headings" , f"{headings}")
                st.metric("Readability" , f"{readability:.2f}")


                prompt = f"""
                        You are an SEO expert. Based on the article, target keyword, and the calculated metrics below, give clear, practical suggestions for improving this content's SEO. 
                        Explain why each suggestion matters.
                
                        Target keyword: {keyword_input}
                        Word count: {total_words}
                        Keyword density: {keyword_density:.2f}%
                        Heading count: {headings}
                        Readability score: {readability:.2f}
                
                        Article:
                        {article_input}
                         """
                
                response = st.session_state.Client.models.generate_content(
                                model = "gemini-3.8-flash",
                                contents = prompt,
                                )
                
                st.write(response.text)


            except Exception as e:
                st.error(f"Something went wrong: {e}")    

        


