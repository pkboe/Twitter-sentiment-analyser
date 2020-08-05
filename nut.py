# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nut.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Neutral(object):
    def setupUi(self, Neutral):
        Neutral.setObjectName("Neutral")
        Neutral.resize(636, 475)
        Neutral.setStyleSheet("background-color: rgb(243, 254, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Neutral)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Nut_label = QtWidgets.QLineEdit(Neutral)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Nut_label.setFont(font)
        self.Nut_label.setStyleSheet("color: black;")
        self.Nut_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Nut_label.setReadOnly(True)
        self.Nut_label.setObjectName("Nut_label")
        self.verticalLayout.addWidget(self.Nut_label)
        self.Pos_tweet = QtWidgets.QTextEdit(Neutral)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pos_tweet.setFont(font)
        self.Pos_tweet.setStyleSheet("color: black;")
        self.Pos_tweet.setReadOnly(True)
        self.Pos_tweet.setObjectName("Pos_tweet")
        self.verticalLayout.addWidget(self.Pos_tweet)

        self.retranslateUi(Neutral)
        QtCore.QMetaObject.connectSlotsByName(Neutral)

    def retranslateUi(self, Neutral):
        _translate = QtCore.QCoreApplication.translate
        Neutral.setWindowTitle(_translate("Neutral", "Neutral Tweets"))
        self.Nut_label.setText(_translate("Neutral", "Neutral Tweets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Neutral = QtWidgets.QWidget()
    ui = Ui_Neutral()
    ui.setupUi(Neutral)
    Neutral.show()
    sys.exit(app.exec_())
