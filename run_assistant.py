import datetime
import sys
import time

import voice_assistant as assistant

if __name__ == "__main__":
    counter = 0
    while True:
        permission = assistant.takeCommand()

        if 'terminate' in permission or 'i don\'t need you' in permission or 'i do not need you' in permission:
            sys.exit()

        elif 'friday' in permission:
            counter += 1
            assistant.run_friday(counter)

        elif 'wake up' in permission or 'wakeup' in permission:
            hour = int(datetime.datetime.now().hour)

            if (hour >= 23 and hour<24) or (hour >= 0 and hour<9):
                if (hour >= 23 and hour<24) or (hour >= 0 and hour<4):
                    assistant.speak('Please let me sleep sir, It\'s pretty late')

                elif (hour >= 4 and hour<9):
                    assistant.speak('Please let me sleep sir, It\'s quite early')
                response = assistant.takeCommand().lower()

                if 'ok' in response or 'sleep' in response:
                    assistant.speak('Thank you.')

                elif 'no' in response or 'wake up' in response or 'wakeup' in response:
                    assistant.speak('Okay. I\'ll be up in a few seconds')
                    time.sleep(10)
                    counter += 1
                    assistant.run_jarvis(counter)

        elif 'jarvis' in permission or 'are you up' in permission:
            counter += 1
            assistant.run_jarvis(counter)
