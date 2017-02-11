import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
	app = QApplication(sys.argv)
	win = QWidget()


	#------------------------------------------
	act_msg = QLineEdit()

	#------------------------------------------
	start_btn= QPushButton(win)
	start_btn.setText("Start")
	
	start_btn.clicked.connect(start_clicked)

	pause_btn=QPushButton(win)
	pause_btn.setText("Pause")
	
	QObject.connect(pause_btn,SIGNAL("clicked()"),pause_clicked)

	stop_btn=QPushButton(win)
	stop_btn.setText("Stop")
	
	QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)
	#------------------------------------------
	addx = QLineEdit()
	addy = QLineEdit()
	#------------------------------------------
	status_msg = QLineEdit()
	#------------------------------------------
	l2=QLabel()
	l2.setPixmap(QPixmap("detected circles.jpg"))
	#------------------------------------------
	row = 1
	
	grid=QGridLayout()

	grid.addWidget(QLabel("Action message"),row,1,1,4)

	row=row+1
	grid.addWidget(act_msg,row,1,1,4)

	row=row+1
	grid.addWidget(start_btn,row,1,1,1)
	grid.addWidget(pause_btn,row,2,1,1)
	grid.addWidget(stop_btn,row,3,1,1)

	row=row+1
	grid.addWidget(QLabel("X_target ="),row,1,1,1)
	grid.addWidget(addx,row,2,1,1)
	grid.addWidget(QLabel("Y_target ="),row,3,1,1)
	grid.addWidget(addy,row,4)

	row=row+1
	grid.addWidget(QLabel("Status message"),row,1,1,4)

	row=row+1
	grid.addWidget(status_msg,row,1,1,4)

	row=row+1
	grid.addWidget(QLabel("ROI image"),row,1,1,4)

	row=row+1
	grid.addWidget(l2,row,1,4,3)



	win.setLayout(grid)
	#win.setGeometry(x,y,width,height)
	win.setGeometry(100,100,550,600)
	win.setWindowTitle("Camera Control XY Robotic Arm")
	win.show()
	sys.exit(app.exec_())


def start_clicked():
	print "Start clicked"

def pause_clicked():
	print "Pause clicked"

def stop_clicked():
	print "Stop clicked"

if __name__ == '__main__':
    window()