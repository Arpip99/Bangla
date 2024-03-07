import pygame
import time
from gtts import gTTS

def say_time_in_bangla(hour, minute):
    bangla_numbers = ['এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগারো', 'বারো', 'তেরো', 'চোদ্দ', 'পনেরো', 'ষোলো', 'সতেরো', 'আঠারো', 'উনিশ', 'বিশ', 'একুশ', 'বাইশ', 'তেইশ', 'চব্বিশ', 'পঁচিশ', 'ছাব্বিশ', 'সাতাশ', 'আঠাশ', 'উনত্রিশ', 'ত্রিশ', 'একত্রিশ', 'বত্রিশ', 'তেত্রিশ', 'চুয়াল্লিশ', 'পঁয়তাল্লিশ', 'ছেঁয়াল্লিশ', 'সাততল্লিশ', 'আটতল্লিশ', 'উনচাল্লিশ', 'চাল্লিশ', 'একচাল্লিশ', 'বিয়াল্লিশ', 'তেতাল্লিশ', 'চুরাল্লিশ', 'পঁয়তাল্লিশ', 'ছেচাল্লিশ', 'সাতচাল্লিশ', 'আটচাল্লিশ', 'উনপঞ্চাশ', 'পঞ্চাশ', 'একান্ন', 'বাহান্ন', 'তিপ্পান্ন', 'চুয়ান্ন', 'পঁচান্ন', 'ছাপ্পান্ন', 'সাতান্ন', 'আটান্ন', 'উনষাট', 'ষাট', 'একষট্টি', 'বাষট্টি', 'তেষট্টি', 'চুয়াষট্টি', 'পঁয়ষট্টি', 'ছেষট্টি', 'সাতষট্টি', 'আটষট্টি', 'উনসত্তর', 'সত্তর', 'একাত্তর', 'বাহাত্তর', 'তিয়াত্তর', 'চুয়াত্তর', 'পঁচাত্তর', 'ছিয়াত্তর', 'সাতাত্তর', 'আটাত্তর', 'উনআশি', 'আশি']
    hour_str = bangla_numbers[hour % 12 - 1]
    minute_str = bangla_numbers[minute // 5]
    text = f"এখন সময় {hour_str}টা বেজে {minute_str}মিনিট"
    tts = gTTS(text=text, lang='bn')
    tts.save("time.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("time.mp3")
    pygame.mixer.music.play()
    # Wait for the audio to finish playing
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

while True:
    current_time = time.localtime()
    hour = current_time.tm_hour % 12 or 12  # Convert to 12-hour format
    minute = current_time.tm_min
    if minute % 5 == 0:
        say_time_in_bangla(hour, minute)
    time.sleep(60)  # Check every minute