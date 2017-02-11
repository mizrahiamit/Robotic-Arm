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

	
	grid=QGridLayout()

	grid.addWidget(act_msg,1,1,1,4)

	grid.addWidget(start_btn,2,1,1,1)
	grid.addWidget(pause_btn,2,2,1,1)
	grid.addWidget(stop_btn,2,3,1,1)

	grid.addWidget(QLabel("X_target ="),3,1,1,1)
	grid.addWidget(addx,3,2,1,1)
	grid.addWidget(QLabel("Y_target ="),3,3,1,1)
	grid.addWidget(addy,3,4)

	grid.addWidget(status_msg,4,1,1,4)

	#grid.addWidget(l2,5,1)

	'''
	#------------------------------------------
	vbox=QVBoxLayout()
	vbox.addStretch()
	vbox.addWidget(l2)
	win.setLayout(vbox)
	#------------------------------------------
	'''


	win.setLayout(grid)
	win.setGeometry(100,100,400,1000)
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