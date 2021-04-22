import os
import webbrowser
import voice_assistant as assistant

def open_module(command):
    if 'open youtube' in command:
        assistant.speak('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in command:
        assistant.speak('opening google')
        try:
            assistant.speak('What should I search for?')
            query = assistant.takeCommand()
            if 'none' in query or query is None:
                webbrowser.open('www.google.com')
            elif query is not None:
                assistant.search_google(query)
        except:
            webbrowser.open('www.google.com')

    elif 'open mail' in command:
        assistant.speak('opening gmail')
        webbrowser.open('www.gmail.com')

    elif 'open whatsapp' in command:
        assistant.speak('opening whatsapp')
        webbrowser.open('https://web.whatsapp.com/')

    elif 'open facebook' in command:
        assistant.speak('opening facebook')
        webbrowser.open('www.facebook.com')

    elif 'open stackoverflow' in command or 'open stack overflow' in command:
        assistant.speak('opening stackoverflow')
        webbrowser.open('www.stackoverflow.com')

    elif 'open prime video' in command or 'open primevideo' in command:
        assistant.speak('opening prime video')
        webbrowser.open('www.primevideo.com')

    elif 'open netflix' in command:
        assistant.speak('opening netflix')
        webbrowser.open('www.netflix.com')

    elif 'explorer' in command:
        assistant.speak('Opening file explorer')
        os.system('explorer')

    elif 'open vs code' in command or 'i want to work on flutter' in command:
        try:
            vsCodePath = 'S:\\Development\\Tools\\Microsoft VS Code\\Code.exe'
            assistant.speak('Opening VS Code')
            os.startfile(vsCodePath)
        except:
            assistant.speak('Could not find VS Code in given location')

    elif 'open android studio' in command or 'i want to build an android app' in command:
        try:
            studioPath = 'S:\\Development\\Tools\\Android Studio\\bin\\studio64.exe'
            assistant.speak('Opening Android Studio')
            os.startfile(studioPath)
        except:
            assistant.speak('Could not find Android Studio in given location')

    elif 'open sublime' in command or 'open note pad' in command or 'open notepad' in command:
        try:
            sublimePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            assistant.speak('Opening Sublime Text editor')
            os.startfile(sublimePath)
        except:
            assistant.speak('Could not find Sublime text in given location')

    elif 'open python ide' in command or 'i want to work on python' in command or 'python' in command:
        try:
            pycharmPath = 'S:\\Development\\Tools\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe'
            assistant.speak('Opening PyCharm')
            os.startfile(pycharmPath)
        except:
            assistant.speak('Could not find PyCharm in given location')
