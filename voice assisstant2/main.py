import webbrowser
import urllib.parse
from ai.tool_llm import decide_tool
from core.tool_executor import execute_tool
from utils.tts import speak

# 🔥 LOCAL SYSTEM COMMANDS
from tools.system_tools import get_time, get_battery

# 🎵 MUSIC
from skills.music import play_music


# 📞 WHATSAPP
from skills.whatsapp import call_whatsapp

# 🔊 VOLUME
from skills.volume import (
    increase_volume,
    decrease_volume,
    mute_system,
    unmute_system
)

def handle_command_from_tray(command: str):
    try:
        command = command.lower().strip()
        if not command:
            return

        # =====================================================
        # 🔊 VOLUME CONTROLS (PRIORITY)
        # =====================================================
        if "unmute" in command:
            unmute_system()
            return

        if "mute" in command:
            mute_system()
            return

        if "volume up" in command or "increase volume" in command:
            increase_volume()
            return

        if "volume down" in command or "decrease volume" in command:
            decrease_volume()
            return

        

        # =====================================================
        # ⏰ TIME & BATTERY
        # =====================================================
        if "time" in command:
            from tools.system_tools import get_time
            response = get_time()
            speak(response)
            return

        if "battery" in command:
            speak(get_battery())
            return

        # =====================================================
        # 🎵 MUSIC
        # =====================================================
        if "play" in command:
           song = (
              command
              .replace("play", "")
              .replace("song", "")
              .replace("nova", "")
              .strip()
            )
           play_music(song)
           return



        # =====================================================
        # 🤖 AI FALLBACK
        # =====================================================
        # If no keywords match, then we use the LLM
        decision = decide_tool(command)

        if decision:
            print("AI decision:", decision)
            execute_tool(decision)
        else:
            speak("I didn't catch that. Could you repeat?")

    except Exception as e:
        print(f"Main Error: {e}")
        speak("I ran into a problem processing that command.")