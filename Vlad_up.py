import speech_recognition as sr
import webbrowser
import pyttsx3
import time

from CLI import dialogFlow_request
import os, subprocess

# Text To Speech

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[5].id)


CANCEL = ["cancel", "back", "stand by"]
TERMINATE = ["shut down", "terminate", "quit"]

r2 = sr.Recognizer()

def UP(cmd):
    print("I Think you said " + cmd)
    eng.say("I Think you said " + cmd)
    # eng.runAndWait()

    # cmd = cmd.lower()

    if cmd in CANCEL:
        return

    elif cmd in TERMINATE:
        terminate(eng)
        
    else:
        response = dialogFlow_request(cmd)
        print("I Think you said " + cmd)
        eng.say("I Think you said " + cmd)
            
