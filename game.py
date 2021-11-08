from PyQt5 import QtWidgets, uic
import sys
import menu
import json
from level import Polo
class Game(QtWidgets.QDialog):
    

    def __init__(self,name,level):
        self.name=name
        self.level_1 = level
        # print(self.level_1)
        super(Game, self).__init__()
        uic.loadUi('ui/game_screen.ui', self)
        self.quitButton.clicked.connect(self.back)
        self.show()
        # self.play_game()
        

    def back(self):
        self.level_update()# call methode to level update -A
        self.cams = menu.Menu(self.name)
        self.cams.show()
        self.level_update()
        self.close()

    def level_update(self):# level update -A
        self.user_info = {
            'username':self.name,
            'level':self.level_1
            }
        js_file_name = 'user/'+self.name+'.json'       
        with open(js_file_name,'w') as jsFile:
            jsFile.write(json.dumps(self.user_info,indent=4))

    def timer(self):
        pass

    # =================================================#

    def play_game(self):
        pass

