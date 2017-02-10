import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
	app = QApplication(sys.argv)
	win = QWidget()

    start_btn = QPushButton("Start")
    pause_btn = QPushButton("Pause")
    stop_btn = QPushButton("Stop")

    vbox = QVBoxLayout()
    vbox.addWidget(start_btn)
    vbox.addStretch()
    vbox.addWidget(pause_btn)
    vbox.addStretch()
    vbox.addWidget(stop_btn)
    win.setLayout(vbox)


	win.setWindowTitle("PyQt")
	win.show()
	sys.exit(app.exec_())


'''def start_clicked():
	print "Start clicked"

def pause_clicked():
	print "Pause clicked"

def stop_clicked():
	print "Stop clicked"'''

if __name__ == '__main__':
window()