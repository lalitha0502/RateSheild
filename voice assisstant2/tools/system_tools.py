import pyautogui
import time
import webbrowser
import subprocess
import datetime
import psutil
import ctypes
from utils.tts import speak

def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}"

def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        return f"Battery is at {battery.percent} percent"
    return "I couldn't read the battery status"

def open_app(app_name: str):
    name = app_name.lower().strip()
    system_apps = [
        "chrome", "msedge", "edge", "notepad",
        "calc", "calculator", "cmd", "powershell",
        "explorer", "control", "spotify", "word"
    ]

    if name in system_apps:
        subprocess.Popen(f"start {name}", shell=True)
        return f"Opening {app_name}"
    
    url = f"https://www.{name}.com"
    webbrowser.open(url)
    return f"Opening {app_name} in your browser"

def search_web(query: str):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching the web for {query}"

def type_text(text: str):
    time.sleep(1)
    pyautogui.write(text, interval=0.05)
    return f"I have typed: {text}"



# Virtual key codes
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF

def _send_key(vk):
    ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
    ctypes.windll.user32.keybd_event(vk, 0, 2, 0)

def press_key(key):
    if key == "volume_up":
        _send_key(VK_VOLUME_UP)
        speak("Increasing volume")

    elif key == "volume_down":
        _send_key(VK_VOLUME_DOWN)
        speak("Decreasing volume")

    elif key == "mute":
        _send_key(VK_VOLUME_MUTE)
        speak("System muted")
