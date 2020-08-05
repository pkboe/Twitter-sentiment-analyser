# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pos.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Postive(object):
    def setupUi(self, Postive):
        Postive.setObjectName("Postive")
        Postive.resize(636, 475)
        Postive.setStyleSheet("background-color: rgb(243, 254, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Postive)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Pos_label = QtWidgets.QLineEdit(Postive)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Pos_label.setFont(font)
        self.Pos_label.setStyleSheet("color: rgb(32, 185, 255);")
        self.Pos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Pos_label.setReadOnly(True)
        self.Pos_label.setObjectName("Pos_label")
        self.verticalLayout.addWidget(self.Pos_label)
        self.Pos_tweet = QtWidgets.QTextEdit(Postive)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pos_tweet.setFont(font)
        self.Pos_tweet.setStyleSheet("color: rgb(27, 161, 218);")
        self.Pos_tweet.setReadOnly(True)
        self.Pos_tweet.setObjectName("Pos_tweet")
        self.verticalLayout.addWidget(self.Pos_tweet)

        self.retranslateUi(Postive)
        QtCore.QMetaObject.connectSlotsByName(Postive)

    def retranslateUi(self, Postive):
        _translate = QtCore.QCoreApplication.translate
        Postive.setWindowTitle(_translate("Postive", "Postive Tweets"))
        self.Pos_label.setText(_translate("Postive", "Postive Tweets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Postive = QtWidgets.QWidget()
    ui = Ui_Postive()
    ui.setupUi(Postive)
    Postive.show()
    sys.exit(app.exec_())
