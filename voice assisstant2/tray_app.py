import threading
import time
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

from utils.tts import speak
from core.listener import listen
from main import handle_command_from_tray

WAKE_WORD = "nova"
running = True
SLEEP_MODE = False


# ---------------- TRAY ICON ----------------
def create_icon():
    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, 56, 56), fill="white")
    draw.text((26, 18), "N", fill="black")
    return image


# ---------------- ASSISTANT LOOP ----------------
def assistant_loop():
    global running, SLEEP_MODE
    speak("Nova is running")

    while running:
        text = listen()
        time.sleep(0.3)
        if not text:
            continue

        text = text.lower().strip()
        print("Heard:", text)

        # 💤 SLEEP MODE (ONLY WAKE WORD WORKS)
        if SLEEP_MODE:
            if WAKE_WORD in text:
                SLEEP_MODE = False
                speak("I'm awake")
            continue

        # 😴 GO TO SLEEP
        if "go to sleep" in text or text == "sleep":
            SLEEP_MODE = True
            speak("Going to sleep")
            continue

        # 🎙 WAKE WORD COMMAND
        if text.startswith(WAKE_WORD):
            command = text.replace(WAKE_WORD, "", 1).strip()

            if not command:
                speak("Yes?")
                command = listen()
                if not command:
                    speak("I didn't catch that")
                    continue

            print("Executing command:", command)
            handle_command_from_tray(command)
            continue

        # ⚡ DIRECT COMMAND (NO WAKE WORD)
        handle_command_from_tray(text)

        time.sleep(0.2)


# ---------------- EXIT ----------------
def exit_app(icon, item):
    global running
    running = False
    speak("Goodbye")
    icon.stop()


# ---------------- MAIN ----------------
def main():
    icon = Icon(
        "Nova",
        create_icon(),
        "Nova Assistant",
        menu=Menu(
            MenuItem("Exit", exit_app)
        )
    )

    icon.run_detached()
    assistant_loop()


if __name__ == "__main__":
    main()
