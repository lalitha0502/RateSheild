import pyttsx3
import threading

def speak(text: str):
    if not text:
        return
    print("Nova:", text)

    def _threaded_speak():
        # Re-initializing inside the thread for every call 
        # prevents the engine from locking up after an error.
        try:
            # Re-initialize to clear any previous 'busy' state
            engine = pyttsx3.init() 
            engine.setProperty("rate", 170)
            engine.say(text)
            engine.runAndWait()
            # Explicitly stop to release the driver
            engine.stop() 
        except Exception as e:
            print(f"TTS Thread Error: {e}")

    threading.Thread(target=_threaded_speak, daemon=True).start()