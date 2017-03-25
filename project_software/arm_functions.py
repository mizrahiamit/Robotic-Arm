'''
Name: arm_functions.py
Author: Mizrahi  Amit
Last update:16/3/17
Project: Camera Control XY Robotic Arm
'''
import RPi.GPIO as IO
import time
import math


def cal_deviation(arm_wrist_pos, x_dest, y_dest):

	print "arm_wrist_pos[0]  ",arm_wrist_pos[0]
	print "x_dest  " ,x_dest
	print "arm_wrist_pos[1]  ",arm_wrist_pos[1]
	print "y_dest  ",y_dest
	
	return math.hypot(arm_wrist_pos[0] - x_dest, arm_wrist_pos[1] - y_dest)


def cal_next_move(_distance, _wrist_pos, _shoulder_pos, _x_pos, _y_pos):
	cover_radius = math.hypot(_wrist_pos[0] - _shoulder_pos[0], _wrist_pos[1] - _shoulder_pos[1]) #The distance between the wirst to the shoulder
	
	if (cover_radius > (_distance+15)):
		print cover_radius," > ",_distance
		m1_change =  0
		m2_change = -1 
		print "motor2 -9 deg"

	elif (cover_radius < (_distance-15)):
		print cover_radius," < ",_distance
		m1_change =  0
		m2_change = +1 
		print "motor2 +9 deg"
	elif (cover_radius > (_distance+10)):
		print cover_radius," > ",_distance
		m1_change =  0
		m2_change = -0.5 
		print "motor2 -9 deg"

	elif (cover_radius < (_distance-10)):
		print cover_radius," < ",_distance
		m1_change =  0
		m2_change = +0.5 
		print "motor2 +9 deg"

	elif (_wrist_pos[1] < (_y_pos-15)):
		print _wrist_pos[1]," < ",_y_pos
		m1_change = -0.5 # -4.5 degrees
		m2_change = 0
		print "motor1 -4.5 deg"

	elif (_wrist_pos[1] > (_y_pos+15)):
		print _wrist_pos[1]," > ",_y_pos
		m1_change = +0.5 # +4.5 degrees
		m2_change = 0
		print "motor1 +4.5 deg"

	elif (_wrist_pos[1] < (_y_pos-5)):
		print _wrist_pos[1]," < ",_y_pos
		m1_change = -0.10 # -4.5 degrees
		m2_change = 0
		print "motor1 -4.5 deg"

	elif (_wrist_pos[1] > (_y_pos+5)):
		print _wrist_pos[1]," > ",_y_pos
		m1_change = +0.10 # +4.5 degrees
		m2_change = 0
		print "motor1 +4.5 deg"

	elif (_wrist_pos[0] < _x_pos-5):
		print _wrist_pos[0]," < ",_x_pos
		m1_change = -0.05 # - 4.5 degrees
		m2_change = +0.05
		print "motor1 -4.5 deg"
	else:
		print _wrist_pos[0]," > ",_x_pos
		m1_change = +0.05 # +4.5 degrees
		m2_change = -0.05
		print "motor1 +4.5 deg"


	return m1_change,m2_change 

