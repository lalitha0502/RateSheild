import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, engine="google"):
        """
        engine: 'google' (online)
                'offline' (future: whisper / vosk)
        """
        self.engine = engine
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            if self.engine == "google":
                text = self.recognizer.recognize_google(audio)
            else:
                # Placeholder for offline engines
                raise NotImplementedError("Offline engine not implemented yet")

            return text.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError as e:
            print("Speech service error:", e)
            return ""
