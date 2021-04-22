from pywikihow import search_wikihow
import voice_assistant as assistant

def get_howto_result(command):
    assistant.speak(f'Searching database for {command}')
    try:
        max_results = 1
        how_to = search_wikihow(command, max_results)
        assert len(how_to) == 1
        how_to[0].print()
        assistant.speak(how_to[0].summary)
        assistant.speak('Anything else sir?')
        command = assistant.takeCommand()
        if 'no' in command:
            assistant.speak('Okay sir.')
        elif 'repeat' in command:
            assistant.speak(how_to[0].summary)
        elif 'how to' in command:
            get_howto_result(command)
        elif 'yes' in command:
            assistant.speak('What sir?')
            newcommand = assistant.takeCommand()
            get_howto_result(newcommand)
    except:
        assistant.speak(f'No information on {command}')
        assistant.speak('Do you wish to know about something else?')
        newcommand = assistant.takeCommand()
        if 'no' in newcommand:
            assistant.speak('Okay sir.')
        elif 'yes' in newcommand:
            assistant.speak('What sir?')
            newcommand = assistant.takeCommand()
            if 'i want to know about' in newcommand:
                newcommand = newcommand.replace('i want to know about','')
            get_howto_result(newcommand)
        elif 'none' in newcommand or newcommand is None:
            pass
        else:
            assistant.speak('I did not quite get you.')