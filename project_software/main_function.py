import sys
import cv2
import numpy as np
import math
import time

  
def check_coordinates(dest_coor,arm_src_coor,arm_radius):
    #return true if move is possible, else false.
    print "Checking if move is possible"
    #first condition: coordinates must be in the frame 640x480
    if (dest_coor[1] < 640) or (dest_coor[2] < 480) or dest_coor[1] == 0 ) or (dest_coor[2] == 0 ):
        #second condition: coordinates must be in arm region
        delta_x = asb(dest_coor[1]-arm_src_coor[1])
        delta_y = asb(dest_coor[2]-arm_src_coor[2])
        distance = sqrt( pow(delta_y,2) + pow(delta_x,2) )
        if distance< arm_radius :
            return  true
        else:
            return false
    else:
        return false
#------------------------------------------------------
def disable_arm(self):
    #disabling pwm port, to the servo motors.
    print "Disabling arm"
    return true  
#------------------------------------------------------
def robotic_arm_algoritem(self):

    sleep(1)
    print "Take picture"
    sleep(1)
    print "show picture"
    sleep(1)
    print "locate arm position"
    sleep(1)
    print "check success"
    sleep(1)
    print "calculate arm next move"
    sleep(1)
    print "command to the servo motors"

    return true
#------------------------------------------------------