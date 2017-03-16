import cv2
import numpy as np

  
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
        lower_blue = np.array([90,30,0])
        upper_blue = np.array([115,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
    elif color == 'green':
        # define range of green color in HSV
        lower_green = np.array([50,90,90])
        upper_green = np.array([70,255,255])
        # Threshold the HSV image to get only green colors
        mask = cv2.inRange(hsv, lower_green, upper_green)
    elif color =='yellow':
        # define range of yellow color in HSV
        lower_yellow = np.array([20,230,60])
        upper_yellow = np.array([40,255,255])
        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    else:
        mask = None

    return  mask

def return_circles_values(img):
    img = cv2.medianBlur(img,5)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,100, param1=35,param2=20,minRadius=5,maxRadius=50)
    return circles

def draw_circle(img,circles):
    #draw circle by coordinate and radius
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    return img








    
 