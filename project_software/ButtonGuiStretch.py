import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    #---------------------------------------------------
    # Adding Start, Pause & Stop buttons
    fbox = QFormLayout()
    hbox = QHBoxLayout()
    vbox = QVBoxLayout()
    
    start_btn = QPushButton("Start")
    pause_btn = QPushButton("Pause")
    stop_btn = QPushButton("Stop")

    

    hbox.addWidget(start_btn)
    hbox.addStretch()
    hbox.addWidget(pause_btn)
    hbox.addStretch()
    hbox.addWidget(stop_btn)
    
    

    start_btn.clicked.connect(start_clicked)
    QObject.connect(pause_btn,SIGNAL("clicked()"),pause_clicked)
    QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)

    vbox.addStretch()
    #---------------------------------------------------
    # Adding inputs for XY coordinates
    
 '''   

    #l_x=QLabel("X_target =")
    #l_y=QLabel("Y_target =")

    addx = QLineEdit()
    addy = QLineEdit()

    #hbox.addWidget(addx)
    #fbox.addRow(l_x,hbox)

    #hbox.addWidget(addy)
    #fbox.addRow(l_y,hbox)
    

    vbox.addStretch()

    fbox.addRow(QLabel("X_target ="),addx)
    fbox.addRow(QLabel("Y_target ="),addy)
    
    vbox.addStretch()
'''

    win.setLayout(fbox)

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