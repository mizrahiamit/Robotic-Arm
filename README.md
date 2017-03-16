# Robotic-Arm
Description Camera control XY Robotic arm

# Stages
- Build a shield to the Raspberry pi
- Install Raspbian on SD card
- Install Python + OpenCV
- Open a new project on GitHub
- Install PyQt4
- Install Picamera
- Writing a program to take a picture
- Writing a program to find colored circles on a arm (coordinates)
- Writing a GUI
- Display a picture in the GUI
- Get pixel coordinate by clicking right click on the mouse
- Plan Block diagram to the software
- function robotic_arm_algoritem runs in loop after start_clicked->obotic_arm_algoritem()
  and stop after stop btn or pause btn pressed
- Read new image every n sec and show on GUI
- Detect arm position every iteration
- Show target coordinate on the image
- Check if target coor. in arm work range (By radious)
- Calculate arm next move (pwm)
- Check for sucess
- Add error after N max iterations
- Check at the begining for arm recognition(3 points)
- ------------------------Next-------------------------------------
- Organize Code


# Start Raspberry pi
- Open Terminal
- $ arp -a
- Check that bridge connection exists
- $ssh -X pi@192.168.2.8 (bridge I.P)
- Insert password: raspberry
- $source ~/.profile
- $workon cv
- $cd Documents/Robotic-Arm
