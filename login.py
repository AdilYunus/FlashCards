from PyQt5 import QtWidgets, uic, QtCore
import sys
import os
import json
import menu


class Login(QtWidgets.QDialog):

    user_name = ""

    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('ui/login1.ui', self)
        self.pushButton.clicked.connect(self.login)
        # enter tusuyla da sonraki ikrana gidebilir -A
        self.pushButton.setAutoDefault(True)
        # login page ->cancel button -A
        self.pushButton_2.clicked.connect(self.cancel)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.show()

    def login(self):
        # login methode
        self.user_name = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        if not os.path.isfile('user/'+self.user_name+'.json'):
            self.signup()
        else:
            with open('user/'+self.user_name+'.json', 'r') as jsFile:
                user_data = json.load(jsFile)
            if user_data['password'] == self.password:
                self.cams = menu.Menu(self.user_name)
                self.cams.show()
                self.close()
            elif self.password == "" and self.user_name =="":
                self.login_info.setText("Please enter your username & password")
            elif self.password =="":
                self.login_info.setText("Please enter your password")
            else:
                self.login_info.setText("Invalid username password combination")
                


    def signup(self):
        # sign up methode
        self.user_info = {
            'username': self.user_name,
            'password': self.password,
            'level': 1,
            'time': 0
        }
        if self.password == "" and self.user_name =="":
            self.login_info.setText("Please enter your username & password")
        elif self.password == "":
            self.login_info.setText("Please enter your password")
        elif self.user_name =="":
            self.login_info.setText("Please enter your username")
        
        else:
            js_file_name = 'user/'+self.user_name+'.json'
            with open(js_file_name, 'w') as jsFile:
                jsFile.write(json.dumps(self.user_info, indent=4))
            
            self.cams = menu.Menu(self.user_name)
            self.cams.show()
            self.close()
        

    def cancel(self):  # quit
        self.close()
