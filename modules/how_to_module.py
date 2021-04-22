from pywikihow import search_wikihow
import jarvis_voice_assistant as jarvis

def get_howto_result(command):
    jarvis.speak(f'Searching database for {command}')
    try:
        max_results = 1
        how_to = search_wikihow(command, max_results)
        assert len(how_to) == 1
        how_to[0].print()
        jarvis.speak(how_to[0].summary)
        jarvis.speak('Anything else sir?')
        command = jarvis.takeCommand()
        if 'no' in command:
            jarvis.speak('Okay sir.')
        elif 'repeat' in command:
            jarvis.speak(how_to[0].summary)
        elif 'how to' in command:
            get_howto_result(command)
        elif 'yes' in command:
            jarvis.speak('What sir?')
            newcommand = jarvis.takeCommand()
            get_howto_result(newcommand)
    except:
        jarvis.speak(f'No information on {command}')
        jarvis.speak('Do you wish to know about something else?')
        newcommand = jarvis.takeCommand()
        if 'no' in newcommand:
            jarvis.speak('Okay sir.')
        elif 'yes' in newcommand:
            jarvis.speak('What sir?')
            newcommand = jarvis.takeCommand()
            if 'i want to know about' in newcommand:
                newcommand = newcommand.replace('i want to know about','')
            get_howto_result(newcommand)
        elif 'none' in newcommand or newcommand is None:
            pass
        else:
            jarvis.speak('I did not quite get you.')