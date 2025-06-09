import requests
import streamlit as st

def analyze_email_with_ai(body):
    try:
        headers = {
            "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a cybersecurity assistant. Assess this email for phishing risk."},
                {"role": "user", "content": body}
            ]
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res = response.json()

        if "choices" in res and len(res["choices"]) > 0:
            return res["choices"][0]["message"]["content"]
        else:
            return "⚠️ Error from AI: No choices returned in response."

    except Exception as e:
        return f"⚠️ Error from AI: {e}"

