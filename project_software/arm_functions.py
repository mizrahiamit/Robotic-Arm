import RPi.GPIO as IO
import time
import math


def cal_deviation(arm_wrist_pos, x_dest, y_dest):
	return math.hypot(arm_wrist_pos[0] - x_dest, arm_wrist_pos[1] - y_dest)


def cal_next_move(_deviation, _distance, _wrist_pos, _shoulder_pos, _x_pos, _y_pos):
	cover_radius = math.hypot(_wrist_pos[0] - _shoulder_pos[0], _wrist_pos[1] - _shoulder_pos[1]) #The distance between the wirst to the shoulder
	
	if (cover_radius > (_deviation +5)):
		m1_change =  0
		m2_change = -0.5 # -6 degrees

	if (cover_radius < (_deviation -5)):
		m1_change =  0
		m2_change = +0.5 # +6 degrees

	elif (_wrist_pos[1] < (_y_pos-5)):
		m1_change = +0.5 # +6 degrees
		m2_change = 0

	elif (_wrist_pos[1] > (_y_pos+5)):
		m1_change = -0.5 # -6 degrees
		m2_change = 0

	elif (_wrist_pos[0] < _x_pos):
		m1_change = -0.25 # - 3 degrees
		m2_change = 0
	else:
		m1_change = +0.25 # +3 degrees
		m2_change = 0


	return m1_change,m2_change 

