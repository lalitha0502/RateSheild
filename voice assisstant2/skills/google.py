import webbrowser
from utils.tts import speak
from core.context_manager import context

def google_search_skill(command):
    query = command.replace("search", "").replace("google", "").strip()

    if not query:
        speak("What should I search on Google?")
        return

    context["last_search"] = query
    speak(f"Searching {query} on Google")
    webbrowser.open(f"https://www.google.com/search?q={query}")
