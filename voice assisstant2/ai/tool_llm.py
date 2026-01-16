import json
import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are a Windows voice assistant.

You MUST respond ONLY in valid JSON.
No explanations. No extra text.

JSON FORMAT:
{
  "tool": "<tool_name>",
  "args": { ... }
}

Available tools:
- open_app(app_name)
- search_web(query)
- type_text(text)
- press_key(key)
- get_time()
- get_battery()
- chat(response)

Rules:
- Open apps → open_app
- Search → search_web
- Time → get_time
- Battery → get_battery
- Otherwise → chat
"""



def decide_tool(command: str):
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
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": command}
                ]
            },
            timeout=20
        )

        data = response.json()

        # 🔴 HANDLE API ERRORS
        if "choices" not in data:
            print("OpenRouter error response:", data)
            return {
                "tool": "chat",
                "response": "I am having trouble connecting to my AI service."
            }

        content = data["choices"][0]["message"]["content"]

        # 🔴 HANDLE INVALID JSON FROM MODEL
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "tool": "chat",
                "response": content
            }

    except Exception as e:
        print("LLM Exception:", e)
        return {
            "tool": "chat",
            "response": "Something went wrong while contacting the AI."
        }
