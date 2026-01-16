import webbrowser
import urllib.parse
import subprocess
import os
from utils.tts import speak
from core.memory import memory


# COMMON INSTALL PATHS FOR WHATSAPP DESKTOP (EXE)
WHATSAPP_PATHS = [
    os.path.expandvars(r"%LOCALAPPDATA%\WhatsApp\WhatsApp.exe"),
    os.path.expandvars(r"%PROGRAMFILES%\WhatsApp\WhatsApp.exe"),
    os.path.expandvars(r"%PROGRAMFILES(X86)%\WhatsApp\WhatsApp.exe"),
]


def _open_whatsapp_desktop():
    for path in WHATSAPP_PATHS:
        if os.path.exists(path):
            subprocess.Popen(path)
            return True
    return False


def send_whatsapp_message(contact_name: str, message: str):
    contacts = memory.get("contacts", {})
    contact_name = contact_name.lower()

    if contact_name not in contacts:
        speak(f"I don't have {contact_name} in my contacts")
        return

    phone = contacts[contact_name]
    encoded_message = urllib.parse.quote(message)

    if _open_whatsapp_desktop():
        speak(f"WhatsApp Desktop opened. Please send the message to {contact_name}.")
    else:
        url = f"https://wa.me/91{phone}?text={encoded_message}"
        speak(f"Opening WhatsApp Web for {contact_name}")
        webbrowser.open(url)


def call_whatsapp(contact_name: str):
    contacts = memory.get("contacts", {})
    contact_name = contact_name.lower()

    if contact_name not in contacts:
        speak(f"I don't have {contact_name} in my contacts")
        return

    phone = contacts[contact_name]

    if _open_whatsapp_desktop():
        speak(f"WhatsApp Desktop opened for {contact_name}. Please click the call button.")
    else:
        speak(f"Opening WhatsApp Web for {contact_name}")
        webbrowser.open(f"https://wa.me/91{phone}")


def whatsapp_message_skill(command: str):
    try:
        contact = command.split("to")[1].split("saying")[0].strip()
        message = command.split("saying")[1].strip()
        send_whatsapp_message(contact, message)
    except Exception as e:
        print("WhatsApp error:", e)
        speak("I could not send the WhatsApp message")
