import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
def window():
app = QApplication(sys.argv)
w = QWidget()
b= QPushButton(w)
b.setText("Show message!")
b.move(50,50)
b.clicked.connect(showdialog)
w.setWindowTitle("PyQt Dialog demo")