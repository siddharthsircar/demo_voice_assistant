import datetime
import sys
import time

import jarvis_voice_assistant as jarvis

if __name__ == "__main__":
    counter = 0
    while True:
        permission = jarvis.takeCommand()

        if 'wake up' in permission or 'wakeup' in permission:
            hour = int(datetime.datetime.now().hour)

            if (hour >= 23 and hour<24) or (hour >= 0 and hour<9):
                if (hour >= 23 and hour<24) or (hour >= 0 and hour<4):
                    jarvis.speak('Please let me sleep sir, It\'s pretty late')

                elif (hour >= 4 and hour<9):
                    jarvis.speak('Please let me sleep sir, It\'s quite early')
                response = jarvis.takeCommand().lower()

                if 'ok' in response or 'sleep' in response:
                    jarvis.speak('Thank you.')

                elif 'no' in response or 'wake up' in response or 'wakeup' in response:
                    jarvis.speak('Okay. I\'ll be up in a few seconds')
                    counter += 1
                    jarvis.run_jarvis(counter)

        elif 'jarvis' in permission:
            counter += 1
            jarvis.run_jarvis(counter)

        elif 'terminate' in permission:
            sys.exit()