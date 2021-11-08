from PyQt5 import QtWidgets, uic
import sys
import os
import json
import menu

class Login(QtWidgets.QDialog):
    
    user_name=""
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setAutoDefault(True)#enter tusuyla da sonraki ikrana gidebilir -A
        self.pushButton_2.clicked.connect(self.cancel)# login page ->cancel button -A
        self.show()
        
    def login(self):
    #login methode
        self.user_name=self.lineEdit_username.text()
        if not os.path.isfile('user/'+self.user_name+'.json'):
            self.signup()
        
        self.cams = menu.Menu(self.user_name)
        self.cams.show()
        self.close()


    def signup(self):
    #sign up methode
        self.user_info = {
            'username':self.user_name,
            'level':1
            }
        
        js_file_name = 'user/'+self.user_name+'.json'       
        with open(js_file_name,'w') as jsFile:
            jsFile.write(json.dumps(self.user_info,indent=4))
        
    def cancel(self):#quit
        self.close()

