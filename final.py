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
        query = recognizer.recognize_google(audio, language='bn-BD')
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
    engine.setProperty('rate', 150)  # Adjusting speech rate (optional)
    engine.say(text)
    engine.runAndWait()

if _name_ == "_main_":
    while True:
        command = listen_microphone().lower()
        if "তোমার নাম কি" in command:
            speak("আমার নাম অপেক্ষা")
        elif "বাংলাদেশের জাতির জনকের নাম" in command:
            speak("বঙ্গবন্ধু শেখ মুজিবুর রহমান")
        elif "বাংলাদেশের প্রধান মন্ত্রীর নাম" in command:
            speak("শেখ হাসিনা")
        elif "বিদায়" in command or "খুদা হাফেজ" in command:
            speak("আবার দেখা হবে, ধন্যবাদ!")
 break