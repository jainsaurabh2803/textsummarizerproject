# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello, this is a Python TTS demo on Mac.")
# engine.runAndWait()

import sounddevice as sd
import pyaudio
import speech_recognition as sr
print(pyaudio.__version__)

import os

text = "Hello, this is your Mac speaking!"
os.system(f'say "{text}"')


recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


