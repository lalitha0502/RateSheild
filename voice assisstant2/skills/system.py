import subprocess
import webbrowser
import shutil
from utils.tts import speak

KNOWN_APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "calculator": "calc",
    "whatsapp": r"C:\Users\Srilatha\AppData\Local\WhatsApp\WhatsApp.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
}

def open_app(app_name):
    app_name = app_name.lower().strip()

    
    if app_name in KNOWN_APPS:
        speak(f"Opening {app_name}")
        subprocess.Popen(KNOWN_APPS[app_name], shell=True)
        return

    
    try:
        speak(f"Trying to open {app_name}")
        subprocess.Popen(f"start {app_name}", shell=True)
        return
    except:
        pass

   
    exe = shutil.which(app_name)
    if exe:
        speak(f"Opening {app_name}")
        subprocess.Popen(exe)
        return

    speak(f"I couldn't find {app_name}, searching on Google")
    webbrowser.open(f"https://www.google.com/search?q={app_name}")
