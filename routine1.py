from gtts import gTTS
import time
import os

# Function to convert time into Bangla text
def time_to_bangla(hour, minute):
    bangla_hour = str(hour)
    bangla_minute = str(minute).zfill(2)  # Add leading zero if minute is single digit

    meridiem = "পূর্বাহ্ণ" if hour < 12 else "অপরাহ্ণ"
    if hour > 12:
        bangla_hour = str(hour - 12)
    
    bangla_time = f'এখন সময় {bangla_hour}টা বেজে {bangla_minute} মিনিট {meridiem}'
    return bangla_time

# Function to declare routine based on time
def routine(hour, minute):
    routines = {
        (12, 10): "গোসল করো",
        (13, 10): "খাবার খাও",
        (13, 15): "নামাজ পড়ো",
        (13, 30): "বিশ্রাম নাও"
    }
    return routines.get((hour, minute), "")

# Main function
def main():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min

        # Speaking time every 3 minutes
        if minute % 3 == 0:
            bangla_time = time_to_bangla(hour, minute)
            tts = gTTS(bangla_time, lang='bn')
            tts.save("time.mp3")
            print(bangla_time)
            os.system("mpg321 time.mp3")  # Play the audio file

        # Declaring routine based on time
        routine_text = routine(hour, minute)
        if routine_text:
            tts = gTTS(routine_text, lang='bn')
            tts.save("routine.mp3")
            print(routine_text)
            os.system("mpg321 routine.mp3")  # Play the audio file

        time.sleep(60)  # Check time every minute

if _name_ == "_main_":
    main()