import os

import pyjokes
import pyttsx3
import datetime

import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser

import gratitude_module
import open_module

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

    speak("All systems online.")

def takeCommand():
    '''
    It takes microphone input from user
    :return: String output
    '''
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.2)
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
    speak(f'Searching for {query}')
    pywhatkit.search(query)

def search_wiki(query):
    result = wikipedia.summary(query, sentences=1)
    speak(result)

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

    if 'wake up' in command or 'wakeup' in command:
        speak('Hello sir. I am online.')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'It is {time}')

    elif 'who is' in command:
        speak('Asking Wiki..')
        query = command.replace('who is', '')
        search_wiki(query)

    elif 'what is' in command:
        speak('Asking Wiki..')
        query = command.replace('what is', '')
        search_wiki(query)

    elif 'tell me about' in command:
        speak('Asking Wiki..')
        query = command.replace('tell me about', '')
        search_wiki(query)

    elif 'search google' in command:
        try:
            speak('What should I search for?')
            query = takeCommand()
            search_google(query)
        except:
            speak('Could you please repeat')
            query = takeCommand()
            search_google(query)

    elif 'run a search on' in command:
        try:
            query = command.replace('run a search on', '')
            search_google(query)
        except:
            speak('What should I search for?')
            query = takeCommand()
            search_google(query)

    elif 'open' in command or 'i want to work on' in command or 'i want to build' in command:
        open_module.open_module(command)

    elif 'play' in command:
        song = command.replace('play', '')
        speak('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'who are you' in command:
        speak('I am Batman')

    elif 'how are you' in command:
        speak('I have been good. Thank you for asking.')

    elif 'tell me a joke' in command:
        speak(pyjokes.get_joke())

    elif 'goodnight' in command or 'good night' in command or 'good bye' in command or \
            'goodbye' in command or 'bye' in command or 'thank you' in command or 'thankyou' in command:
        gratitude_module.gratitude_module(command)

    elif 'none' in command:
        pass

    else:
        speak('I did not quite get you.')

if __name__ == "__main__":
    greetMe()
    while True:
        run_jarvis()