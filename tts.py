# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello, this is a Python TTS demo on Mac.")
# engine.runAndWait()

import pandas as pd
import numpy as np
import sounddevice as sd
import speech_recognition as sr
import pyaudio
print(pyaudio.__version__)

import os

### Text-to-Speech Example
# text = "Hello, this is your Mac speaking!"
# os.system(f'say "{text}"')


# Speech Recognition Example    

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Say something...")
#     audio = recognizer.listen(source)

# try:
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio.")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

# Continuous Listening Example

def listen_forever():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening continuously. Press Ctrl+C to stop.")

        try:
            print("Say something...")
            while True:                
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                    print("You said:", text)
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

        except KeyboardInterrupt:
            print("\nStopped by user.")

if __name__ == "__main__":
    listen_forever()
   


