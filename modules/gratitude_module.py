import sys

import jarvis_voice_assistant as jarvis

def gratitude_module(command):
    if ('thank you' in command and 'goodnight' in command) or \
         ('thank you' in command and 'good night' in command) or \
         ('thankyou' in command and 'good night' in command) or \
         ('thankyou' in command and 'goodnight' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Night!')
        jarvis.speak('Let me know when you need me')
        return 'sleep'

    elif ('thank you' in command and 'bye bye' in command) or \
         ('thank you' in command and 'byebye' in command) or \
         ('thankyou' in command and 'bye bye' in command) or \
         ('thankyou' in command and 'byebye' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Bye!')
        jarvis.speak('Let me know when you need me')
        return 'sleep'

    elif ('thank you' in command and 'goodbye' in command) or \
         ('thank you' in command and 'good bye' in command) or \
         ('thankyou' in command and 'good bye' in command) or \
         ('thankyou' in command and 'goodbye' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Bye!')
        jarvis.speak('Let me know when you need me')
        return 'sleep'

    elif 'goodbye' in command or 'good bye' in command:
        jarvis.speak('Good bye sir!')
        jarvis.speak('Let me know when you need me')
        return 'sleep'

    elif 'goodnight' in command or 'good night' in command:
        jarvis.speak('Good night sir!')
        jarvis.speak('Let me know when you need me')
        return 'sleep'

    elif 'thank you' in command or 'thankyou' in command:
        jarvis.speak('Glad to help!')
        return 'none'