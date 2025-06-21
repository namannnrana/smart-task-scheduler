import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak now...")
        try:
            audio_text = r.listen(source, timeout=3, phrase_time_limit=5)
            result = r.recognize_google(audio_text)
            print("You said:", result)
            return result
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("API unavailable (check internet).")
