import os
import webbrowser
import voice_assistant as assistant

def close_module(command):
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
