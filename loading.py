from PyQt5 import QtWidgets, uic, QtCore,Qt
from PyQt5.QtCore import QTime, QTimer, Qt
import sys
import login
import json
import res

class Loading(QtWidgets.QDialog):

    def __init__(self):
        super(Loading, self).__init__()
        uic.loadUi('ui/loading.ui', self)
        #call menu progressBar -A
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #hidden frame
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()
        self.progressBar.setProperty("value",1)
        
        self.count = 6 
        self.progressBar.setProperty("value",self.count)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.timer_TimeOut)
        self.timer2.start(15)

    def timer_TimeOut(self):
        #methode for sleep time 
        self.count += 1
        self.progressBar.setProperty("value",self.count)
        if self.count == 100:
        
            self.cams = login.Login()
            self.cams.show()
            self.close()


