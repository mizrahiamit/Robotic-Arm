'''
Name: main.py
Author: Mizrahi Amit
Last update:4/3/17
Project: Camera Control XY Robotic Arm
'''
# Only needed for access to command line arguments
import sys


from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QWidget, QHBoxLayout, QLabel, QPushButton)
from main_function import *
from image processing functions import *

import time


class Form(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(Form, self).__init__(parent, **kwargs)

        #set parameters for the timing the loop generator
        self._generator = None
        self._timerId = None
        #------------------------------------------
        #Arm position parameters 
        self._shoulder_pos = None,None
        self._elbow_pos = None,None
        self._wrist_pos = None,None
        #------------------------------------------
        #Msg that tell the user what the next move
        self.act_msg = QtGui.QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Please choose coordinates")
        #------------------------------------------
        #Start button
        self.check_btn= QtGui.QPushButton()
        self.check_btn.setText("Check system")
        
        #------------------------------------------
        #Start button
        self.start_btn= QtGui.QPushButton()
        self.start_btn.setText("Start")
        self.connect(self.start_btn,SIGNAL("clicked(bool)"),self.start_clicked)
        
        #Pause button
        self.pause_btn=QtGui.QPushButton()
        self.pause_btn.setText("Pause")
        #self.pause_btn.setEnabled(False)
        self.connect(self.pause_btn,SIGNAL("clicked()"),self.pause_clicked)

        #Stop button
        self.stop_btn=QtGui.QPushButton()
        self.stop_btn.setText("Stop")
        #self.stop_btn.setEnabled(False)
        self.connect(self.stop_btn,SIGNAL("clicked()"),self.stop_clicked)
        #------------------------------------------
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        #------------------------------------------
        #XY coordinates by the user choise
        self.addx = QtGui.QLineEdit()
        self.addx.setText("0")
        self.addy = QtGui.QLineEdit()
        self.addy.setText("0")
        #------------------------------------------
        #Msg that tell the user the system status
        self.status_msg = QtGui.QLineEdit()
        self.status_msg.setObjectName("status_msg")
        self.status_msg.setText("Stand by")
        #------------------------------------------
        #Show image
        self.l2=QtGui.QLabel()
        self.l2.setPixmap(QtGui.QPixmap("Test Image.jpg"))
        #Get pixel coordinates by right click on the mouse
        self.l2.mousePressEvent = self.getPos
        #------------------------------------------
        
        #GUI format
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        #check for arm rdetection button
        vbox.addWidget(self.check_btn)
        vbox.addStretch()
        #Action Msg
        hbox.addWidget(QtGui.QLabel("Action message"))
        #hbox.addStretch()
        hbox.addWidget(self.act_msg)

        vbox.addLayout(hbox)
        vbox.addStretch()
        #Start  Pause  Stop buttons
        hbox = QtGui.QHBoxLayout()
        
        hbox.addWidget(self.start_btn)
        hbox.addStretch()
        hbox.addWidget(self.pause_btn)
        hbox.addStretch()
        hbox.addWidget(self.stop_btn)

        vbox.addLayout(hbox)
        vbox.addStretch()
        #XY coordinates
        hbox = QtGui.QHBoxLayout()
        
        hbox.addWidget(QtGui.QLabel("X_target ="))
        hbox.addStretch()
        hbox.addWidget(self.addx)
        hbox.addStretch()
        hbox.addWidget(QtGui.QLabel("Y_target ="))
        hbox.addStretch()
        hbox.addWidget(self.addy)

        vbox.addLayout(hbox)
        vbox.addStretch()
        #Status Msg
        hbox = QtGui.QHBoxLayout()
        
        hbox.addWidget(QtGui.QLabel("Status message"))
        #hbox.addStretch()
        hbox.addWidget(self.status_msg)

        vbox.addLayout(hbox)
        vbox.addStretch()
        #Image
        
        vbox.addWidget(QtGui.QLabel("ROI image"))

        vbox.addStretch()
        vbox.addWidget(self.l2)

        self.setLayout(vbox)
        #------------------------------------------
        #setGeometry(x,y,width,height)
        self.setGeometry(100,100,600,350)
        #Title for main window
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
            #set parameters for the timing the loop generator
            # Stop any existing timer
            if self._timerId is not None:
                self.killTimer(self._timerId)
            self._generator = None
            self._timerId = None
            # Start the loop
            self._generator = self.loopGenerator()
            # This is the idle timer 
            self._timerId = self.startTimer(0) 
            
            
                
        else:
            self.start_btn.setEnabled(True)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
            self.status_msg.setText("Coordinates out of reach")
            self.act_msg.setText("Please choose coordinates")

            self.addx.setText('0')
            self.addy.setText('0')


    def pause_clicked(self):
        self.status_msg.setText("Paused")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.act_msg.setText("Waiting for command")
        #set parameters for the timing the loop generator
        # Stop any existing timer
        if self._timerId is not None:
            self.killTimer(self._timerId)
        self._generator = None
        self._timerId = None
        
        print "Pause clicked"

    def stop_clicked(self):
        self.status_msg.setText("Stoped")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.act_msg.setText("Please choose coordinates")
        #Enter zero values to XY coordinates
        self.addx.setText('0')
        self.addy.setText('0')
        
        disable_arm()
        #set parameters for the timing the loop generator
        # Stop any existing timer
        if self._timerId is not None:
            self.killTimer(self._timerId)
        self._generator = None
        self._timerId = None

        print "Stop clicked"

    def getPos(self, event):
        x = event.pos().x()
        self.addx.setText(str(x))
        y = event.pos().y()
        self.addy.setText(str(y))
        print ("x = ", x,"y = ", y)


    def loopGenerator(self):
        _iterations = 7 #enter the number of iterations
        for a in range(_iterations):
            a+=1

            print "Take picture"
            take_new_picture()
            time.sleep(1)

            print "show picture"
            self.l2.setPixmap(QtGui.QPixmap("Test Image.jpg"))
            time.sleep(1)

            print "locate arm position"
            self._shoulder_pos , self._elbow_pos , self._wrist_pos = get_arm_position()
            time.sleep(1)

            print "check success"
            time.sleep(1)

            print "calculate arm next move"
            time.sleep(1)

            print "command to the servo motors"
            time.sleep(1)

            #"pause" the loop using yield
            yield
        print "The arm did not reach the position after"+str(_iterations)

    
    def timerEvent(self, event):
        # This is called every time the GUI is idle.
        if self._generator is None:
            return
        try:
            next(self._generator)  # Run the next iteration
        except StopIteration:
            self.stop_clicked()  # Iteration has finshed, kill the timer
        



#Allow command line arguments for your app
app = QApplication(sys.argv)
#MMain window
form = Form()
form.show()
# Start the event loop.
app.exec_()