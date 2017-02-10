import cv2
import numpy as np
from huogh_transform_function import *


def main():
    # Take a image
    image = cv2.imread('color_img.jpg')
    image2 = image.copy()
    #---------Detect Red Objects-------------
    r_mask = get_color_mask(image,"red")
    
    #---------Detect Red circle-------------

    circles = return_circles_values(r_mask)
    
    if circles is None:
        print "No circle found"
    else:

        image2 = draw_circle(image2,circles)
        print circles
        
        cv2.imwrite('detected red circles.jpg',image2)
    #---------Detect Green Objects-------------
    b_mask = get_color_mask(image,"green")

    #---------Detect Blue circle-------------
    circles = return_circles_values(b_mask)
    
    if circles is None:
        print "No circle found"

    else:
        image2 = draw_circle(image2,circles)
        print circles
        
        cv2.imwrite('detected circles.jpg',image2)

if (__name__ == "__main__"):
	main()