# core/tool_executor.py

from tools.system_tools import (
    open_app,
    search_web,
    type_text,
    press_key,
    get_time,
    get_battery
)
from utils.tts import speak


def execute_tool(decision: dict):
    """
    Executes the tool based on the decision dictionary
    and ensures Nova speaks the result.
    """

    if not decision:
        speak("I didn't understand that.")
        return

    tool = decision.get("tool", "")
    args = decision.get("args", {})
    response_text = None

    # =====================================================
    # 🚫 BLOCK MUSIC FROM AI COMPLETELY
    # =====================================================
    if tool in ("play_music", "music", "spotify"):
        speak("Please tell me the song name")
        return

    # =====================================================
    # ⏰ TIME
    # =====================================================
    if tool == "get_time":
        response_text = get_time()

    # =====================================================
    # 🔋 BATTERY
    # =====================================================
    elif tool == "get_battery":
        response_text = get_battery()

    # =====================================================
    # 📂 OPEN APPLICATION
    # =====================================================
    elif tool == "open_app":
        app_name = args.get("app_name")
        open_app(app_name)
        response_text = f"Opening {app_name}"

    # =====================================================
    # 🌐 SEARCH WEB (SAFE)
    # =====================================================
    elif tool == "search_web":
        query = args.get("query", "").lower()

        # 🚫 Block music-related searches
        if "spotify" in query or "play song" in query or query.startswith("play"):
            speak("Please tell me the song name")
            return

        search_web(query)
        response_text = f"Searching the web for {query}"

    # =====================================================
    # ⌨️ TYPE TEXT
    # =====================================================
    elif tool == "type_text":
        text_to_type = args.get("text")
        type_text(text_to_type)
        response_text = f"I have typed: {text_to_type}"

    # =====================================================
    # 🎛 PRESS KEY
    # =====================================================
    elif tool == "press_key":
        key = args.get("key")
        press_key(key)
        response_text = f"Pressed {key}"

    # =====================================================
    # 💬 CHAT RESPONSE
    # =====================================================
    elif tool == "chat":
        response_text = decision.get(
            "response", "I'm not sure how to respond to that."
        )

    # =====================================================
    # ❓ UNKNOWN TOOL
    # =====================================================
    else:
        response_text = "I'm sorry, I don't know how to do that yet."

    # =====================================================
    # 🔊 SPEAK RESPONSE (ONCE)
    # =====================================================
    if response_text:
        speak(response_text)
