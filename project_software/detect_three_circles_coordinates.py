import cv2
import numpy as np
from huogh_transform_function import *


def main():
    # Take a image
    image = cv2.imread('two circles.jpg')
    image2 = image.copy()
    #---------Detect Blue Objects-------------
    r_mask = get_color_mask(image,"blue")
    
    #---------Detect Blue circle-------------

    circles = return_circles_values(r_mask)
    
    if circles is None:
        print "No circle found"
    else:

        image2 = draw_circle(image2,circles)
        print circles
        
        cv2.imwrite('detected blue circles.jpg',image2)
    #---------Detect Green Objects-------------
    b_mask = get_color_mask(image,"green")

    #---------Detect Green circle-------------
    circles = return_circles_values(b_mask)
    
    if circles is None:
        print "No circle found"

    else:
        image2 = draw_circle(image2,circles)
        print circles
        
        cv2.imwrite('detected green circles.jpg',image2)
    #---------Detect Yellow Objects-------------
    b_mask = get_color_mask(image,"yellow")

    #---------Detect Yellow circle-------------
    circles = return_circles_values(b_mask)
    
    if circles is None:
        print "No circle found"

    else:
        image2 = draw_circle(image2,circles)
        print circles
        
        cv2.imwrite('detected yellow circles.jpg',image2)

if (__name__ == "__main__"):
	main()