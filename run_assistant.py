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

from gui.ui.jarvis_gui import Ui_jarvisgui

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
                    time.sleep(5)
                    counter += 1
                    assistant.run_jarvis(counter)

        elif 'jarvis' in permission or 'are you up' in permission:
            counter += 1
            assistant.run_jarvis(counter)



# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread,self).__init__()
#
#     def run_assistant(self):
#         counter = 0
#         while True:
#             permission = assistant.takeCommand()
#
#             if 'terminate' in permission or 'i don\'t need you' in permission or 'i do not need you' in permission:
#                 sys.exit()
#
#             elif 'friday' in permission:
#                 counter += 1
#                 assistant.run_friday(counter)
#
#             elif 'wake up' in permission or 'wakeup' in permission:
#                 hour = int(datetime.datetime.now().hour)
#
#                 if (hour >= 23 and hour < 24) or (hour >= 0 and hour < 9):
#                     if (hour >= 23 and hour < 24) or (hour >= 0 and hour < 4):
#                         assistant.speak('Please let me sleep sir, It\'s pretty late')
#
#                     elif (hour >= 4 and hour < 9):
#                         assistant.speak('Please let me sleep sir, It\'s quite early')
#                     response = assistant.takeCommand().lower()
#
#                     if 'ok' in response or 'sleep' in response:
#                         assistant.speak('Thank you.')
#
#                     elif 'no' in response or 'wake up' in response or 'wakeup' in response:
#                         assistant.speak('Okay. I\'ll be up in a few seconds')
#                         time.sleep(5)
#                         counter += 1
#                         assistant.run_jarvis(counter)
#
#             elif 'jarvis' in permission or 'are you up' in permission:
#                 counter += 1
#                 assistant.run_jarvis(counter)
#
#     def run(self):
#         self.run_assistant()
#
# startExecution = MainThread()
#
# class Runner(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_jarvisgui()
#         self.ui.setupUi(self)
#         self.ui.runAssistant.clicked.connect(self.startTask)
#         self.ui.putToSleep.clicked.connect(self.close())
#
#     def startTask(self):
#         self.ui.movie = QtGui.QMovie('resources/jarvis-intro-1.gif')
#         self.ui.label.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         timer = QTimer(self)
#         timer.timeout().connect(self.showTime)
#         timer.start(1000)
#         startExecution.start()
#
#     def showTime(self):
#         current_time = QTime.currentTime()
#         current_date = QDate.currentDate()
#         label_time = current_time.toString('%I:%M %p')
#         label_date = current_date.toString(Qt.ISODate)
#         self.ui.date.setText(label_date)
#         self.ui.time.setText(label_time)
#
# app = QApplication(sys.argv)
# jarvis = Runner()
# jarvis.show()
# exit(app.exec_())