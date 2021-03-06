#-------------------------------------------------------------------------------
# Name:        Raspberry Pi Camera Controlled XY Robotic Arm
# Purpose:     Electrical engineering project
#
# Author:      Mizrahi Amit
#
# Created:     30/03/2017
# Copyright:   (c) Mizrahi 2017
#-------------------------------------------------------------------------------

import sys
import numpy as np
import cv2



#------------------------------------------------------
def get_color_mask(image,color):
    #return white image with images in the color only
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    if color =='red':
        # define range of red color in HSV
        lower_red = np.array([0,70,50])
        upper_red = np.array([10,255,255])
        # Threshold the HSV image to get only red colors
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        # define range of red color in HSV
        lower_red = np.array([175,70,50])
        upper_red = np.array([180,255,255])
        # Threshold the HSV image to get only red colors
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        mask = cv2.bitwise_or(mask1, mask2, mask = None)

    elif color =='blue':
        # define range of blue color in HSV
        
        lower_blue = np.array([82,20,20])
        upper_blue = np.array([122,255,255])
        
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
    elif color == 'green':
        # define range of green color in HSV
        
        lower_green = np.array([40,130,100])
        upper_green = np.array([65,255,255])
        
        # Threshold the HSV image to get only green colors
        mask = cv2.inRange(hsv, lower_green, upper_green)
    elif color =='yellow':
        # define range of yellow color in HSV
        
        lower_yellow = np.array([15,150,120])
        upper_yellow = np.array([37,255,255])
        
        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    else:
        mask = None

    return  mask

#------------------------------------------------------
def return_circles_values(img):
    img = cv2.medianBlur(img,5)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,200, param1=35,param2=20,minRadius=5,maxRadius=50)
    return circles
#------------------------------------------------------
def detect_circle_by_color(color,image):
    mask = get_color_mask(image,color)
    circles = return_circles_values(mask)
    if circles is None:
        x = None
        y = None
    else:
        x = circles[0][0][0]
        y = circles[0][0][1]

    return x,y

#------------------------------------------------------
def get_arm_position(image):

    pos1 = detect_circle_by_color('yellow',image)#Shoulder
    
    pos2 = detect_circle_by_color('blue',image)#Elobow
    
    pos3 = detect_circle_by_color('green',image)#Wirst
    
    
    return pos1,pos2,pos3











