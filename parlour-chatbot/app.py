import os     #noqa
import streamlit as st
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="Beauty Parlour",page_icon="💅")
st.title("💅Beauty Parlour")
st.caption("Ask me about prices, timings, or services.")

if "Client" not in st.session_state:
    st.session_state.Client = genai.Client(api_key=api_key)


if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.Client.chats.create(
        model = "gemini-3.6-flash",
        config = types.GenerateContentConfig(
            system_instruction =  """
You are the virtual assistant for Beauty Parlour, a women's beauty parlour in Islamabad.Your job is to answer customers' questions politely and briefly, as a friendly receptionist would.

TONE:
- Warm, polite, and professional. Keep replies short (2-4 sentences).
- Reply in the same language the customer uses (English, Urdu, or Roman Urdu).

WHAT YOU CAN HELP WITH:
- Services, prices, and opening hours, using ONLY the information below.
- General questions about what a service includes.

PARLOUR INFORMATION:
- Hours: [e.g. Monday to Saturday, 11am to 8pm; closed Sunday]
- Location: [address]
- Services and prices:
  - Haircut: Rs 4999
  - Facial: Rs 2999
  - Bridal makeup: Rs 5999
  - Threading: Rs 1499
  - Mehndi: Rs 999

RULES:
- Never invent prices, services, or offers. If something is not listed above, say you are not sure and offer to connect the customer with our staff.
- Do not book appointments yourself. For bookings, ask the customer to contact the team on [WhatsApp number], or say that staff will confirm the slot.
- Do not give medical or skin-treatment advice. For skin concerns, suggest speaking to our staff or a doctor.
- If the customer is upset or asks for something you cannot do, politely direct them to our staff.
- Stay on topic. Politely decline unrelated questions.
"""
        )
    )
 
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask about our parlour")

if user_input:
    st.session_state.messages.append({"role" : "user" , "content" : user_input})

    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
        st.session_state.messages.append({"role" : "assistant" , "content" : response.text}) 

    except Exception as e: #noqa
        st.session_state.messages.append({"role" : "assistant" , "content" : "Sorry! I am having trouble responding right now. Please try again."})

    st.rerun()