import pywhatkit
import wikipedia

import jarvis_voice_assistant as jarvis


def search_google(query):
    jarvis.speak(f'Searching for {query}')
    try:
        pywhatkit.search(query)
    except:
        jarvis.speak(f'Could not find information on {query}')

def search_wiki(query):
    jarvis.speak(f'Asking Wiki about {query}')
    try:
        result = wikipedia.summary(query, sentences=1)
        jarvis.speak(result)
        jarvis.speak('Anything else sir?')
        command = jarvis.takeCommand()

        if 'no' in command:
            jarvis.speak('Okay.')

        elif 'repeat' in command:
            jarvis.speak(result)

        elif 'yes' in command:
            jarvis.speak('What do you want to know about?')
            command = jarvis.takeCommand()
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
        jarvis.speak(f'Wiki has no information on {query}')
        jarvis.speak('Anything else sir?')
        command = jarvis.takeCommand()
        if 'no' in command:
            jarvis.speak('Okay.')

        elif 'yes' in command:
            jarvis.speak('What do you want to know about?')
            command = jarvis.takeCommand()
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
                jarvis.speak('I did not quite get you.')
