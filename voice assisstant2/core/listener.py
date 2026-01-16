from utils.speech import SpeechRecognizer
from utils.tts import speak

# Initialize once
speech = SpeechRecognizer(engine="google")

def listen():
    """
    Listens for user input and returns the text.
    """
    # Some speech engines need a tiny pause to reset the audio device
    command = speech.listen()
    
    if not command:
        return ""

    # Clean the command
    command = command.strip().lower()
    print("User:", command)
    
    return command