import sys


from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QLabel, QPushButton)
from main_function import *

import time


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

       

        self.algoritem_enable = False
        #------------------------------------------
        self.act_msg = QtGui.QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Please choose coordinates")
        #------------------------------------------
        self.start_btn= QtGui.QPushButton()
        self.start_btn.setText("Start")
        
        self.connect(self.start_btn,SIGNAL("clicked(bool)"),self.start_clicked)
        

        self.pause_btn=QtGui.QPushButton()
        self.pause_btn.setText("Pause")
        #self.pause_btn.setEnabled(False)
        
        self.connect(self.pause_btn,SIGNAL("clicked()"),self.pause_clicked)

        self.stop_btn=QtGui.QPushButton()
        self.stop_btn.setText("Stop")
        #self.stop_btn.setEnabled(False)
        
        self.connect(self.stop_btn,SIGNAL("clicked()"),self.stop_clicked)
        #------------------------------------------
        self.addx = QtGui.QLineEdit()
        self.addx.setText("0")
        self.addy = QtGui.QLineEdit()
        self.addy.setText("0")
        #------------------------------------------
        self.status_msg = QtGui.QLineEdit()
        self.status_msg.setObjectName("status_msg")
        self.status_msg.setText("Stand by")
        #------------------------------------------
        self.l2=QtGui.QLabel()
        self.l2.setPixmap(QtGui.QPixmap("detected circles.jpg"))
        #Get pixel coordinates by right click on the mouse
        self.l2.mousePressEvent = self.getPos
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

        row=row+1
        grid.addWidget(QtGui.QLabel("ROI image"),row,1,1,4)

        row=row+1
        grid.addWidget(self.l2,row,1,8,6)


        while (self.algoritem_enable):
            time.sleep(1)
            print "Take picture"
            time.sleep(1)
            print "show picture"
            time.sleep(1)
            print "locate arm position"
            time.sleep(1)
            print "check success"
            time.sleep(1)
            print "calculate arm next move"
            time.sleep(1)
            print "command to the servo motors"

        self.setLayout(grid)
        #setGeometry(x,y,width,height)
        self.setGeometry(100,100,600,350)
        self.setWindowTitle("Camera Control XY Robotic Arm")



        

    def start_clicked(self,bool):
        self.status_msg.setText("Start clicked")
        print "Start clicked"
        
        dst_coordinate = int(self.addx.text()) , int(self.addy.text())
 
        #get from detection, example: [310 , 410]
        src_coordinate = 310 , 410
        if(check_coordinates(dst_coordinate,src_coordinate,200)):
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            self.status_msg.setText("Running")
            self.act_msg.setText("Stand by")

            self.algoritem_enable = True
            
                
        else:
            self.start_btn.setEnabled(True)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
            self.status_msg.setText("Coordinates out of reach")
            self.act_msg.setText("Please choose coordinates")

            self.addx.setText('0')
            self.addy.setText('0')
'''
    def robotic_arm_algoritem(self,bool):
        while bool:
            time.sleep(1)
            print "Take picture"
            time.sleep(1)
            print "show picture"
            time.sleep(1)
            print "locate arm position"
            time.sleep(1)
            print "check success"
            time.sleep(1)
            print "calculate arm next move"
            time.sleep(1)
            print "command to the servo motors"
'''

    




        

    def pause_clicked(self):
        self.status_msg.setText("Paused")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.act_msg.setText("Waiting for command")

        self.algoritem_enable = False

        print "Pause clicked"

    def stop_clicked(self):
        self.status_msg.setText("Stoped")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.act_msg.setText("Please choose coordinates")

        self.addx.setText('0')
        self.addy.setText('0')

        disable_arm()

        self.algoritem_enable = False

        print "Stop clicked"

    def getPos(self, event):
        x = event.pos().x()
        self.addx.setText(str(x))
        y = event.pos().y()
        self.addy.setText(str(y))
        print ("x = ", x,"y = ", y)
        
'''
    def mousePressEvent(self, QMouseEvent):
        print QMouseEvent.pos()
'''


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()