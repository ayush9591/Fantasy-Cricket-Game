# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoreboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 244)
        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 201, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(62, 194, 42);")
        self.label.setObjectName("label")
        self.finalscore = QtWidgets.QLabel(Dialog)
        self.finalscore.setGeometry(QtCore.QRect(110, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.finalscore.setFont(font)
        self.finalscore.setStyleSheet("color: rgb(25, 188, 220);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.finalscore.setFrameShape(QtWidgets.QFrame.Box)
        self.finalscore.setLineWidth(2)
        self.finalscore.setAlignment(QtCore.Qt.AlignCenter)
        self.finalscore.setObjectName("finalscore")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Score Board"))
        self.label.setText(_translate("Dialog", "Your Team Score :"))
        self.finalscore.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
