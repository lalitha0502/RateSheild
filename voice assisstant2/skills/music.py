import webbrowser
from utils.tts import speak

def play_music(song_name: str):
    if not song_name:
        speak("Please tell me which song you want to play")
        return

    speak(f"Playing {song_name}")
    webbrowser.open(
        f"https://open.spotify.com/search/{song_name.replace(' ', '%20')}"
    )
