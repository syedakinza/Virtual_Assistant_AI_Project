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
        speak("Assalam-o-Alikum Sir. Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Assalam-o-Alikum Sir. Good Evening")
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
                speak("Okay Sir. Opening YouTube")
                webbrowser.open("youtube.com")
            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")
                speak("Okay Sir. Opening  WhatsApp")
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("Okay Sir. Opening Google.")
            elif 'open gamil' in query:
                speak("Okay Sir. Opening Gmail.")
                webbrowser.open("gmail.com")
            elif 'open facebook' in query:
                speak("Okay Sir. Opening Facebook.")
                webbrowser.open("facebook.com")

            elif 'play music' in query:
                speak("Okay Sir. Playing Songs. Enjoy the Songs.")
                music_dir = 'F:\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'tell me the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(strTime)
            elif 'tell me the date' in query:
                today = date.today()
                strdate = today.strftime("%D:%M:%Y")
                speak(f"Sir, the date is {strdate}")
                print(strdate)
            elif 'tell me the day' in query:
                now = datetime.datetime.now()
                strday= now.strftime("%A")
                speak(f"Sir, the day is {strday}")
                print(strday)

            elif 'open word' in query:
                speak("Okay Sir. Opening Word.")
                wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
                os.startfile(wordPath)
            elif 'open excel' in query:
                speak("Okay Sir. Opening Excel.")
                excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013"
                os.startfile(excelPath)
            elif 'open powerpoint' in query:
                speak("Okay Sir. Opening PowerPoint.")
                pptPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
                os.startfile(pptPath)
            elif 'open paint' in query:
                speak("Okay Sir. Opening Paint. Enjoy Painting.")
                paintPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint"
                os.startfile(paintPath)

            elif 'show weather' in query:
                speak("Okay Sir. Showing Weather.")
                webbrowser.open("accuweather.com")

            elif 'send email' in query:
                
                try:
                    speak("What should I say sir?")
                    content = takecommand()
                    to = "syedazehra4407@gmail.com"
                    speak("Okay Sir. Trying to send Email.")
                    sendEmail(to, content)
                    speak("Email has been sent to Zehra successfully!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am not able to send this email")
            elif 'thanks' in query:
                speak("Allah Hafiz. Have a nice day sir. See you soon")
                break
