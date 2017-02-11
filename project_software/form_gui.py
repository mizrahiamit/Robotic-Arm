import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

       


        #------------------------------------------
        self.act_msg = QLineEdit()
        self.act_msg.setObjectName("act_msg")
        self.act_msg.setText("Stand by")
        #------------------------------------------
        self.start_btn= QPushButton()
        self.start_btn.setText("Start")
        
        self.start_btn.clicked.connect(start_clicked)

        self.pause_btn=QPushButton()
        self.pause_btn.setText("Pause")
        
        QObject.connect(pause_btn,SIGNAL("clicked()"),pause_clicked)

        self.stop_btn=QPushButton()
        self.stop_btn.setText("Stop")
        
        QObject.connect(stop_btn,SIGNAL("clicked()"),stop_clicked)
        #------------------------------------------
        self.addx = QLineEdit()
        self.addy = QLineEdit()
        #------------------------------------------
        self.status_msg = QLineEdit()
        self.status_msg.setObjectName("status_msg")
        self.status_msg.setText("Stand by")
        #------------------------------------------
        self.l2=QLabel()
        self.l2.setPixmap(QPixmap("detected circles.jpg"))
        #------------------------------------------
        row = 1
        
        grid=QGridLayout()

        grid.addWidget(QLabel("Action message"),row,1,1,4)

        row=row+1
        grid.addWidget(self.act_msg,row,1,1,4)

        row=row+1
        grid.addWidget(self.start_btn,row,1,1,1)
        grid.addWidget(self.pause_btn,row,2,1,1)
        grid.addWidget(self.stop_btn,row,3,1,1)

        row=row+1
        grid.addWidget(QLabel("X_target ="),row,1,1,1)
        grid.addWidget(self.addx,row,2,1,1)
        grid.addWidget(QLabel("Y_target ="),row,3,1,1)
        grid.addWidget(self.addy,row,4,1,1)

        row=row+1
        grid.addWidget(QLabel("Status message"),row,1,1,4)

        row=row+1
        grid.addWidget(self.status_msg,row,1,1,4)

        row=row+1
        grid.addWidget(QLabel("ROI image"),row,1,1,4)

        row=row+1
        grid.addWidget(self.l2,row,1,8,6)



        self.setLayout(grid)
        #win.setGeometry(x,y,width,height)
        self.setGeometry(100,100,600,350)
        self.setWindowTitle("Camera Control XY Robotic Arm")



        self.setWindowTitle("Learning")

    def start_clicked():
        self.status_msg("Start clicked")
        print "Start clicked"

    def pause_clicked():
        self.status_msg("Pause clicked")
        print "Pause clicked"

    def stop_clicked():
        self.status_msg("Stop clicked")
        print "Stop clicked"


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()