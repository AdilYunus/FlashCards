from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QTime, QTimer
import menu
import json
import sys
from datetime import datetime


class Game(QtWidgets.QDialog):

    def __init__(self, name, level, count_t):
        self.name = name
        self.level = level
        self.count_t = count_t
        self.count_s = '00:00:00'
        self.count = 3
        super(Game, self).__init__()
        uic.loadUi('ui/game_screen.ui', self)
        # when click beck button call func. back
        self.quitButton.clicked.connect(self.back)
        self.levelNumber.setText(str(self.level))
        # disable window close button
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #game time
        self.total_time()
        self.gameTime.setText(self.count_s)
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.total_time)
        self.timer1.start(1000)

        #when the game begin true and false button are disable
        self.pushButton.setEnabled(False)
        self.pushButton.toggle()
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.toggle()
        #in game when click true & false button call methode
        self.pushButton.clicked.connect(self.true)
        self.pushButton_2.clicked.connect(self.false)

        self.show() 
        # ----------QTimer------
        self.sleeptime.setText(str(self.count))
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.timer_TimeOut)
        self.timer2.start(1000)
        # -----call the game methode
        self.load_words()

    def total_time(self):
        #methode for game time
        
        self.count_t += 1
        self.time = self.count_t
        self.time = int(self.time)
        self.day = self.time // (24 * 3600)
        self.time = self.time % (24 * 3600)
        self.hour = self.time // 3600
        self.time %= 3600
        self.minutes = self.time // 60
        self.time %= 60
        self.seconds = self.time
        if self.day != 0:
            self.count_s = "%02d:%02d:%02d:%02d" % (
                self.day, self.hour, self.minutes, self.seconds)
        elif self.day == 0:
            self.count_s = "%02d:%02d:%02d" % (
                self.hour, self.minutes, self.seconds)
        self.gameTime.setText(self.count_s)
        

    def timer_TimeOut(self):
        #methode for sleep time 
        self.count -= 1
        if self.count == 0:
            #show the english word
            self.words.setText(self.word_list[self.index][1])
            self.language.setText('English')
            #let sleep time stop en wait for click
            self.timer2.stop()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)

        self.sleeptime.setText(str(self.count))

    def back(self):
        self.level_update()  # call methode to level update -A
        self.cams = menu.Menu(self.name)
        self.cams.show()
        self.close()

    def level_update(self):  # level and game time update -A
        self.user_info = {
            'username': self.name,
            'level': self.level,
            'time': self.count_t
        }
        js_file_name = 'user/'+self.name+'.json'
        with open(js_file_name, 'w') as jsFile:
            jsFile.write(json.dumps(self.user_info, indent=4))

    def true(self):  # click True +1 to c_true
        #set button disable
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        #start sleep time
        self.timer2.start(1000)
        self.count = 3
        #update sleep time
        self.sleeptime.setText(str(self.count))
        self.words.setText(self.word_list[self.index][0])
        self.c_true += 1
        self.index += 1
        #show dutch word
        
        self.point1.setText(str(self.c_true))
        self.point2.setText(str(self.c_false))

        self.language.setText('Nederlands')
        #updat progresbar
        self.progressBar_ingame.setProperty("value", self.c_true)

        if self.c_true == 20:  # if c_true = 20 level +1 and begin new level
            self.level += 1
            self.c_true = 0
            self.c_false = 0
            self.point2.setText(str(self.c_false))
            self.point1.setText(str(self.c_true))
            self.levelNumber.setText(str(self.level))
            self.progressBar_ingame.setProperty("value", self.c_true)
            self.index = 0
            self.word_list = []
            if self.level == 251:#If the player has done all level.than back to level 1
                self.timer2.stop()
                self.level = 1
                self.index = 0
                self.back()
                self.close()

            else:

                #call methode for begin new level
                self.load_words()

    def false(self):  # click false +1 to c_false and append this word to word_list -A
        #set button disable
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.timer2.start(1000)
        self.count = 3
        self.sleeptime.setText(str(self.count))
        #append words to last of list
        self.word_list.append(self.word_list[self.index])
        self.c_false += 1
        self.point2.setText(str(self.c_false))
        self.index += 1
        self.words.setText(self.word_list[self.index][0])
        self.language.setText('Nederlands')

    def load_words(self):

        self.index = 0
        self.levelNumber.setText(str(self.level))
        self.word_list = []

        with open('nl_words_4data.json', 'r') as jsFile:
            self.total_list = json.load(jsFile)
        # --------
        level_w = self.level*20+1
        # take 20 wordes from total_list give to word_list -A
        for n in range(level_w-20, level_w):
            self.word_list.append(
                [self.total_list[str(n)]['Dutch Word'], self.total_list[str(n)]['English Word']])

        # -------a
        self.c_true = 0
        self.c_false = 0
        self.point1.setText(str(self.c_true))
        self.point2.setText(str(self.c_false))

        self.words.setText(self.word_list[self.index][0])
        self.language.setText('Nederlands')
