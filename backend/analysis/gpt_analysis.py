import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def analyze_email_with_ai(email_text):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",  # Or try "mistralai/mixtral-8x7b"
                "messages": [
                    {"role": "system", "content": "You are a cybersecurity assistant. Analyze emails for phishing."},
                    {"role": "user", "content": email_text}
                ]
            }
        )
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error from AI: {e}"
