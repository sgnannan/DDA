# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\LoadingPointParameters.ui'
#
# Created: Tue May 13 15:57:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LoadPointParameters(object):
    def setupUi(self, LoadPointParameters):
        LoadPointParameters.setObjectName("LoadPointParameters")
        LoadPointParameters.resize(600, 353)
        LoadPointParameters.setMinimumSize(QtCore.QSize(600, 353))
        LoadPointParameters.setMaximumSize(QtCore.QSize(600, 353))
        self.verticalLayout = QtGui.QVBoxLayout(LoadPointParameters)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(LoadPointParameters)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(LoadPointParameters)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadPointParameters)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LoadPointParameters.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LoadPointParameters.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadPointParameters)

    def retranslateUi(self, LoadPointParameters):
        LoadPointParameters.setWindowTitle(QtGui.QApplication.translate("LoadPointParameters", "Load points Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("LoadPointParameters", "Stress for each time", None, QtGui.QApplication.UnicodeUTF8))

