import datetime
import sys
import time

import voice_assistant as assistant

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from gui.jarvis_2_1 import Ui_Form

# if __name__ == "__main__":
#     counter = 0
#     while True:
#         permission = assistant.takeCommand()
#
#         if 'terminate' in permission or 'i don\'t need you' in permission or 'i do not need you' in permission:
#             sys.exit()
#
#         elif 'friday' in permission:
#             counter += 1
#             assistant.run_friday(counter)
#
#         elif 'wake up' in permission or 'wakeup' in permission:
#             hour = int(datetime.datetime.now().hour)
#
#             if (hour >= 23 and hour<24) or (hour >= 0 and hour<9):
#                 if (hour >= 23 and hour<24) or (hour >= 0 and hour<4):
#                     assistant.speak('Please let me sleep sir, It\'s pretty late')
#
#                 elif (hour >= 4 and hour<9):
#                     assistant.speak('Please let me sleep sir, It\'s quite early')
#                 response = assistant.takeCommand().lower()
#
#                 if 'ok' in response or 'sleep' in response:
#                     assistant.speak('Thank you.')
#
#                 elif 'no' in response or 'wake up' in response or 'wakeup' in response:
#                     assistant.speak('Okay. I\'ll be up in a few seconds')
#                     time.sleep(5)
#                     counter += 1
#                     assistant.run_jarvis(counter)
#
#         elif 'jarvis' in permission or 'are you up' in permission:
#             counter += 1
#             assistant.run_jarvis(counter)

# Converting py design to py class: pyuic5 -x jarvis2_0.ui -o jarvis2_0.py

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run_assistant(self):
        self.counter = 0
        while True:
            self.permission = assistant.takeCommand()

            if 'terminate' in self.permission or 'i don\'t need you' in self.permission or 'i do not need you' in self.permission:
                sys.exit()

            elif 'friday' in self.permission:
                self.counter += 1
                assistant.run_friday(self.counter)

            elif 'wake up' in self.permission or 'wakeup' in self.permission:
                hour = int(datetime.datetime.now().hour)

                if (hour >= 23 and hour < 24) or (hour >= 0 and hour < 9):
                    if (hour >= 23 and hour < 24) or (hour >= 0 and hour < 4):
                        assistant.speak('Please let me sleep sir, It\'s pretty late')

                    elif (hour >= 4 and hour < 9):
                        assistant.speak('Please let me sleep sir, It\'s quite early')
                    response = assistant.takeCommand().lower()

                    if 'ok' in response or 'sleep' in response:
                        assistant.speak('Thank you.')

                    elif 'no' in response or 'wake up' in response or 'wakeup' in response:
                        assistant.speak('Okay. I\'ll be up in a few seconds')
                        time.sleep(5)
                        self.counter += 1
                        assistant.run_jarvis(self.counter)

            elif 'jarvis' in self.permission or 'are you up' in self.permission:
                self.counter += 1
                # self.Runner.change_animation('S:\\Development\\Python\\jarvis_voiceai\\resources\\listening.gif')
                assistant.run_jarvis(self.counter)

    def run(self):
        self.run_assistant()

startExecution = MainThread()

class Runner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.movie = QtGui.QMovie('S:\\Development\\Python\\jarvis_voiceai\\resources\\ai_animation_2.gif')
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.startTask()

    def startTask(self):
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Runner()
jarvis.show()
sys.exit(app.exec_())