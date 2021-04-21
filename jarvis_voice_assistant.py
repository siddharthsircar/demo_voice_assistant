import os

import pyjokes
import pyttsx3
import datetime

import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am online")

def takeCommand():
    '''
    It takes microphone input from user
    :return: String output
    '''
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # listener.pause_threshold = 1
        audio = listener.listen(source)
        try:
            print('Recognizing...')
            command = listener.recognize_google(audio)
        except Exception as e:
            print(e)
            print('I did not get you!')
            return 'None'
        return command

def search_google(query):
    speak(f'Searching google for {query}')
    pywhatkit.search(query)

def run_jarvis():
    command = takeCommand().lower()
    if 'hey' in command:
        command = command.replace('hey', '')
    if 'hi' in command:
        command = command.replace('hi', '')
    if 'jarvis' in command:
        command = command.replace('jarvis', '')
    print(f'User: {command}')

    # Logic for executing tasks based on commands
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'It is {time}')

    elif 'who is' in command:
        speak('Asking Wiki..')
        query = command.replace('who is', '')
        result = wikipedia.summary(query, sentences=1)
        speak(result)

    elif 'what is' in command:
        speak('Asking Wiki..')
        query = command.replace('what is', '')
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif 'tell me about' in command:
        speak('Asking Wiki..')
        query = command.replace('tell me about', '')
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif 'search google' in command:
        try:
            speak('What should I search for?')
            query = takeCommand()
            search_google(query)
        except:
            speak('Could you please repeat')
            query = takeCommand()
            search_google(query)

    elif  'do a search on' in command:
        try:
            query = command.replace('do a search on', '')
            search_google(query)
        except:
            speak('What should I search for?')
            query = takeCommand()
            search_google(query)

    elif 'covid status in india' in command:
        pass

    elif 'open youtube' in command:
        speak('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in command:
        speak('opening google')
        webbrowser.open('www.google.com')

    elif 'open facebook' in command:
        speak('opening facebook')
        webbrowser.open('www.facebook.com')

    elif 'open stackoverflow' in command or 'open stack overflow' in command:
        speak('opening stackoverflow')
        webbrowser.open('www.stackoverflow.com')

    elif 'open prime video' in command or 'open primevideo' in command:
        speak('opening prime video')
        webbrowser.open('www.primevideo.com')

    elif 'open netflix' in command:
        speak('opening netflix')
        webbrowser.open('www.netflix.com')

    elif 'play' in command:
        song = command.replace('play', '')
        speak('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'open vs code' in command:
        try:
            vsCodePath = 'S:\\Development\\Tools\\Microsoft VS Code\\Code.exe'
            speak('Opening VS Code')
            os.startfile(vsCodePath)
        except:
            speak('Could not find VS Code in given location')

    elif 'open android studio' in command or 'i want to build an android app' in command:
        try:
            studioPath = 'S:\\Development\\Tools\\Android Studio\\bin\\studio64.exe'
            speak('Opening Android Studio')
            os.startfile(studioPath)
        except:
            speak('Could not find Android Studio in given location')

    elif 'open sublime' in command or 'open text editor' in command:
        try:
            sublimePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            speak('Opening Sublime Text editor')
            os.startfile(sublimePath)
        except:
            speak('Could not find Sublime text in given location')

    elif 'open python ide' in command or 'i want to work on python' in command or 'python' in command:
        try:
            pycharmPath = 'S:\\Development\\Tools\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe'
            speak('Opening PyCharm')
            os.startfile(pycharmPath)
        except:
            speak('Could not find PyCharm in given location')

    elif 'who are you' in command:
        speak('I am Batman')

    elif ('thank you' in command and 'goodnight' in command) or \
            ('thank you' in command and 'good night' in command) or \
            ('thankyou' in command and 'good night' in command) or \
            ('thankyou' in command and 'goodnight' in command):
        speak('Always at your service sir!')
        speak('Good Night!')
        exit()

    elif ('thank you' in command and 'bye bye' in command) or \
            ('thank you' in command and 'byebye' in command) or \
            ('thankyou' in command and 'bye bye' in command) or \
            ('thankyou' in command and 'byebye' in command):
        speak('Always at your service sir!')
        speak('Good Bye!')
        exit()

    elif ('thank you' in command and 'goodbye' in command) or \
            ('thank you' in command and 'good bye' in command) or \
            ('thankyou' in command and 'good bye' in command) or \
            ('thankyou' in command and 'goodbye' in command):
        speak('Always at your service sir!')
        speak('Good Bye!')
        exit()

    elif 'thank you' in command or 'thankyou' in command:
        speak('Always at your service sir!')

    elif 'how are you' in command:
        speak('I have been good. Thank you for asking.')

    elif 'tell me a joke' in command:
        speak(pyjokes.get_joke())

    elif 'goodbye' in command or 'good bye' in command:
        speak('Good bye sir!')
        exit()

    elif 'goodnight' in command or 'good night' in command:
        speak('Good night sir!')
        exit()

    elif 'none' in command:
        pass

    else:
        speak('I did not quite get you.')

if __name__ == "__main__":
    greetMe()
    while True:
        run_jarvis()