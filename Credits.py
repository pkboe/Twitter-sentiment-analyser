# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Credits.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Credits(object):
    def setupUi(self, Credits):
        Credits.setObjectName("Credits")
        Credits.resize(234, 164)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Credits.sizePolicy().hasHeightForWidth())
        Credits.setSizePolicy(sizePolicy)
        Credits.setMinimumSize(QtCore.QSize(173, 162))
        Credits.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Credits)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Cred_label = QtWidgets.QLineEdit(Credits)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Cred_label.setFont(font)
        self.Cred_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Cred_label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border : 0px")
        self.Cred_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cred_label.setReadOnly(True)
        self.Cred_label.setObjectName("Cred_label")
        self.verticalLayout.addWidget(self.Cred_label)
        self.cred_view = QtWidgets.QTextEdit(Credits)
        self.cred_view.setMaximumSize(QtCore.QSize(216, 116))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cred_view.setFont(font)
        self.cred_view.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cred_view.setReadOnly(True)
        self.cred_view.setObjectName("cred_view")
        self.verticalLayout.addWidget(self.cred_view)

        self.retranslateUi(Credits)
        QtCore.QMetaObject.connectSlotsByName(Credits)

    def retranslateUi(self, Credits):
        _translate = QtCore.QCoreApplication.translate
        Credits.setWindowTitle(_translate("Credits", "Form"))
        self.Cred_label.setText(_translate("Credits", "Credits"))
        self.cred_view.setHtml(_translate("Credits", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Liberation Sans\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; text-decoration: underline;\">Pranil Kharche</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; text-decoration: underline;\">Yadnyesh Mulay</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; text-decoration: underline;\">Nitish Didolkar</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; text-decoration: underline;\">Aadesh Jadhav</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Credits = QtWidgets.QWidget()
    ui = Ui_Credits()
    ui.setupUi(Credits)
    Credits.show()
    sys.exit(app.exec_())
