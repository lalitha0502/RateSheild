

import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt):
    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful desktop AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=15
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return "I had trouble connecting to the AI service."
