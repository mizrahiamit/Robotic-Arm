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
- ------------------------Next-------------------------------------
- Read new image every n sec

# Start Raspberry pi
- Open Terminal
- $ arp -a
- Check that bridge connection exists
- $ssh -X pi@192.168.2.8 (bridge I.P)
- Insert password: raspberry
- $source ~/.profile
- $workon cv
- $cd Documents/Robotic-Arm
