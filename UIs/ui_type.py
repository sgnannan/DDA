# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\type.ui'
#
# Created: Thu May 15 15:00:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 306)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 250, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 190, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 150, 121, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtGui.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 70, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtGui.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(210, 70, 101, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtGui.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(60, 110, 111, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtGui.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(210, 110, 89, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtGui.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(60, 150, 131, 16))
        self.radioButton_7.setObjectName("radioButton_7")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 281, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "HolePoints", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Dialog", "MeasuredPoints", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Dialog", "Joints", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("Dialog", "MaterialLines", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("Dialog", "BoltElements", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_6.setText(QtGui.QApplication.translate("Dialog", "FixPoints", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_7.setText(QtGui.QApplication.translate("Dialog", "LoadingPoints", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Please choose the joint type you chose:", None, QtGui.QApplication.UnicodeUTF8))

