import speech_recognition as sr
from gtts import gTTS
import os
import time

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as source
    with sr.Microphone() as source:
        print("কি বলবেন?")
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        query = recognizer.recognize_google(audio, language='bn-BD')
        print("আপনি বলেছেন: " + query)
        return query
    except sr.UnknownValueError:
        print("আমি বুঝতে পারছি না")
        return ""
    except sr.RequestError:
        print("আমার সাথে কথা বলা সম্ভব হচ্ছে না")
        return ""

def speak_bangla(text):
    # Convert text to Bangla speech
    tts = gTTS(text=text, lang='bn')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

def get_current_time():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    return hour, minute

def main():
    last_announcement = -5
    while True:
        hour, minute = get_current_time()
        if minute % 5 == 0 and minute != last_announcement:
            speak_bangla(f"এখন সময় {hour} টা {minute} মিনিট")
            last_announcement = minute
        query = recognize_speech()
        if query:
            if "কেমন আছো?" in query:
                speak_bangla("ভালো আছি")
            elif "বাংলাদেশের জাতির জনকের নাম কি?" in query:
                speak_bangla("বঙ্গবন্ধু শেখ মুজিবুর রহমান")
            elif "তোমার নাম কি?" in query:
                speak_bangla("আমার নাম আশা")
                break

if _name_ == "_main_":
    main()