# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Mod\DDA\Resources\ui\DFMaterialPanel.ui'
#
# Created: Tue May 13 15:57:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DFMaterialPanel(object):
    def setupUi(self, DFMaterialPanel):
        DFMaterialPanel.setObjectName("DFMaterialPanel")
        DFMaterialPanel.resize(768, 397)
        DFMaterialPanel.setMinimumSize(QtCore.QSize(533, 325))
        DFMaterialPanel.setMaximumSize(QtCore.QSize(1000, 1000))
        self.verticalLayout_3 = QtGui.QVBoxLayout(DFMaterialPanel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtGui.QListWidget(DFMaterialPanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(140, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(140, 16777215))
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.horizontalLayout.addWidget(self.listWidget)
        self.stackedWidget = QtGui.QStackedWidget(DFMaterialPanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(350, 250))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blockMatsGroupB = QtGui.QGroupBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockMatsGroupB.sizePolicy().hasHeightForWidth())
        self.blockMatsGroupB.setSizePolicy(sizePolicy)
        self.blockMatsGroupB.setObjectName("blockMatsGroupB")
        self.horizontalLayout_2.addWidget(self.blockMatsGroupB)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.jointMatsGroupB = QtGui.QGroupBox(self.page_2)
        self.jointMatsGroupB.setObjectName("jointMatsGroupB")
        self.horizontalLayout_3.addWidget(self.jointMatsGroupB)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LoadingPointMatsGroupB = QtGui.QGroupBox(self.page_3)
        self.LoadingPointMatsGroupB.setObjectName("LoadingPointMatsGroupB")
        self.horizontalLayout_4.addWidget(self.LoadingPointMatsGroupB)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtGui.QLabel(self.page_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.waterUnitSpinB = QtGui.QDoubleSpinBox(self.page_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waterUnitSpinB.sizePolicy().hasHeightForWidth())
        self.waterUnitSpinB.setSizePolicy(sizePolicy)
        self.waterUnitSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.waterUnitSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.waterUnitSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.waterUnitSpinB.setDecimals(6)
        self.waterUnitSpinB.setMinimum(-999999999.0)
        self.waterUnitSpinB.setMaximum(999999999.0)
        self.waterUnitSpinB.setObjectName("waterUnitSpinB")
        self.horizontalLayout_7.addWidget(self.waterUnitSpinB)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.waterMatsGroupB = QtGui.QGroupBox(self.page_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.waterMatsGroupB.sizePolicy().hasHeightForWidth())
        self.waterMatsGroupB.setSizePolicy(sizePolicy)
        self.waterMatsGroupB.setObjectName("waterMatsGroupB")
        self.verticalLayout.addWidget(self.waterMatsGroupB)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.sectionAngleSpinBox = QtGui.QDoubleSpinBox(self.page_5)
        self.sectionAngleSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.sectionAngleSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sectionAngleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sectionAngleSpinBox.setDecimals(6)
        self.sectionAngleSpinBox.setMaximum(1.0)
        self.sectionAngleSpinBox.setObjectName("sectionAngleSpinBox")
        self.gridLayout.addWidget(self.sectionAngleSpinBox, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.timeSpinB = QtGui.QDoubleSpinBox(self.page_5)
        self.timeSpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.timeSpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeSpinB.setDecimals(6)
        self.timeSpinB.setMinimum(-999999999.0)
        self.timeSpinB.setMaximum(999999999.0)
        self.timeSpinB.setProperty("value", 0.005)
        self.timeSpinB.setObjectName("timeSpinB")
        self.gridLayout.addWidget(self.timeSpinB, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gravitySpinB = QtGui.QDoubleSpinBox(self.page_5)
        self.gravitySpinB.setMinimumSize(QtCore.QSize(100, 0))
        self.gravitySpinB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gravitySpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gravitySpinB.setDecimals(6)
        self.gravitySpinB.setMinimum(-999999999.0)
        self.gravitySpinB.setMaximum(999999999.0)
        self.gravitySpinB.setProperty("value", 9.81)
        self.gravitySpinB.setObjectName("gravitySpinB")
        self.gridLayout.addWidget(self.gravitySpinB, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.page_5)
        self.label_6.setMinimumSize(QtCore.QSize(151, 20))
        self.label_6.setMaximumSize(QtCore.QSize(151, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.browseBtn = QtGui.QPushButton(self.page_5)
        self.browseBtn.setObjectName("browseBtn")
        self.gridLayout.addWidget(self.browseBtn, 3, 3, 1, 1)
        self.earthquakeFilenameLabel = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.earthquakeFilenameLabel.sizePolicy().hasHeightForWidth())
        self.earthquakeFilenameLabel.setSizePolicy(sizePolicy)
        self.earthquakeFilenameLabel.setObjectName("earthquakeFilenameLabel")
        self.gridLayout.addWidget(self.earthquakeFilenameLabel, 3, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.earthquakeStepsLabel = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.earthquakeStepsLabel.sizePolicy().hasHeightForWidth())
        self.earthquakeStepsLabel.setSizePolicy(sizePolicy)
        self.earthquakeStepsLabel.setObjectName("earthquakeStepsLabel")
        self.gridLayout.addWidget(self.earthquakeStepsLabel, 2, 0, 1, 1)
        self.totalStepsSpinB = QtGui.QSpinBox(self.page_5)
        self.totalStepsSpinB.setMinimumSize(QtCore.QSize(100, 20))
        self.totalStepsSpinB.setMaximumSize(QtCore.QSize(100, 20))
        self.totalStepsSpinB.setWhatsThis("")
        self.totalStepsSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalStepsSpinB.setReadOnly(True)
        self.totalStepsSpinB.setMaximum(999999999)
        self.totalStepsSpinB.setObjectName("totalStepsSpinB")
        self.gridLayout.addWidget(self.totalStepsSpinB, 2, 1, 1, 1)
        self.startStepsSpinB = QtGui.QSpinBox(self.page_5)
        self.startStepsSpinB.setMinimumSize(QtCore.QSize(100, 20))
        self.startStepsSpinB.setMaximumSize(QtCore.QSize(100, 20))
        self.startStepsSpinB.setWhatsThis("")
        self.startStepsSpinB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startStepsSpinB.setMaximum(999999999)
        self.startStepsSpinB.setObjectName("startStepsSpinB")
        self.gridLayout.addWidget(self.startStepsSpinB, 2, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_8 = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem = QtGui.QSpacerItem(20, 80, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_7 = QtGui.QLabel(self.page_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        spacerItem1 = QtGui.QSpacerItem(20, 79, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page_5)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DFMaterialPanel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(DFMaterialPanel)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DFMaterialPanel.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DFMaterialPanel.reject)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged(int)"), self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(DFMaterialPanel)

    def retranslateUi(self, DFMaterialPanel):
        DFMaterialPanel.setWindowTitle(QtGui.QApplication.translate("DFMaterialPanel", "Configure DF materials", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("DFMaterialPanel", "Block materials", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("DFMaterialPanel", "Joint materials", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("DFMaterialPanel", "Loading points", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(3).setText(QtGui.QApplication.translate("DFMaterialPanel", "water (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(4).setText(QtGui.QApplication.translate("DFMaterialPanel", "earthquake (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.blockMatsGroupB.setTitle(QtGui.QApplication.translate("DFMaterialPanel", "Parameters for each block material", None, QtGui.QApplication.UnicodeUTF8))
        self.jointMatsGroupB.setTitle(QtGui.QApplication.translate("DFMaterialPanel", "Parameters for each joint material", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadingPointMatsGroupB.setTitle(QtGui.QApplication.translate("DFMaterialPanel", "Parameters for each loading points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DFMaterialPanel", "Water unit widget: ", None, QtGui.QApplication.UnicodeUTF8))
        self.waterMatsGroupB.setTitle(QtGui.QApplication.translate("DFMaterialPanel", "Surface control points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DFMaterialPanel", "Section angle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DFMaterialPanel", "Time interval: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DFMaterialPanel", "Gravity acceleration: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DFMaterialPanel", "Earthquake data file : ", None, QtGui.QApplication.UnicodeUTF8))
        self.browseBtn.setText(QtGui.QApplication.translate("DFMaterialPanel", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.earthquakeFilenameLabel.setText(QtGui.QApplication.translate("DFMaterialPanel", "not select yet.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("DFMaterialPanel", "<html><head/><body><p><span style=\" font-size:11pt;\">The time start use to earthquake data. </span></p><p><span style=\" font-size:11pt;\">The sum of this number and earthquake steps must be smaller than total steps.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DFMaterialPanel", "Start steps  :", None, QtGui.QApplication.UnicodeUTF8))
        self.earthquakeStepsLabel.setToolTip(QtGui.QApplication.translate("DFMaterialPanel", "<html><head/><body><p><span style=\" font-size:11pt;\">Total earthquake steps.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.earthquakeStepsLabel.setText(QtGui.QApplication.translate("DFMaterialPanel", "Earthquake steps  :", None, QtGui.QApplication.UnicodeUTF8))
        self.totalStepsSpinB.setToolTip(QtGui.QApplication.translate("DFMaterialPanel", "<html><head/><body><p><span style=\" font-size:11pt;\">Total earthquake steps.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.startStepsSpinB.setToolTip(QtGui.QApplication.translate("DFMaterialPanel", "<html><head/><body><p><span style=\" font-size:11pt;\">The time start to use earthquake data. </span></p><p><span style=\" font-size:11pt;\">The sum of this number and earthquake steps must be smaller than total steps</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("DFMaterialPanel", "<html><head/><body><p><span style=\" font-size:11pt;\">The time start use to earthquake data. </span></p><p><span style=\" font-size:11pt;\">The sum of this number and earthquake steps must be smaller than total steps.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DFMaterialPanel", "Note: We didn\'t supply edit widget for earthquake because eathquake is a phnomenon. \n"
"We should only use the data without modifying it.", None, QtGui.QApplication.UnicodeUTF8))

