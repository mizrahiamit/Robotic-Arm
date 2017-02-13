import sys


from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QLabel, QPushButton)
from main_function import *
#from PyQt4.QtCore import SIGNAL
#from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

       


        #------------------------------------------
        self.act_msg = QtGui.QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Please choose coordinates")
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



        self.setLayout(grid)
        #setGeometry(x,y,width,height)
        self.setGeometry(100,100,600,350)
        self.setWindowTitle("Camera Control XY Robotic Arm")



        self.setWindowTitle("Learning")

    def start_clicked(self):
        self.status_msg.setText("Start clicked")
        print "Start clicked"
        dst_coordinate = [int(self.addx) , int(self.addy)]
        #get from detection, example: [310 , 410]
        src_coordinate = [310 , 410]
        if(check_coordinates(dst_coordinate,arm_src_coor,arm_radius)):
            self.status_msg.setText("Running")
            self.act_msg.setText("Stand by")
            robotic_arm_algoritem()
        else:
            self.status_msg.setText("Coordinates out of reach")
            self.act_msg.setText("Please choose coordinates")

            self.addx.setText('0')
            self.addy.setText('0')




        

    def pause_clicked(self):
        self.status_msg.setText("Paused")
        self.act_msg.setText("Waiting for command")
        print "Pause clicked"

    def stop_clicked(self):
        self.status_msg.setText("Stoped")
        self.act_msg.setText("Please choose coordinates")

        self.addx.setText('0')
        self.addy.setText('0')

        disable_arm()

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