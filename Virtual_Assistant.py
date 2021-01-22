import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from datetime import date


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I Am Your Assistant Sir. Please Tell Me How May I Help You")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sir Say That Again Please...")
        return "None"
    return  query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('kinza.fatima2511@yahoo.com', 'here my password')
        server.sendmail('kinza.fatima2511@yahoo.com', to, content)
        server.close()
if __name__ == "__main__":
    wishMe()
    while True:
            query = takecommand().lower()

            if 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open gamil' in query:
                webbrowser.open("gmail.com")
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

