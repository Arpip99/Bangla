import speech_recognition as sr
import pyttsx3

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusting for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Failed to request results. Please check your internet connection.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if _name_ == "_main_":
    while True:
        command = listen_microphone()
        if command == "hi":
            speak("Hello!")
        elif command == "exit":
            speak("Goodbye!")
        break
