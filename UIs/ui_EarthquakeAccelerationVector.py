# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\EarthquakeAccelerationVector.ui'
#
# Created: Tue May 13 15:57:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EarthquakeAccelerationVector(object):
    def setupUi(self, EarthquakeAccelerationVector):
        EarthquakeAccelerationVector.setObjectName("EarthquakeAccelerationVector")
        EarthquakeAccelerationVector.resize(238, 175)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EarthquakeAccelerationVector.sizePolicy().hasHeightForWidth())
        EarthquakeAccelerationVector.setSizePolicy(sizePolicy)
        EarthquakeAccelerationVector.setMinimumSize(QtCore.QSize(238, 175))
        EarthquakeAccelerationVector.setMaximumSize(QtCore.QSize(238, 175))
        self.buttonBox = QtGui.QDialogButtonBox(EarthquakeAccelerationVector)
        self.buttonBox.setGeometry(QtCore.QRect(0, 130, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtGui.QGroupBox(EarthquakeAccelerationVector)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 211, 101))
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
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.ZSpinB = QtGui.QDoubleSpinBox(self.groupBox)
        self.ZSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.ZSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ZSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ZSpinB.setDecimals(6)
        self.ZSpinB.setMinimum(-999999999.0)
        self.ZSpinB.setMaximum(999999999.0)
        self.ZSpinB.setObjectName("ZSpinB")
        self.gridLayout.addWidget(self.ZSpinB, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(EarthquakeAccelerationVector)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EarthquakeAccelerationVector.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EarthquakeAccelerationVector.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EarthquakeAccelerationVector.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EarthquakeAccelerationVector.reject)
        QtCore.QMetaObject.connectSlotsByName(EarthquakeAccelerationVector)

    def retranslateUi(self, EarthquakeAccelerationVector):
        EarthquakeAccelerationVector.setWindowTitle(QtGui.QApplication.translate("EarthquakeAccelerationVector", "Earthquake Acceleration Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("EarthquakeAccelerationVector", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EarthquakeAccelerationVector", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EarthquakeAccelerationVector", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EarthquakeAccelerationVector", "Z:", None, QtGui.QApplication.UnicodeUTF8))

