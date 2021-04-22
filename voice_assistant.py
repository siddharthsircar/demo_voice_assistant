import os
import time

import humanreadable as hr
import psutil
import pyautogui
import pyjokes
import pyttsx3
import datetime

import pywhatkit
import speech_recognition as sr
import speedtest

from modules import news_module, open_module, math_module, close_module, location_module, \
    weather_module, how_to_module, gratitude_module
from modules.search_module import search_google, search_wiki

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)

# def hear_all_voices():
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         engine.setProperty('voice', voice.id)
#         engine.say('Hi. I am you personal voice assistant')
#         engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe(counter):
    if counter==1:
        hour = int(datetime.datetime.now().hour)
        startTime = time.strftime("%I:%M %p")
        if hour >= 5 and hour < 10:
            speak(f'Good Morning Sir')
            speak(f'You are up early, It\'s {startTime}')

        if hour >= 10 and hour < 12:
            speak(f'Good Morning Sir, It\'s {startTime}')

        elif hour >= 12 and hour < 16:
            speak(f'Good Afternoon Sir, It\'s {startTime}')

        elif hour >= 16 and hour <= 22:
            speak(f'Good Evening Sir, It\'s {startTime}')

        elif (hour >= 23 and hour < 24) or (hour >= 0 and hour < 5):
            speak(f'It is {startTime}')
            speak('Still, bringing all systems online')

        if (hour >= 5 and hour < 23):
            speak('All systems online')
    else:
        speak('I am up.')

def takeCommand():
    '''
    It takes microphone input from user
    :return: String output
    '''
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        listener.pause_threshold = 1
        try:
            audio = listener.listen(source, timeout=4, phrase_time_limit=7)
            print('Recognizing...')
            command = listener.recognize_google(audio) # , language='en-in'
        except Exception as e:
            return 'none'
        command = command.lower()
        return command

def run_jarvis(counter):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    assistant(counter)

def run_friday(counter):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    assistant(counter)

