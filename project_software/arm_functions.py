'''
Name: arm_functions.py
Author: Mizrahi Amit
Last update:16/3/17
Project: Camera Control XY Robotic Arm
'''


import RPi.GPIO as IO
import time
import math


def cal_deviation(arm_wrist_pos, x_dest, y_dest):
	return math.hypot(arm_wrist_pos[0] - x_dest, arm_wrist_pos[1] - y_dest)


def cal_next_move(_deviation, _distance, _wrist_pos, _shoulder_pos, _x_pos, _y_pos):
	cover_radius = math.hypot(_wrist_pos[0] - _shoulder_pos[0], _wrist_pos[1] - _shoulder_pos[1]) #The distance between the wirst to the shoulder
	
	if (cover_radius > (_deviation +5)):
		m1_change =  0
		m2_change = -0.5 # -9 degrees
		print "motor2 -9 deg"
	'''	
	elif (cover_radius < (_deviation -5)):
		m1_change =  0
		m2_change = +0.3 # +9 degrees ********************************
		print "motor2 +9 deg"
	'''
	elif (_wrist_pos[1] < (_y_pos-5)):
		m1_change = +0.5 # +9 degrees
		m2_change = 0
		print "motor1 +9 deg"

	elif (_wrist_pos[1] > (_y_pos+5)):
		m1_change = -0.5 # -9 degrees
		m2_change = 0
		print "motor1 -9 deg"

	elif (_wrist_pos[0] < _x_pos):
		m1_change = -0.25 # - 4.5 degrees
		m2_change = 0
		print "motor1 -4.5 deg"
	else:
		m1_change = +0.25 # +4.5 degrees
		m2_change = 0
		print "motor1 +4.5 deg"


	return m1_change,m2_change 

