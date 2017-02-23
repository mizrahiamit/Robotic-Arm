import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

#Output ports
IO.setup(14, IO.OUT)#Conrol Motor1
IO.setup(18, IO.OUT)#Conrol Motor2

#Freq=50Hz
pwm_m1 = IO.PWM(14,50)
pwm_m2 = IO.PWM(18,50)

pwm_m1.start(2.5)#7.5% duty cycle
pwm_m2.start(12.5)#7.5% duty cycle


while 1:
	pwm_m1.ChangeDutyCycle(2.5)
	pwm_m2.ChangeDutyCycle(12.5)
	time.sleep(30)

	pwm_m1.ChangeDutyCycle(7.5)
	pwm_m2.ChangeDutyCycle(7.5)
	time.sleep(30)

	pwm_m1.ChangeDutyCycle(12.5)
	pwm_m2.ChangeDutyCycle(2.5)
	time.sleep(30)

