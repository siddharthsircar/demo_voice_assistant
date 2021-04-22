import os
import webbrowser
import jarvis_voice_assistant as jarvis

def open_module(command):
    if 'open youtube' in command:
        jarvis.speak('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in command:
        jarvis.speak('opening google')
        try:
            jarvis.speak('What should I search for?')
            query = jarvis.takeCommand()
            if 'none' in query or query is None:
                webbrowser.open('www.google.com')
            elif query is not None:
                jarvis.search_google(query)
        except:
            webbrowser.open('www.google.com')

    elif 'open mail' in command:
        jarvis.speak('opening gmail')
        webbrowser.open('www.gmail.com')

    elif 'open whatsapp' in command:
        jarvis.speak('opening whatsapp')
        webbrowser.open('https://web.whatsapp.com/')

    elif 'open facebook' in command:
        jarvis.speak('opening facebook')
        webbrowser.open('www.facebook.com')

    elif 'open stackoverflow' in command or 'open stack overflow' in command:
        jarvis.speak('opening stackoverflow')
        webbrowser.open('www.stackoverflow.com')

    elif 'open prime video' in command or 'open primevideo' in command:
        jarvis.speak('opening prime video')
        webbrowser.open('www.primevideo.com')

    elif 'open netflix' in command:
        jarvis.speak('opening netflix')
        webbrowser.open('www.netflix.com')

    elif 'explorer' in command:
        jarvis.speak('Opening file explorer')
        os.system('explorer')

    # elif 'camera' in command:
    #     try:
    #         cap = cv2.VideoCapture(0)
    #         while True:
    #             ret, img = cap.read()
    #             cv2.imshow('webcam', img)
    #             k = cv2.waitKey(50)
    #             if k==27:
    #                 break;
    #         cap.release()
    #         cv2.destroyAllWindows()

    elif 'open vs code' in command or 'i want to work on flutter' in command:
        try:
            vsCodePath = 'S:\\Development\\Tools\\Microsoft VS Code\\Code.exe'
            jarvis.speak('Opening VS Code')
            os.startfile(vsCodePath)
        except:
            jarvis.speak('Could not find VS Code in given location')

    elif 'open android studio' in command or 'i want to build an android app' in command:
        try:
            studioPath = 'S:\\Development\\Tools\\Android Studio\\bin\\studio64.exe'
            jarvis.speak('Opening Android Studio')
            os.startfile(studioPath)
        except:
            jarvis.speak('Could not find Android Studio in given location')

    elif 'open sublime' in command or 'open note pad' in command or 'open notepad' in command:
        try:
            sublimePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            jarvis.speak('Opening Sublime Text editor')
            os.startfile(sublimePath)
        except:
            jarvis.speak('Could not find Sublime text in given location')

    elif 'open python ide' in command or 'i want to work on python' in command or 'python' in command:
        try:
            pycharmPath = 'S:\\Development\\Tools\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe'
            jarvis.speak('Opening PyCharm')
            os.startfile(pycharmPath)
        except:
            jarvis.speak('Could not find PyCharm in given location')
