import sys
from PySide2.QtWidgets import *
from PySide2 import QtGui,QtCore
from PySide2.QtWidgets import QFrame
from PySide2.QtCore import *
from PySide2.QtGui import *


class MyLabel(QLabel):
    def paintEvent(self, event):
        painter = QPainter(self)

        metrics = QFontMetrics(self.font())
        elided = metrics.elidedText(self.text(), Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)



def error(str):
    msgBox = QMessageBox();
    msgBox.setText(str);
    msgBox.setWindowTitle("Service Engine ")
    msgBox.setWindowIcon((QtGui.QIcon("error.png")))
    QApplication.beep()
    msgBox.exec_()



def clicked():
    if not (sub_window.isHidden()):
        error("Positive Tweets Are Already Opened !")
    elif(sub_window.isHidden()):
        positive_btn.setStyleSheet("background-color: rgb(0, 191, 255);    border-style: inset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
        negative_btn.setStyleSheet("background-color: red;    border-style: outset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
        sub_window.show()
        sub_window2.hide()






def clicked2():
    if not (sub_window2.isHidden()):
        error("Negative Tweets Are Already Opened !")
    elif (sub_window2.isHidden()):
        negative_btn.setStyleSheet("background-color: rgb(0, 191, 255);    border-style: inset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
        positive_btn.setStyleSheet("background-color: Green;    border-style: outset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
        sub_window2.show()
        sub_window.hide()



app = QApplication(sys.argv)
main_window = QMainWindow()
sub_window  =  QLabel()
sub_window2 =  QLabel()
positive_btn = QPushButton("Postive Tweets",main_window)
negative_btn = QPushButton("Negative Tweets",main_window)
main_text = QLabel(main_window)
positive_buffer = "POSITIVE TWEET From Backend."
negative_buffer = "NEGATIVE TWEET From Backend."
scrollArea = QScrollArea()
scrollArea.setBackgroundRole(QPalette.Dark)



main_text.setText("Twitter Sentiment Detector v1.0.0 (Beta*)")
main_text.resize(main_window.width()/1.4,main_window.height()/10)
main_text.setAlignment(Qt.AlignCenter)
main_text.move(0,0)
main_text.setStyleSheet(" color: rgb(0, 191, 255); font: bold 20px; " )

screen = app.primaryScreen()
size = screen.size()
rect = screen.availableGeometry()

avl_width=rect.width()                  #Avilable resol of desktop that can be utiized by softwere.
avl_height=rect.height()

main_window.setWindowTitle("Twitter Sentiment Detector")
main_window.setWindowIcon(QtGui.QIcon("twitter.png"))
main_window.resize(avl_width/3,avl_height/2)

sub_window.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
sub_window.setLineWidth(0)
sub_window.resize(avl_width/3,avl_height/1.2)
sub_window.move(avl_height*1.1,avl_width*0.058)
sub_window.setMidLineWidth(3)
sub_window.setContentsMargins(0,0,0,0)
sub_window.setWindowTitle("Positive Tweets")
sub_window.setStyleSheet("border:5px solid green; font: bold 12px;")
sub_window.setAlignment(Qt.AlignTop)
positive_buffer = positive_buffer + "INITIALIZATION FETCH OF VERY FIRST POSITIVE TWEET."
negative_buffer = negative_buffer + "INITIALIZATION FETCH OF VERY FIRST NEGATIVE TWEET"






sub_window2.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
sub_window2.resize(avl_width/3,avl_height/1.2)
sub_window2.move(avl_height*1.1,avl_width*0.058)
sub_window2.setLineWidth(0)
sub_window2.setMidLineWidth(3)
sub_window2.setContentsMargins(0,0,0,0)
sub_window2.setWindowTitle("Negative Tweets")
sub_window2.setAlignment(Qt.AlignTop)
sub_window2.setStyleSheet("border:5px solid red; font: bold 14px;")


positive_btn.move(main_window.height()/2.6,50)
positive_btn.setStyleSheet("background-color: Green;    border-style: outset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
positive_btn.clicked.connect(clicked)

negative_btn.move(main_window.height()/2.6,100)
negative_btn.setStyleSheet("background-color: red;    border-style: outset;    border-width: 2px;    border-radius: 10px;   border-color: beige;    font: bold 14px;    min-width: 10em;padding: 6px;")
negative_btn.clicked.connect(clicked2)


#############################################################OUTGRAPHING##############################################################################################################################################################

def pos_text (str):
    str=str + "FUNCTION TO FETCH THE TWEET + Call To This Function"
    sub_window.setText(str)

def neg_text (str):
    str=str + "FUNCTION TO FETCH THE TWEET + Call To This "
    sub_window2.setText(str)



pos_text(positive_buffer)
neg_text(negative_buffer)





main_window.show()
app.exec_()
sys.exit()
