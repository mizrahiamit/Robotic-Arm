import sys


from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *#(Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QLabel, QPushButton)
from main_function import *


import time
#from PyQt4.QtCore import SIGNAL
#from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

       
        self._running = False
        #------------------------------------------
        self.act_msg = QtGui.QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Stand by")
        #------------------------------------------
        self.start_btn= QtGui.QPushButton()
        self.start_btn.setText("Start")
        
        self.start_btn.clicked.connect(self.start_clicked)

        self.pause_btn=QtGui.QPushButton()
        self.pause_btn.setText("Pause")
        
        self.connect(self.pause_btn,SIGNAL("clicked()"),self.pause_clicked)

        self.stop_btn=QtGui.QPushButton()
        self.stop_btn.setText("Stop")
        
        self.connect(self.stop_btn,SIGNAL("clicked()"),self.stop_clicked)
        #------------------------------------------
        self.addx = QtGui.QLineEdit()
        self.addy = QtGui.QLineEdit()
        #------------------------------------------
        self.status_msg = QtGui.QLineEdit()
        self.status_msg.setObjectName("status_msg")
        self.status_msg.setText("Stand by")
        #------------------------------------------
        
        #------------------------------------------
        self.workerThread = WorkrThread()#***************************************
        #------------------------------------------
        row = 1
        
        grid=QtGui.QGridLayout()

        grid.addWidget(QtGui.QLabel("Action message"),row,1,1,4)

        row=row+1
        grid.addWidget(self.act_msg,row,1,1,4)

        row=row+1
        grid.addWidget(self.start_btn,row,1,1,1)
        grid.addWidget(self.pause_btn,row,2,1,1)
        grid.addWidget(self.stop_btn,row,3,1,1)

        row=row+1
        grid.addWidget(QtGui.QLabel("X_target ="),row,1,1,1)
        grid.addWidget(self.addx,row,2,1,1)
        grid.addWidget(QtGui.QLabel("Y_target ="),row,3,1,1)
        grid.addWidget(self.addy,row,4,1,1)

        row=row+1
        grid.addWidget(QtGui.QLabel("Status message"),row,1,1,4)

        row=row+1
        grid.addWidget(self.status_msg,row,1,1,4)

        



        self.setLayout(grid)
        #win.setGeometry(x,y,width,height)
        self.setGeometry(100,100,600,350)
        self.setWindowTitle("Camera Control XY Robotic Arm")



        

    def start_clicked(self):
        self._running = True
        self.workerThread.start()#******************************
        self.status_msg.setText("Start clicked")
        print "Start clicked"

    def pause_clicked(self):
        self._running = False
        self.status_msg.setText("Pause clicked")
        print "Pause clicked"

    def stop_clicked(self):
        self._running = False
        self.status_msg.setText("Stop clicked")
        print "Stop clicked"


class WorkrThread(QThread):

    def __init__(self, parent=None):
        super(WorkrThread, self).__init__(parent)

    def run(self):
        sleep(5)
        print "Enter thread"
        


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()