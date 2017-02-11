import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
	app = QApplication(sys.argv)
	win = QWidget()


	#------------------------------------------
	l1=QLabel("Camera Control XY Robotic Arm")
	l1.setAlignment(Qt.AlignCenter)
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
	stop_btn.setText("Pause")
	
	QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)
	#------------------------------------------
	addx = QLineEdit()
	addy = QLineEdit()
    #------------------------------------------
    status_msg = QLineEdit()
    #------------------------------------------
    l2.setPixmap(QPixmap("detected circles.jpg"))
    #------------------------------------------

	
	vbox=QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(act_msg)
    vbox.addStretch()
    
    

	grid=QGridLayout()

	grid.addWidget(start_btn,1,1)
	grid.addWidget(pause_btn,1,2)
	grid.addWidget(stop_btn,1,3)

	grid.addWidget(QLabel("X_target ="),2,1)
	grid.addWidget(addx,2,2)
	grid.addWidget(addy,2,3)
	grid.addWidget(QLabel("X_target ="),2,4)

    win.setLayout(grid)

    vbox.addStretch()
    vbox.addWidget(status_msg)
    vbox.addStretch()
    vbox.addWidget(l2)


    win.setLayout(vbox)
	'''
	for i in range(1,5):
		for j in range(1,5):
			grid.addWidget(QPushButton("B"+str(i)+str(j)),i,j)
	'''
	
	
	#win.setGeometry(100,100,200,100)
	win.setWindowTitle("PyQt")
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