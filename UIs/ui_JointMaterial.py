# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\JointMaterial.ui'
#
# Created: Tue May 13 15:57:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_JointMaterial(object):
    def setupUi(self, JointMaterial):
        JointMaterial.setObjectName("JointMaterial")
        JointMaterial.resize(284, 141)
        JointMaterial.setMinimumSize(QtCore.QSize(284, 141))
        JointMaterial.setMaximumSize(QtCore.QSize(284, 141))
        self.verticalLayout = QtGui.QVBoxLayout(JointMaterial)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.FrictionSpinB = QtGui.QDoubleSpinBox(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrictionSpinB.sizePolicy().hasHeightForWidth())
        self.FrictionSpinB.setSizePolicy(sizePolicy)
        self.FrictionSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.FrictionSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FrictionSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FrictionSpinB.setDecimals(6)
        self.FrictionSpinB.setMinimum(-999999999.0)
        self.FrictionSpinB.setMaximum(999999999.0)
        self.FrictionSpinB.setObjectName("FrictionSpinB")
        self.gridLayout.addWidget(self.FrictionSpinB, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.extensionSpinB = QtGui.QDoubleSpinBox(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extensionSpinB.sizePolicy().hasHeightForWidth())
        self.extensionSpinB.setSizePolicy(sizePolicy)
        self.extensionSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.extensionSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.extensionSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.extensionSpinB.setDecimals(6)
        self.extensionSpinB.setMinimum(-999999999.0)
        self.extensionSpinB.setMaximum(999999999.0)
        self.extensionSpinB.setObjectName("extensionSpinB")
        self.gridLayout.addWidget(self.extensionSpinB, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.CohesionSpinB = QtGui.QDoubleSpinBox(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CohesionSpinB.sizePolicy().hasHeightForWidth())
        self.CohesionSpinB.setSizePolicy(sizePolicy)
        self.CohesionSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.CohesionSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CohesionSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CohesionSpinB.setDecimals(6)
        self.CohesionSpinB.setMinimum(-999999999.0)
        self.CohesionSpinB.setMaximum(999999999.0)
        self.CohesionSpinB.setObjectName("CohesionSpinB")
        self.gridLayout.addWidget(self.CohesionSpinB, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(JointMaterial)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.FrictionSpinB)
        self.label_13.setBuddy(self.extensionSpinB)
        self.label_4.setBuddy(self.CohesionSpinB)

        self.retranslateUi(JointMaterial)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), JointMaterial.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), JointMaterial.reject)
        QtCore.QMetaObject.connectSlotsByName(JointMaterial)

    def retranslateUi(self, JointMaterial):
        JointMaterial.setWindowTitle(QtGui.QApplication.translate("JointMaterial", "Joint Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("JointMaterial", "Frictional angle(fa):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("JointMaterial", "Extension strength(es):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("JointMaterial", "Cohesion(co):", None, QtGui.QApplication.UnicodeUTF8))

