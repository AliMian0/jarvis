import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour >= 12 and hour < 118:
        speak("good afternoon!")
    else:
        speak('good evening!')
    speak("i am jarvis sir. please tell me how may i help you?")


def takeCommand():
    r = sr.recognizer()
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



if __name__=="main_":
    wishMe()
    takeCommand()