from mtranslate import translate
import googletrans
from googletrans import Translator
import speech_recognition as sr
import os
import pyttsx3

# ...

# Kullanıcının konuşmasını tanımak için tanıma motorunu başlat
r = sr.Recognizer()
translator = Translator()

engine = pyttsx3.init()



# Mikrofonu başlat
with sr.Microphone() as source:
    print("Sesli asistanınızı dinliyorum...")
    while True:
        
        try:
                # Kullanıcının konuşmasını dinle ve tanımayı gerçekleştir
            with sr.Microphone() as source:
                audio = r.listen(source)  # 5 saniyeye kadar dinleme yapacak

                # Ses algılandı, çeviri işlemini gerçekleştir
            text = r.recognize_google(audio, language='tr-TR')

            dt = translator.detect(text).lang

            print(dt)

            if dt == 'tr':
                os.system('cls')
                translated = translate(text, "en")
                print(translated)

                engine.say(translated)

                engine.runAndWait()

            else:
                os.system('cls')

        except sr.UnknownValueError:
            print("Anlaşılamadı")
            pass
        except sr.RequestError:
            print("Servise erişilemiyor")
            pass