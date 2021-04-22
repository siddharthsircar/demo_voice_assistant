import pywhatkit
import wikipedia

import voice_assistant as assistant


def search_google(query):
    assistant.speak(f'Searching for {query}')
    try:
        pywhatkit.search(query)
    except:
        assistant.speak(f'Could not find information on {query}')

def search_wiki(query):
    assistant.speak(f'Asking Wiki about {query}')
    try:
        result = wikipedia.summary(query, sentences=1)
        assistant.speak(result)
        assistant.speak('Anything else sir?')
        command = assistant.takeCommand()

        if 'no' in command:
            assistant.speak('Okay.')

        elif 'repeat' in command:
            assistant.speak(result)

        elif 'yes' in command:
            assistant.speak('What do you want to know about?')
            command = assistant.takeCommand()
            if 'who is' in command:
                query = command.replace('who is', '')
                search_wiki(query)
            elif 'what is' in command:
                query = command.replace('what is', '')
                search_wiki(query)
            elif 'tell me about' in command:
                query = command.replace('tell me about', '')
                search_wiki(query)
            else:
                search_wiki(command)
    except:
        assistant.speak(f'Wiki has no information on {query}')
        assistant.speak('Anything else sir?')
        command = assistant.takeCommand()
        if 'no' in command:
            assistant.speak('Okay.')

        elif 'yes' in command:
            assistant.speak('What do you want to know about?')
            command = assistant.takeCommand()
            if 'who is' in command:
                query = command.replace('who is', '')
                search_wiki(query)
            elif 'what is' in command:
                query = command.replace('what is', '')
                search_wiki(query)
            elif 'tell me about' in command:
                query = command.replace('tell me about', '')
                search_wiki(query)
            elif 'none' in command or command is None:
                pass
            else:
                assistant.speak('I did not quite get you.')
