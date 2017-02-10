import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
	app = QApplication(sys.argv)
	win = QDialog()

	start_btn= QPushButton(win)
	start_btn.setText("Start")
	start_btn.move(50,20)
	start_btn.clicked.connect(start_clicked)

	pause_btn=QPushButton(win)
	pause_btn.setText("Pause")
	pause_btn.move(70,20)
	QObject.connect(pause_btn,SIGNAL("clicked()"),pause_clicked)

	stop_btn=QPushButton(win)
	stop_btn.setText("Pause")
	stop_btn.move(90,20)
	QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)

	win.setGeometry(10,10,200,100)
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