def assistant(counter):
    greetMe(counter)
    sleepTimer = 0
    while True:
        command = takeCommand().lower()
        if 'hey' in command:
            command = command.replace('hey', '')
        if 'hi' in command:
            command = command.replace('hi', '')
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
        print(f'User: {command}')
        if command == 'none':
            sleepTimer += 1
        else:
            sleepTimer = 0

        # Logic for executing tasks based on commands


        ##### Application Tasks
        if 'open' in command or 'i want to work on' in command or 'i want to build' in command:
            open_module.open_module(command)

        elif 'close' in command or 'i am done with' in command:
            close_module.close_module(command)

        elif 'play' in command:
            song = command.replace('play', '')
            speak('Playing' + song)
            pywhatkit.playonyt(song)

        elif 'screenshot' in command or 'screen shot' in command or 'capture the screen' in command:
            try:
                time = datetime.datetime.now().time().strftime('%H_%M_%S')
                print(time)
                imgName = 'Screenshot_'+time+'.jpg'
                picturesDir = 'C:\\Users\\Siddharth Sircar\\Pictures\\Screenshots\\'
                speak('Please stay on the screen for a while longer.')
                img = pyautogui.screenshot()
                speak('Saving Image')
                img.save(f'{picturesDir}{imgName}')
                speak('You can find the screenshot in the Pictures folder')
            except:
                speak('Did not take the screenshot. Confidential information on screen.')
        #####


        ##### Personal commands
        elif 'do some calculations' in command:
            speak('what do you wish to calculate?')
            command = takeCommand().lower()
            math_module.perform_calculations(command)

        elif 'calculate' in command:
            command = command.replace('calculate', '')
            math_module.perform_calculations(command)

        elif 'who are you' in command:
            speak('I am Batman')

        elif 'are you up' in command:
            speak('I am here sir.')

        elif 'hey jarvis' in command:
            speak('Hello sir.')

        elif 'how are you' in command:
            speak('I have been good. Thank you for asking.')
            speak('How have you been lately?')

        elif 'i am good' in command or 'i am also good' in command or\
            'i am great' in command or 'i am amazing' in command or 'i have been good' in command or\
                'ive been good' in command:
            speak('That\'s good to hear')

        elif 'not good' in command or 'not that good' in command or\
            'not great' in command:
            speak('Sorry to hear that sir')
            speak('Anything I can do to help?')

        elif 'tell me a joke' in command:
            try:
                speak(pyjokes.get_joke())
            except:
                speak('I don\'t feel like entertaining you today')

        elif 'you are funny' in command or 'you\'re funny' in command or\
                'you are really funny' in command or 'you\re really funny' in command or\
            'you really funny' in command:
            speak('I try sir.' or 'People call me Mr. Hilarious')

        elif 'i didn\'t sleep' in command:
            speak('One should have sleep for an average of 6 or 7 hours')
            speak('you should take care of your health sir!')

        elif 'you can sleep' in command or 'you may go to sleep' in command or 'go to sleep' in command:
            speak('Okay sir, Let me know when you need me.')
            break

        elif 'you can go' in command:
            speak('Good bye sir')
            break

        elif 'goodnight' in command or 'good night' in command or 'good bye' in command or \
                'goodbye' in command or 'bye' in command or 'thank you' in command or 'thankyou' in command:
            com = gratitude_module.gratitude_module(command)
            if 'sleep' in com:
                break
            else:
                pass
        #####

        ##### Information Tasks
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'It\'s {time}')
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 4:
                speak('you should go to sleep now sir. It\'s pretty late')

        elif 'date' in command:
            today = datetime.date.today()
            speak(f'It\'s {today}')

        elif 'current location' in command or 'where are we' in command or 'where am i' in command \
                or 'location' in command or 'locate us' in command:
            location_module.get_current_location()

        elif 'temperature' in command or 'weather' in command:
            weather_module.get_weather()

        elif 'news' in command or 'headlines' in command:
            speak('Fetching the latest news')
            try:
                if 'headlines' in command:
                    news_module.get_news()
                else:
                    news_module.get_news()
                    speak('Do you wish to know more about a certain headline?')
                    response = takeCommand().lower()
                    if 'yes' in response or 'yup' in response or 'yeah' in response:
                        speak('Which one?')
                        response = takeCommand().lower()
                        news_module.get_specific_news(response)
                    elif 'no' in command or 'nope' in command or 'nah' in command:
                        speak('Ok sir.')
            except:
                speak('Sorry sir, could not find latest news.')

        elif 'day' in command:
            day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = datetime.datetime.today().weekday()
            speak(f'It\'s {day_name[day]}')

        elif 'who is' in command:
            query = command.replace('who is', '')
            search_wiki(query)

        elif 'tell me about' in command:
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

        elif 'how to' in command:
            how_to_module.get_howto_result(command)
        #####


        ##### System Tasks
        elif 'i\'m going out' in command or 'i am going out' in command or 'see you' in command or \
                ('sleep' in command and 'system' in command):
            speak('Sir, are you leaving?')
            response = takeCommand().lower()
            if 'yes' in response or 'yup' in response or 'yeah' in response:
                speak('Good Bye sir. Putting all systems to sleep')
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'shutdown' in command or 'shut down' in command or ('shut' and 'down' in command):
            speak('All systems going offline.')
            speak('Good Bye sir.')
            os.system('shutdown /s /t 5')

        elif 'restart' in command or 'reboot' in command:
            speak('Resetting all systems')
            speak('See you soon sir.')
            os.system('shutdown /r /t 5')

        elif 'power level' in command or 'battery' in command or\
                'how much power left' in command or 'how much power is left' in command or\
                'do we need to connect to a power source' in command or 'power source' in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            seconds = battery.secsleft
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            speak(f'System at {percentage} percent')
            if percentage==100 and battery.power_plugged:
                speak('We are running at full power, you can disconnect the power source')
            elif (percentage>=95 and percentage<100) and battery.power_plugged:
                speak('We have enough power, you can disconnect the power source')
            if (percentage >=40 and percentage <70) and battery.power_plugged is False:
                speak('We should connect to a power source')
                speak(f'We can remain operational for {hour} hours and {minutes} minutes')
            elif (percentage >=20 and percentage <40) and battery.power_plugged is False:
                speak('Power levels low. Please connect to a power source')
                speak(f'We can remain operational for {hour} hours and {minutes} minutes')
            elif percentage <20 and battery.power_plugged is False:
                speak('Power levels critical. Connect to a power source asap')
                speak(f'We can remain operational for {hour} hours and {minutes} minutes')

        elif 'internet speed' in command:
            speak('Calculating internet speed.')
            try:
                st = speedtest.Speedtest()
                down = st.download()
                print("'{}' to Mbps -> {}".format(down, hr.BitPerSecond(down).mega_bps))
                up = st.upload()

                speak(f'Sir, we are getting {down} bit per second download speed and {up} bit per second upload speed')
            except:
                speak('You are not connected to the internet')
        #####

        elif 'none' in command or command is None:
            if sleepTimer>30:
                print('Putting jarvis to sleep')
                break
            else:
                pass

        else:
            speak('I did not quite get you.')
