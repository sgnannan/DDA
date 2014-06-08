# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\WaterControlPoint.ui'
#
# Created: Tue May 13 15:57:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(220, 151)
        Dialog.setMinimumSize(QtCore.QSize(220, 151))
        Dialog.setMaximumSize(QtCore.QSize(220, 151))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 110, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 201, 81))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.XSpinB = QtGui.QDoubleSpinBox(self.groupBox)
        self.XSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.XSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.XSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XSpinB.setDecimals(6)
        self.XSpinB.setMinimum(-999999999.0)
        self.XSpinB.setMaximum(999999999.0)
        self.XSpinB.setObjectName("XSpinB")
        self.gridLayout.addWidget(self.XSpinB, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.YSpinB = QtGui.QDoubleSpinBox(self.groupBox)
        self.YSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.YSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.YSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YSpinB.setDecimals(6)
        self.YSpinB.setMinimum(-999999999.0)
        self.YSpinB.setMaximum(999999999.0)
        self.YSpinB.setObjectName("YSpinB")
        self.gridLayout.addWidget(self.YSpinB, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Y:", None, QtGui.QApplication.UnicodeUTF8))

