import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import SIGNAL


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    start_btn = QPushButton("Start")
    pause_btn = QPushButton("Pause")
    stop_btn = QPushButton("Stop")

    box = QHBoxLayout()

    box.addWidget(start_btn)
    box.addStretch()
    box.addWidget(pause_btn)
    box.addStretch()
    box.addWidget(stop_btn)

    win.setLayout(box)

    start_btn.clicked.connect(start_clicked)
    QObject.connect(pause_btn,SIGNAL("clicked()"),pause_clicked)
    QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)

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