import sys


from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *#(Qt, SIGNAL, QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
from PyQt4.QtGui import *#(QApplication, QDialog, QHBoxLayout, QLabel, QPushButton)

import time

class Form(QDialog):
    def __init__(self, parent=None):
        #Allow Qt to set up the object.
        super(Form, self).__init__(parent)

        layout = QVBoxLayout()

        self.process_btn=QtGui.QPushButton()
        self.process_btn.setText("Process")
        self.connect(self.process_btn,SIGNAL("clicked()"),self.processData)
        layout.addWidget(self.process_btn)
        
        #self.workrThread = WorkrThread()

    def processData(self):
		#self.workrThread.start()#call "run" method
		self.msg=QtGui.QMessageBox()
		self.msg.setInformativeText("Done!", "Done.")
'''
class WorkrThread(QThread):

	def __init__(self, parent=None):
		super(WorkrThread, self).__init__(parent)

	def run(self):
		time.sleep(5)
		print "Done with the thread"
'''

#Allow command line arguments for your app
app = QApplication(sys.argv)
#MMain window
form = Form()
form.show()
# Start the event loop.
app.exec_()