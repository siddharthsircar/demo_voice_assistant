import jarvis_voice_assistant as jarvis

def gratitude_module(command):
    if ('thank you' in command and 'goodnight' in command) or \
         ('thank you' in command and 'good night' in command) or \
         ('thankyou' in command and 'good night' in command) or \
         ('thankyou' in command and 'goodnight' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Night!')
        exit()

    elif ('thank you' in command and 'bye bye' in command) or \
         ('thank you' in command and 'byebye' in command) or \
         ('thankyou' in command and 'bye bye' in command) or \
         ('thankyou' in command and 'byebye' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Bye!')
        exit()

    elif ('thank you' in command and 'goodbye' in command) or \
         ('thank you' in command and 'good bye' in command) or \
         ('thankyou' in command and 'good bye' in command) or \
         ('thankyou' in command and 'goodbye' in command):
        jarvis.speak('Always at your service sir!')
        jarvis.speak('Good Bye!')
        exit()

    elif 'thank you' in command or 'thankyou' in command:
        jarvis.speak('Always at your service sir!')

    elif 'goodbye' in command or 'good bye' in command:
        jarvis.speak('Good bye sir!')
        exit()

    elif 'goodnight' in command or 'good night' in command:
        jarvis.speak('Good night sir!')
        exit()