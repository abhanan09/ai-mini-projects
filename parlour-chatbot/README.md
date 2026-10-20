# Beauty Parlour Assistant

A Gemini-powered chatbot demo that answers a beauty parlour's common customer questions (services, prices, and timings) the way a friendly receptionist would.


## What it does

- Answers questions about services, prices, and opening hours
- Replies in the customer's language (English, Urdu, or Roman Urdu)
- Remembers the conversation, so follow-up questions work
- Sends booking requests to the parlour's staff instead of booking itself
- Declines medical advice and unrelated questions

## Built with

- Python
- Streamlit
- Google Gemini API (`google-genai` SDK)

## How it works

- The system instruction defines the bot's persona, the parlour's information, and its rules (never invent prices, send bookings to staff).
- `st.session_state` stores the API client, the chat session, and the message history so they survive Streamlit's reruns.

## Run it locally

1. Clone the repo and install dependencies:
```
   pip install -r requirements.txt
```
2. Set your Gemini API key as an environment variable named `GOOGLE_API_KEY`.
3. Start the app:
```
   streamlit run app.py
```

## Customizing for a business

Edit the system instruction in `app.py`: the business name, city, hours, services, prices, and contact number.

## Limitations

- Demo only: it does not manage a booking calendar
- Answers come only from the information in the system instruction

## Author

Abdul Hanan, building AI chatbots and automation tools for small businesses.