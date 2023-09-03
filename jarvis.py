import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning master!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon master!")
    else:
        speak('good evening master!')
    speak("i am GHOST . please tell me how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening---")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)

        print("say that again please: ")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('alimian2129@gmail.com','ali#4633$')
    server.sendmail('alimian2129@gmail.com',to,content)
    server.close()

if __name__=="main_":
    wishMe()
    if 1:
        query = takeCommand() .lower()
        if 'wikipedia' in query:
             speak('Searching wikipedia...')
             query= query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master the time is {strTime}")



        elif 'open pycharm' in query:
             codePath="C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.4\bin\pycharm64.exe"
             os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "alimian2129@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry the email has not sent!")