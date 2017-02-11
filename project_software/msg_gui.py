import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


def window():
	app = QApplication(sys.argv)
	

	msg=QMessageBox()
	msg.setIcon(QMessageBox.Information)
	msg.setText("This is a message box")
	msg.setInformativeText("This is additional information")
	msg.setWindowTitle("MessageBox demo")
	msg.setDetailedText("The details are as follows:")
	msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	msg.buttonClicked.connect(msgbtn)
	
	
	sys.exit(app.exec_())


def msgbtn(i):
	print "Button pressed is:",i.text()

if __name__ == '__main__':
	window()