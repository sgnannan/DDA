# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\boltElement.ui'
#
# Created: Thu May 15 15:00:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_parameters(object):
    def setupUi(self, parameters):
        parameters.setObjectName("parameters")
        parameters.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(parameters)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(parameters)
        self.label.setGeometry(QtCore.QRect(80, 100, 150, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(parameters)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 150, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(parameters)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 150, 20))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtGui.QDoubleSpinBox(parameters)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 100, 91, 22))
        self.doubleSpinBox.setMaximum(999999.99)
        self.doubleSpinBox.setProperty("value", 16889.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(parameters)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(230, 150, 91, 22))
        self.doubleSpinBox_2.setMaximum(999999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(parameters)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(230, 200, 91, 22))
        self.doubleSpinBox_3.setMaximum(999999.99)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_4 = QtGui.QLabel(parameters)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 351, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(parameters)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 351, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(parameters)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 351, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(parameters)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), parameters.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), parameters.reject)
        QtCore.QMetaObject.connectSlotsByName(parameters)

    def retranslateUi(self, parameters):
        parameters.setWindowTitle(QtGui.QApplication.translate("parameters", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("parameters", "elasticity modulus:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("parameters", "extension strength :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("parameters", "Prestress :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("parameters", "Please enter the parameters for elasticity modulus,", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("parameters", "extension strength, and prestress, please don\'t change the", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("parameters", "defalt empirical value if you are not familiar about it:", None, QtGui.QApplication.UnicodeUTF8))

