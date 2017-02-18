# import the necessary packages
from picamera.array import PiRGBArray
import picamera
import time
import cv2


''' 
# initialize the camera and grab a reference to the raw camera capture
with picamera.PiCamera() as camera:
	rawCapture = PiRGBArray(camera)
 
	# allow the camera to warmup
	time.sleep(2)
 
	# grab an image from the camera
	camera.capture(rawCapture, format="bgr")
	image = rawCapture.array
 
	# display the image on screen and wait for a keypress
	cv2.imshow("Image", image)
	cv2.waitKey(0)
'''
#--------------------------------------------------


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('Test Image.jpg')
