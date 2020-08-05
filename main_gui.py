from PyQt5 import QtCore, QtGui, QtWidgets
from pos import Ui_Postive
from neg import  Ui_Negative
from nut import Ui_Neutral
from Credits import Ui_Credits
from driver import driver
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(777, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(777, 507))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color : black;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(-10, 0, 761, 87))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border : 0px")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background:transparent")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 180, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(62, 191, 255)")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 130, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setUnderline(False)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border : 0px;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 330, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 410, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(420, 320, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border : 0px;")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(410, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border : 0px;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(420, 420, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border : 0px;")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 240, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 34, 93);")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.neg_per = QtWidgets.QLineEdit(self.centralwidget)
        self.neg_per.setGeometry(QtCore.QRect(630, 370, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.neg_per.setFont(font)
        self.neg_per.setStyleSheet("color: rgb(255, 0, 4);")
        self.neg_per.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.neg_per.setText("")
        self.neg_per.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.neg_per.setReadOnly(True)
        self.neg_per.setObjectName("neg_per")
        self.pos_per = QtWidgets.QLineEdit(self.centralwidget)
        self.pos_per.setGeometry(QtCore.QRect(630, 320, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.pos_per.setFont(font)
        self.pos_per.setStyleSheet("color: rgb(12, 255, 0);")
        self.pos_per.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.pos_per.setText("")
        self.pos_per.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pos_per.setReadOnly(True)
        self.pos_per.setObjectName("pos_per")
        self.nut_per = QtWidgets.QLineEdit(self.centralwidget)
        self.nut_per.setGeometry(QtCore.QRect(630, 420, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.nut_per.setFont(font)
        self.nut_per.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.nut_per.setText("")
        self.nut_per.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nut_per.setReadOnly(True)
        self.nut_per.setObjectName("nut_per")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.Form = QtWidgets.QAction(MainWindow)
        self.Form.setCheckable(True)
        self.Form.setObjectName("Form")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionHelp_2 = QtWidgets.QAction(MainWindow)
        self.actionHelp_2.setObjectName("actionHelp_2")
        self.menuFile.addAction(self.actionRestart)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionCredits)
        self.menuAbout.addAction(self.actionHelp_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twitter Sentiment Analyser"))
        self.lineEdit.setText(_translate("MainWindow", "Twitter Sentiment Analyser"))
        self.label.setText(_translate("MainWindow", "Version:1.0"))
        self.pushButton.setText(_translate("MainWindow", "Fetch Tweets"))
        self.lineEdit_3.setText(_translate("MainWindow", "Enter The Topic Or Username To Fetch :"))
        self.checkBox.setText(_translate("MainWindow", "Positive Tweets"))
        self.checkBox_2.setText(_translate("MainWindow", "Negative Tweets"))
        self.checkBox_3.setText(_translate("MainWindow", "Neutral Tweets"))
        self.lineEdit_6.setText(_translate("MainWindow", "Positivity Percentage :"))
        self.lineEdit_7.setText(_translate("MainWindow", "Negativity Percentage :"))
        self.lineEdit_8.setText(_translate("MainWindow", "Neutrality Percentage :"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.Form.setText(_translate("MainWindow", "Form"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionHelp_2.setText(_translate("MainWindow", "Help"))




import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowIcon((QtGui.QIcon("twitter.png")))

Credits = QtWidgets.QWidget()
uic = Ui_Credits()
uic.setupUi(Credits)

Postive = QtWidgets.QWidget()
uip = Ui_Postive()
uip.setupUi(Postive)

Neutral = QtWidgets.QWidget()
uit = Ui_Neutral()
uit.setupUi(Neutral)


Negative = QtWidgets.QWidget()
uin = Ui_Negative()
uin.setupUi(Negative)

def SetPerPos(posper):
    ui.pos_per.setText((posper))

def SetTextPos(String):
    uip.Pos_tweet.setText(String)

def SetPerNeg(negper):
    ui.neg_per.setText((negper))

def SetPerNut(nutper):
    ui.nut_per.setText((nutper))


def SetTextNeg(String):
    uin.neg_tweet.setText(String)


def SetTextNut(String):
    uit.Pos_tweet.setText(String)





def fetch_query_from_gui():
    if (ui.lineEdit_2.text()):
        query = ui.lineEdit_2.text()
        driver(query)
        Postive.show()
        Negative.show()
        Neutral.show()
        set_checkbox_all(True)

    else:
        QtWidgets.QApplication.beep()
        msgBox = QtWidgets.QMessageBox();
        msgBox.setText("Enter The Topic Or Username To Fetch And Try Again!   ");
        msgBox.setWindowTitle("Info")
        msgBox.setWindowIcon((QtGui.QIcon("info.png")))
        msgBox.exec()


def pos_check():
    if(ui.checkBox.isChecked()):
        Postive.show()
    else :
        Postive.close()

def neg_check():
    if(ui.checkBox_2.isChecked()):
        Negative.show()
    else :
        Negative.close()

def nut_check():
    if(ui.checkBox_3.isChecked()):
        Neutral.show()
    else :
        Neutral.close()

def main_close():
    all_sub_close()
    MainWindow.close()
def restart():
    reset_all()
    main_close()
    MainWindow.show()

def all_sub_close():
    Postive.close()
    Negative.close()
    Neutral.close()
    Credits.close()

def reset_all():
    all_sub_close()
    set_checkbox_all(False)
    (ui.lineEdit_2.clear())
    (ui.pos_per.clear())
    (ui.neg_per.clear())
    (ui.nut_per.clear())

def set_checkbox_all(boolValue):
    ui.checkBox.setChecked(boolValue)
    ui.checkBox_2.setChecked(boolValue)
    ui.checkBox_3.setChecked(boolValue)

def openCredits():
    Credits.show()

def open_Help():
    osCommandString = "notepad.exe Help.txt"
    os.system(osCommandString)