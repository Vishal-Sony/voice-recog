# -*- coding: utf-8 -*-
import speech_recognition as sr

r=sr.Recognizer()

mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source,duration=1)
    print("Say your name:")
    audio1=r.listen(source,timeout=40)
    print("Say your UID:")
    audio2=r.listen(source,timeout=20)
    print("Thanks!")
    
try:
    print("Your name & UID is:"+r.recognize_google(audio1)+r.recognize_google(audio2));
except:
    print("Sorry! Unable to recognize.")
    pass;

