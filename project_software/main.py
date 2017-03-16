'''
Name: main.py
Author: Mizrahi Amit
Last update:16/3/17
Project: Camera Control XY Robotic Arm
'''
# Only needed for access to command line arguments

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QWidget, QHBoxLayout, QLabel, QPushButton)

import RPi.GPIO as IO

from main_function import *
from image_processing_functions import *
from arm_functions import *


class Form(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(Form, self).__init__(parent, **kwargs)

        self._iterations = 100 #enter the number of MAX iterations
        self._error_miss_detection = 10# Max iterations that the program don't detect the arm
        #set parameters for the timing the loop generator
        self._generator = None
        self._timerId = None
        #------------------------------------------
        #Arm position parameters 
        self._shoulder_pos = None,None
        self._elbow_pos = None,None
        self._wrist_pos = None,None

        self._arm_radius = 0.00
        #------------------------------------------
        #Target Coordinates
        self._x_pos = 0
        self._y_pos = 0
        #------------------------------------------
        #------------------------------------------
        #------------------------------------------
        #Servo configuration
        IO.setwarnings(False)
        IO.setmode(IO.BCM)

        #Output ports
        IO.setup(14, IO.OUT)#Conrol Motor1
        IO.setup(18, IO.OUT)#Conrol Motor2

        #Freq=50Hz
        self.pwm_m1 = IO.PWM(14,50)
        self.pwm_m2 = IO.PWM(18,50)

        self.m1_dc = 7.5 #7.5% duty cycle - 90 degrees
        self.m2_dc = 12.5 #12.5% duty cycle - 180 degrees

        self.pwm_m1.start(self.m1_dc)
        self.pwm_m2.start(self.m2_dc)
        #------------------------------------------
        #Arm configuration
        self._deviation = 640.0 #The distance between the wirst to destination
        #self._cover_radius = 640.0 #The distance between the wirst to the shoulder
        self._distance = 0 #the distance between the shoulder to the destination
        #------------------------------------------
        #------------------------------------------
        #------------------------------------------
        #Msg that tell the user what the next move
        self.act_msg = QtGui.QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Please choose coordinates")
        #------------------------------------------
        #Start button
        self.check_btn= QtGui.QPushButton()
        self.check_btn.setText("Check system")
        self.connect(self.check_btn,SIGNAL("clicked()"),self.check_clicked)
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
        self.start_btn.setEnabled(False)
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


    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    def check_clicked(self):
        print "taking new picture"
        take_new_picture(0,0)
        print "get arm position"
        self._shoulder_pos,self._elbow_pos,self._wrist_pos=get_arm_position()
        print self._shoulder_pos
        print self._elbow_pos
        print self._wrist_pos
        
        if (self._shoulder_pos==(None,None)) or (self._elbow_pos==(None,None)) or (self._wrist_pos==(None,None)):  
            print "Robotic arm was not recognized "
            self.act_msg.setText("Please try again")
            self.status_msg.setText("Robotic arm was not recognized")
            return False
        else:
            print "Robotic arm was recognized"
            self._arm_radius = math.hypot(self._wrist_pos[0] - self._shoulder_pos[0], self._wrist_pos[1] - self._shoulder_pos[1])
            print "radius", self._arm_radius
            self.start_btn.setEnabled(True)
            self.l2.setPixmap(QtGui.QPixmap("Test Image.jpg"))
            self.act_msg.setText("Please choose coordinates")
            self.status_msg.setText("Setup is ready")
            return True
    #------------------------------------------------------------
    def start_clicked(self,bool):
        self.status_msg.setText("Start clicked")
        print "Start clicked"
        
        dst_coordinate = self._x_pos , self._y_pos
        src_coordinate = self._shoulder_pos
        radius = self._arm_radius 

        self._distance = check_coordinates(dst_coordinate,src_coordinate,radius)
        if(self._distance != 600):
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

    #------------------------------------------------------------
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
    #------------------------------------------------------------
    def stop_clicked( self, _str="Stoped"):
        self.status_msg.setText(_str)
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.act_msg.setText("Please choose coordinates")
        #Enter zero values to XY coordinates
        self.addx.setText('0')
        self._x_pos = 0
        self.addy.setText('0')
        self._y_pos = 0
        self._error_miss_detection = 10
        
        #set parameters for the timing the loop generator
        # Stop any existing timer
        if self._timerId is not None:
            self.killTimer(self._timerId)
        self._generator = None
        self._timerId = None

        print "Stop clicked"

    #------------------------------------------------------------
    #------------------------------------------------------------
    def getPos(self, event):
        self._x_pos = event.pos().x()
        self.addx.setText(str(self._x_pos))
        self._y_pos = event.pos().y()
        self.addy.setText(str(self._y_pos))
        print ("x = ", self._x_pos,"y = ", self._y_pos)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    def loopGenerator(self):
        
        for a in range(self._iterations):
            a+=1
            #/////////////////////////////////////////////////
            print "Take picture"
            take_new_picture(self._x_pos,self._y_pos)
            
            #/////////////////////////////////////////////////
            print "show picture"
            self.l2.setPixmap(QtGui.QPixmap("Test Image.jpg"))
            
            #/////////////////////////////////////////////////
            print "locate arm position"
            self._shoulder_pos , self._elbow_pos , self._wrist_pos = get_arm_position()
            print self._shoulder_pos
            print self._elbow_pos
            print self._wrist_pos

            if (self._shoulder_pos[0] == None) or (self._elbow_pos[0] == None) or (self._wrist_pos[0] == None):
                print "miss detection"
                self._error_miss_detection = self._error_miss_detection - 1
                print "error miss detection left : ",self._error_miss_detection
                if (self._error_miss_detection == 0):
                    print "too many miss detection"
                    self.stop_clicked("Error: Problem to detect arm")
            else:
                #/////////////////////////////////////////////////
                print "check success"
                self._deviation = cal_deviation(self._wrist_pos, self._x_pos, self._y_pos)
                if (self._deviation < 5):
                    #self.status_msg.setText("Success")
                    time.sleep(30)
                    self.stop_clicked("Success")
                    
                    break
                
                #/////////////////////////////////////////////////
                print "calculate arm next move"
                m1_change,m2_change = cal_next_move(self._distance, self._wrist_pos, self._shoulder_pos, self._x_pos, self._y_pos)
                self.m1_dc = self.m1_dc + m1_change
                self.m2_dc = self.m2_dc + m2_change
                
                #/////////////////////////////////////////////////
                print "command to the servo motors"
                print "motor 1 duty cycle: ",self.m1_dc
                print "motor 2 duty cycle: ",self.m2_dc
                self.pwm_m1.ChangeDutyCycle(self.m1_dc)
                self.pwm_m2.ChangeDutyCycle(self.m2_dc)
            

            #"pause" the loop using yield
            yield
        print "The arm did not reach the position after :    "+str(self._iterations)

    #------------------------------------------------------------
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