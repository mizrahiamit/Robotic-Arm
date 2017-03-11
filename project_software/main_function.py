import sys
import numpy as np
import cv2
import math
import time

from picamera.array import PiRGBArray
import picamera


  
def check_coordinates(dest_coor,arm_src_coor,arm_radius):
    #return true if move is possible, else false.
    print "Checking if move is possible"
    #first condition: coordinates must be in the frame 640x480
    if (dest_coor[0] < 640) or (dest_coor[1] < 480) or (dest_coor[0] == 0 ) or (dest_coor[1] == 0 ):
        #second condition: coordinates must be in arm region
        delta_x = abs(dest_coor[1]-arm_src_coor[0])
        delta_y = abs(dest_coor[1]-arm_src_coor[0])
        distance = math.sqrt( pow(delta_y,2) + pow(delta_x,2) )
        if distance< arm_radius :
            return  True
        else:
            return False
    else:
        return False
#------------------------------------------------------
def disable_arm():
    #disabling pwm port, to the servo motors.
    print "Disabling arm"
    return True 
#------------------------------------------------------
def take_new_picture(_x_pos,_y_pos):
    img = cv2.imread("Test Image.jpg")
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(img)
    cv2.line(img,(_x_pos+5,_y_pos),(_x_pos-5,_y_pos),(255,255,255),50)
    cv2.line(img,(_x_pos,_y_pos+5),(_x_pos,_y_pos-5),(255,255,255),50)
    img = cv2.iwrite("Test Image.jpg")
        
    return True











