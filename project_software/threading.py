import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time

class MainDialog(QDialog):

	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		

		self.process_btn=QtGui.QPushButton()
        self.process_btn.setText("Process")
        self.connect(self.process_btn,SIGNAL("clicked()"),self.processData)

		self.workrThread = WorkrThread()


	def processData(self):
		self.workrThread.start()#call "run" method
		QMessage.information(self,"Done!", "Done.")

class WorkrThread(QThread):

	def __init__(self, parent=None):
		super(WorkrThread, self).__init__(parent)

	def run(self):
		time.sleep(5)
		print "Done with the thread"


#Allow command line arguments for your app
app = QApplication(sys.argv)
#MMain window
form = MainDialog()
form.show()
# Start the event loop.
app.exec_()