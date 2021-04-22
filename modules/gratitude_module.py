import sys

import voice_assistant as assistant

def gratitude_module(command):
    if ('thank you' in command and 'goodnight' in command) or \
         ('thank you' in command and 'good night' in command) or \
         ('thankyou' in command and 'good night' in command) or \
         ('thankyou' in command and 'goodnight' in command):
        assistant.speak('Always at your service sir!')
        assistant.speak('Good Night!')
        assistant.speak('Let me know when you need me')
        return 'sleep'

    elif ('thank you' in command and 'bye bye' in command) or \
         ('thank you' in command and 'byebye' in command) or \
         ('thankyou' in command and 'bye bye' in command) or \
         ('thankyou' in command and 'byebye' in command):
        assistant.speak('Always at your service sir!')
        assistant.speak('Good Bye!')
        assistant.speak('Let me know when you need me')
        return 'sleep'

    elif ('thank you' in command and 'goodbye' in command) or \
         ('thank you' in command and 'good bye' in command) or \
         ('thankyou' in command and 'good bye' in command) or \
         ('thankyou' in command and 'goodbye' in command):
        assistant.speak('Always at your service sir!')
        assistant.speak('Good Bye!')
        assistant.speak('Let me know when you need me')
        return 'sleep'

    elif 'goodbye' in command or 'good bye' in command:
        assistant.speak('Good bye sir!')
        assistant.speak('Let me know when you need me')
        return 'sleep'

    elif 'goodnight' in command or 'good night' in command:
        assistant.speak('Good night sir!')
        assistant.speak('Let me know when you need me')
        return 'sleep'

    elif 'thank you' in command or 'thankyou' in command:
        assistant.speak('Glad to help!')
        return 'none'