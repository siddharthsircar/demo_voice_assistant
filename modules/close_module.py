import os
import webbrowser
import voice_assistant as assistant

def close_module(command):
    # if 'close youtube' in command:
    #     jarvis.speak('opening youtube')
    #     webbrowser.open('www.youtube.com')
    #
    # elif 'close google' in command:
    #     jarvis.speak('opening google')
    #     try:
    #         jarvis.speak('What should I search for?')
    #         query = jarvis.takeCommand()
    #         if 'none' in query or query is None:
    #             webbrowser.open('www.google.com')
    #         elif query is not None:
    #             jarvis.search_google(query)
    #     except:
    #         webbrowser.open('www.google.com')
    #
    # elif 'close mail' in command:
    #     jarvis.speak('opening gmail')
    #     webbrowser.open('www.gmail.com')
    #
    # elif 'close whatsapp' in command:
    #     jarvis.speak('opening whatsapp')
    #     webbrowser.open('https://web.whatsapp.com/')
    #
    # elif 'close facebook' in command:
    #     jarvis.speak('opening facebook')
    #     webbrowser.open('www.facebook.com')
    #
    # elif 'close stackoverflow' in command or 'close stack overflow' in command:
    #     jarvis.speak('opening stackoverflow')
    #     webbrowser.open('www.stackoverflow.com')
    #
    # elif 'close prime video' in command or 'close primevideo' in command:
    #     jarvis.speak('opening prime video')
    #     webbrowser.open('www.primevideo.com')
    #
    # elif 'close netflix' in command:
    #     jarvis.speak('opening netflix')
    #     webbrowser.open('www.netflix.com')

    if 'explorer' in command:
        assistant.speak('Closing file explorer')
        os.system('taskkill /f /im explorer')

    elif 'close vs code' in command or 'flutter' in command:
        try:
            vsCodePath = 'S:\\Development\\Tools\\Microsoft VS Code\\Code.exe'
            assistant.speak('Closing VS Code')
            os.system(f'taskkill /f /im {vsCodePath}')
        except:
            assistant.speak('VS Code is not open')

    elif 'close android studio' in command or 'android' in command:
        try:
            studioPath = 'S:\\Development\\Tools\\Android Studio\\bin\\studio64.exe'
            assistant.speak('Closing Android Studio')
            os.system(f'taskkill /f /im {studioPath}')
        except:
            assistant.speak('Android studio is not open')

    elif 'close sublime' in command or 'close note pad' in command or 'close notepad' in command:
        try:
            sublimePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            assistant.speak('Opening Sublime Text editor')
            os.system(f'taskkill /f /im {sublimePath}')
        except:
            assistant.speak('Sublime text is not open')

    elif 'close python ide' in command or 'python' in command:
        try:
            pycharmPath = 'S:\\Development\\Tools\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe'
            assistant.speak('Closing PyCharm')
            os.system(f'taskkill /f /im {pycharmPath}')
        except:
            assistant.speak('PyCharm is not open')
