from PyQt5 import QtWidgets, uic
import sys
from game import Game
import json

class Menu(QtWidgets.QDialog):

    def __init__(self,name):
        self.name=name
        super(Menu, self).__init__()
        uic.loadUi('ui/menu.ui', self)
        self.label_username.setText(self.name)
        self.pushButton.clicked.connect(self.play)
        self.progressBar_menu.setProperty("value",self.total_progress())#call menu progressBar -A
        self.quitButton_2.clicked.connect(self.quit)# menu page-> quit -A
        self.show()

    def play(self):
        self.cams = Game(self.name,self.level_1)
        self.cams.show()
        self.close()


    def total_progress(self):#total progress for total level -A
        with open('user/'+self.name+'.json','r') as jsFile:
            user_data = json.load(jsFile)
            self.level_1 = user_data["level"]
            return self.level_1*100/250
    def quit(self):# quit methode-A
        self.close()



