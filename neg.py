# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'neg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Negative(object):
    def setupUi(self, Negative):
        Negative.setObjectName("Negative")
        Negative.resize(636, 449)
        Negative.setStyleSheet("background-color: rgb(243, 254, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Negative)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Neg_label = QtWidgets.QLineEdit(Negative)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Neg_label.setFont(font)
        self.Neg_label.setStyleSheet("color: rgb(255, 0, 115);")
        self.Neg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Neg_label.setReadOnly(True)
        self.Neg_label.setObjectName("Neg_label")
        self.verticalLayout.addWidget(self.Neg_label)
        self.neg_tweet = QtWidgets.QTextEdit(Negative)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.neg_tweet.setFont(font)
        self.neg_tweet.setStyleSheet("color : rgb(234, 0, 93);")
        self.neg_tweet.setReadOnly(True)
        self.neg_tweet.setObjectName("neg_tweet")
        self.verticalLayout.addWidget(self.neg_tweet)

        self.retranslateUi(Negative)
        QtCore.QMetaObject.connectSlotsByName(Negative)

    def retranslateUi(self, Negative):
        _translate = QtCore.QCoreApplication.translate
        Negative.setWindowTitle(_translate("Negative", "Negative Tweets"))
        self.Neg_label.setText(_translate("Negative", "Negative Tweets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Negative = QtWidgets.QWidget()
    ui = Ui_Negative()
    ui.setupUi(Negative)
    Negative.show()
    sys.exit(app.exec_())
