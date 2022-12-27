import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#   this is used for speak the audio with the instances names call


if __name__ == "__main__":
  speak("who are u?")


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning,Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ,Sir")
    elif hour >= 16 and hour < 19:
        speak("Good Evening, Sir")
    else:
        speak("Good Night,Sir")

    speak("I am Jarvis, Please Give me Command Sir")


def takeCommand():
    # it take microphone input from the user and return the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... Sir  ")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return 'None'

        return query


if __name__ == "__main__":
    wish()
    # takeCommand()
    while True:
        query = takeCommand().lower()
        
        # logic for executing tasks based on query
        if "hello" in query:
            speak("hello sir, Namaste")

        elif "how are you" in query:
            speak("I'm fine sir, how can i help you ?")

        elif "who are you" in query:
            speak("Sir I am Jarvis personal assistant ")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("wikipedia says")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'play music' in query:
            music_dir = "D://songs"
            song = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, song[5]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\jarvis"
            os.startfile(codePath)

        elif 'jarvis quit' in query or 'exit' in query or 'close' in query or 'bye' in query:
            speak("Thanks you for using as an Assistant,Sir")
            exit()

        
           
