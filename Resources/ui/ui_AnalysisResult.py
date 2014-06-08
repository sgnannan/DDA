# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Projects/QtCreator/DDA_UIs/AnalysisResult.ui'
#
# Created: Fri Mar 21 18:27:13 2014
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 219)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 180, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 291, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 271, 16))
        self.label.setObjectName("label")
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 51, 261, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_displacement = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_displacement.setObjectName("checkBox_displacement")
        self.verticalLayout.addWidget(self.checkBox_displacement)
        self.checkBox_MP = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_MP.setObjectName("checkBox_MP")
        self.verticalLayout.addWidget(self.checkBox_MP)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_stress = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_stress.setObjectName("checkBox_stress")
        self.horizontalLayout.addWidget(self.checkBox_stress)
        self.spinBox_No = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_No.setMinimumSize(QtCore.QSize(0, 20))
        self.spinBox_No.setObjectName("spinBox_No")
        self.horizontalLayout.addWidget(self.spinBox_No)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBox_useExistingData = QtGui.QCheckBox(Dialog)
        self.checkBox_useExistingData.setGeometry(QtCore.QRect(10, 150, 241, 16))
        self.checkBox_useExistingData.setCheckable(True)
        self.checkBox_useExistingData.setChecked(True)
        self.checkBox_useExistingData.setObjectName("checkBox_useExistingData")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Choose the data you want to analyses.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_displacement.setText(QtGui.QApplication.translate("Dialog", "Analyses displacement for each step", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_MP.setText(QtGui.QApplication.translate("Dialog", "Analyses measured points movement.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stress.setText(QtGui.QApplication.translate("Dialog", "Analyses stress for block :", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_useExistingData.setText(QtGui.QApplication.translate("Dialog", "Use analysis data already extracted", None, QtGui.QApplication.UnicodeUTF8))

