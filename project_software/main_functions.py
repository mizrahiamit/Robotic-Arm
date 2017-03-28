'''
Name: main_functions.py
Author: Mizrahi Amit
Last update:17/3/17
Project: Camera Control XY Robotic Arm
'''

import sys
import numpy as np
import cv2
import math
import time
import io

from picamera.array import PiRGBArray
import picamera

  
def check_coordinates(dest_coor,arm_src_coor,arm_radius):
    #return true if move is possible, else false.
    print "Checking if move is possible"
    distance = math.hypot(dest_coor[0] - arm_src_coor[0], dest_coor[1] - arm_src_coor[1])
    print "the distance is - ", distance
    # check if the destination is in the smaller than the radius of the arm 
    # and on the right of the arm.
    if (distance < arm_radius) and (dest_coor[0] > arm_src_coor[0]):
        return distance
    else:
        return 600
        
    

#------------------------------------------------------
def take_new_picture(_x_pos,_y_pos):
    # Create the in-memory stream
    
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # Construct a numpy array from the stream
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    # "Decode" the image from the array, preserving colour
    image = cv2.imdecode(data, 1)
    

    # OpenCV returns an array with data in BGR order. If you want RGB instead
    if (_x_pos!=0) or (_y_pos!=0):
        cv2.line(image,(_x_pos+10,_y_pos),(_x_pos-10,_y_pos),(0,0,255),1)
        cv2.line(image,(_x_pos,_y_pos+10),(_x_pos,_y_pos-10),(0,0,255),1)

    cv2.imwrite("Test Image.jpg",image)
      
    return newImage

def print_miss(_shoulder_miss,_elbow_miss,_wrist_miss):
    print "Miss detect yellow circel : ",_shoulder_miss
    print "Miss detect blue circel : ",_elbow_miss
    print "Miss detect green circel : ",_wrist_miss
    return True









