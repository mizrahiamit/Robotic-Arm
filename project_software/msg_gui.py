import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


def window():
	app = QApplication(sys.argv)
	w = QWidget()

	msg=QMessageBox()
	msg.setIcon(QMessageBox.Information)
	msg.setText("This is a message box")
	msg.setInformativeText("This is additional information")
	msg.setWindowTitle("MessageBox demo")
	msg.setDetailedText("The details are as follows:")
	msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	msg.buttonClicked.connect(msgbtn)
	retval=msg.exec_()
	print "value of pressed message box button:", retval


	
	w.setWindowTitle("PyQt Dialog demo")
	w.show()
	sys.exit(app.exec_())


def msgbtn(i):
	print "Button pressed is:",i.text()

if __name__ == '__main__':
	window()