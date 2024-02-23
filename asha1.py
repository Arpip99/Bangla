import pygame
import time
from gtts import gTTS
import os

def speak_time_in_bangla(hour, minute):
    # Convert time to Bangla words
    hour_text = convert_to_bangla(hour)
    minute_text = convert_to_bangla(minute)
    
    # Convert time to Bangla string
    time_text = f"এখন সময় {hour_text} টা {minute_text} মিনিট"
    
    # Convert text to Bangla speech
    tts = gTTS(text=time_text, lang='bn')
    tts.save("time.mp3")
    
    # Play the time through speaker
    pygame.mixer.init()
    pygame.mixer.music.load("time.mp3")
    pygame.mixer.music.play()
    time.sleep(5)  # Wait for the speech to finish

def convert_to_bangla(num):
    # Convert numbers to Bangla words
    bangla_numbers = {
        0: 'শুন্য',
        1: 'এক',
        2: 'দুই',
        3: 'তিন',
        4: 'চার',
        5: 'পাঁচ',
        6: 'ছয়',
        7: 'সাত',
        8: 'আট',
        9: 'নয়',
        10: 'দশ',
        11: 'এগারো',
        12: 'বারো',
        13: 'তেরো',
        14: 'চৌদ্দ',
        15: 'পনেরো',
        16: 'ষোল',
        17: 'সতেরো',
        18: 'আঠারো',
        19: 'উনিশ',
        20: 'কুড়ি',
        21: 'একুশ',
        22: 'বাইশ',
        23: 'তেইশ',
        24: 'চুব্বিশ',
        25: 'পঁচিশ',
        26: 'ছাব্বিশ',
        27: 'সাতাশ',
        28: 'আটাশ',
        29: 'ঊনত্রিশ',
        30: 'ত্রিশ',
        31: 'একত্রিশ',
        32: 'বত্রিশ',
        33: 'তেত্রিশ',
        34: 'চৌত্রিশ',
        35: 'পঁয়ত্রিশ',
        36: 'ছত্রিশ',
        37: 'সাইত্রিশ',
        38: 'আটত্রিশ',
        39: 'ঊনচল্লিশ',
        40: 'চল্লিশ',
        41: 'একচল্লিশ',
        42: 'বিয়াল্লিশ',
        43: 'তেতাল্লিশ',
        44: 'চুরাল্লিশ',
        45: 'পঁয়তাল্লিশ',
        46: 'ছেচল্লিশ',
        47: 'সাতচল্লিশ',
        48: 'আটচল্লিশ',
        49: 'ঊনপঞ্চাশ',
        50: 'পঞ্চাশ',
        51: 'একান্ন',
        52: 'বায়ান্ন',
        53: 'তিপ্পান্ন',
        54: 'চুয়ান্ন',
        55: 'পঞ্চান্ন',
        56: 'ছাপ্পান্ন',
        57: 'সাতান্ন',
        58: 'আটান্ন',
        59: 'ঊনষাট'
    }
    if num <= 20:
        return bangla_numbers[num]
    elif num < 30:
        return f'একুশ {bangla_numbers[num - 20]}'
    else:
        tens = num // 10
        unit = num % 10
        return f'{bangla_numbers[tens]}শ {bangla_numbers[unit]}'

def main():
    while True:
        # Get current time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        # Check if minute is divisible by 5
        if minute % 5 == 0:
            speak_time_in_bangla(hour, minute)
        time.sleep(300)  # Wait for 5 minutes

if _name_ == "_main_":
    main()