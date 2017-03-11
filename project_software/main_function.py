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
    # Create the in-memory stream
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # Construct a numpy array from the stream
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    # "Decode" the image from the array, preserving colour
    image = cv2.imdecode(data, 1)
    # OpenCV returns an array with data in BGR order. If you want RGB instead
    # use the following...
    img = image[:, :, ::-1]

    '''
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            camera.resolution = (640, 480)
            #camera.framerate = 24
            camera.start_preview()
            # Camera warm-up time
            time.sleep(2)
            #output = PiRGBArray(camera, size=(640,480))
            #output = np.empty((640, 480, 3), dtype=np.uint8)
            camera.capture(output, 'rgb')
            img = np.frombuffer(output, dtype=np.uint8, count=640*480).reshape(480, 640)
'''
    cv2.line(img,(self._x_pos+5,self._y_pos),(self._x_pos-5,self._y_pos),(255,255,255),50)
    cv2.line(img,(self._x_pos,self._y_pos+5),(self._x_pos,self._y_pos-5),(255,255,255),50)
    cv2.imwrite("Test Image.jpg",img)
        
    return True











