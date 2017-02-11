import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



def window():
    app = QApplication(sys.argv)
    win = QWidget()
    
    l1=QLabel()
    l2=QLabel()
    l3=QLabel()
    l4=QLabel()
    
    l1.setText("Camera Control XY Robotic Arm")
    l4.setText("<A href='www.TutorialsPoint.com'>TutorialsPoint</a>")
    l2.setText("<a href='#'>welcome to Python GUI Programming</a>")
    
    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)
    l3.setPixmap(QPixmap("detected circles.jpg"))
    
    vbox=QVBoxLayout()
    
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)


    
    l1.setOpenExternalLinks(True)
    l4.linkActivated.connect(clicked)
    l2.linkHovered.connect(hovered)
    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
    win.setLayout(vbox)
    
    win.setWindowTitle("QLabel Demo")
    win.show()
    sys.exit(app.exec_())



def hovered():
    print "hovering"
def clicked():
    print "clicked"

def start_clicked():
    print "Start clicked"

def pause_clicked():
    print "Pause clicked"

def stop_clicked():
    print "Stop clicked"

if __name__ == '__main__':
    window()

    