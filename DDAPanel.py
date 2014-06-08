# coding=gbk

#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2009, 2010                                              *  
#*   Xiaolong Cheng <lainegates@163.com>                                   *  
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************
#****************************************
#Modified by Silver <bumingqiu@gmail.com>
#2013-11-27
#****************************************

import FreeCAD , FreeCADGui
from pivy import coin
from PySide import QtCore , QtGui
import PySide
from ui_DC import *
from ui_DL import *
from drawGui import getMainWindow
from Base import translate,_translate

class DLCMD :
    '''
    The DDA Line Panel , call DL Panel out
    '''
    
    def __init__( self ):
        self.__initUI()
        self.__initConnections()
        
    def __initConnections(self):
        '''
        connect qtoolbar actions to functions
        '''
        self.act_LoadDLInputData.triggered.connect(self.loadDLInputData)
        self.act_Border.triggered.connect(self.generateBorder)
        self.act_BoundaryNode.triggered.connect(self.drawBoundaryNodes)
        self.act_AdditionalLine.triggered.connect(self.drawAdditionalLines)
#        self.act_Slope.triggered.connect(self.showSlopePanel)         #Ivan, Slope
        self.act_JointSet.triggered.connect(self.showJointSetPanel)
        self.act_Tunnel.triggered.connect(self.showTunnelPanel)
        self.act_Calculate.triggered.connect(self.calculate)
        self.act_Confirm.triggered.connect(self.confirm)
        self.act_LoadDCInputData.triggered.connect(self.loadDCInputData)

        self.act_LoadDXFInputData.triggered.connect(self.loadDXFInputData)           #Ivan, dxf
        
    def __initUI(self):
        '''
        init DLCMD's UI , using QToolbar
        '''
        self.mw = getMainWindow()
        self.ui = QtGui.QToolBar('DLCMD' , self.mw)
        self.ui.setVisible(False)
        self.mw.addToolBar(QtCore.Qt.TopToolBarArea , self.ui)
        self.ui.setMovable(True)
        self.act_LoadDLInputData = QtGui.QAction(QtGui.QIcon(':/icons/LoadDLInput'),QtGui.QApplication.translate('DDA_DL','LoadDLInputData'),self.ui)
        self.act_BoundaryNode = QtGui.QAction(QtGui.QIcon(':/icons/BoundaryNodes'),QtGui.QApplication.translate('DDA_DL','BoundaryNodes') ,self.ui)
        self.act_Border = QtGui.QAction(QtGui.QIcon(':/icons/Border'),QtGui.QApplication.translate('DDA_DL','GenerateBorder') ,self.ui)
        self.act_AdditionalLine = QtGui.QAction(QtGui.QIcon(':/icons/additionalLines'),QtGui.QApplication.translate('DDA_DL','AdditionalLine') ,self.ui)
        self.act_JointSet = QtGui.QAction(QtGui.QIcon(':/icons/JointSet'),QtGui.QApplication.translate('DDA_DL','JointSet') ,self.ui)
        self.act_Tunnel = QtGui.QAction(QtGui.QIcon(':/icons/Tunnel'),QtGui.QApplication.translate('DDA_DL','Tunnel'),self.ui)
        self.act_Calculate = QtGui.QAction(QtGui.QIcon(':/icons/Calculate'),QtGui.QApplication.translate('DDA_DL','Calculate'),self.ui)
        self.act_Confirm = QtGui.QAction(QtGui.QIcon(':/icons/Save'),QtGui.QApplication.translate('DDA_DL','Confirm'),self.ui)
        self.act_LoadDCInputData = QtGui.QAction(QtGui.QIcon(':/icons/LoadDCInput'),QtGui.QApplication.translate('DDA_DL','LoadDCInputData'),self.ui)
        self.act_LoadDXFInputData = QtGui.QAction(QtGui.QIcon(':/icons/LoadDXF'),QtGui.QApplication.translate('DDA_DL','LoadDXF'),self.ui)#Ivan, dxf
        
        self.ui.addAction(self.act_LoadDLInputData)
        self.ui.addAction(self.act_Border)
        self.ui.addAction(self.act_BoundaryNode)
        self.ui.addAction(self.act_AdditionalLine)
        self.ui.addAction(self.act_JointSet)
        self.ui.addAction(self.act_Tunnel)
        self.ui.addSeparator()
        self.ui.addAction(self.act_Calculate)
        self.ui.addAction(self.act_Confirm)        
        self.ui.addAction(self.act_LoadDCInputData)
        self.ui.addAction(self.act_LoadDXFInputData)    #Ivan

        
    def refreshButton4FirstStep(self):
        self.act_Border.setEnabled(False)
        self.act_BoundaryNode.setEnabled(True)
        self.act_Border.setEnabled(False)
        self.act_JointSet.setEnabled(False)
        self.act_Tunnel.setEnabled(False)

        self.act_Calculate.setEnabled(True)
        self.act_LoadDLInputData.setEnabled(True)
        self.act_Confirm.setEnabled(False)
        self.act_LoadDCInputData.setEnabled(True)
        self.act_LoadDXFInputData.setEnabled(True)   #Ivan, dxf
        

    def refreshButton4ShapesAvailableStep(self):
        self.act_Border.setEnabled(True)
        self.act_BoundaryNode.setEnabled(True)
        self.act_Border.setEnabled(True)
        self.act_JointSet.setEnabled(True)
        self.act_Tunnel.setEnabled(True)

        self.act_Calculate.setEnabled(True)
        self.act_LoadDLInputData.setEnabled(True)
        self.act_Confirm.setEnabled(True)
        self.act_LoadDCInputData.setEnabled(True)
        self.act_LoadDXFInputData.setEnabled(True)   #Ivan, dxf
        
    def refreshButton4SpecialStep(self):
        self.act_Border.setEnabled(False)
        self.act_BoundaryNode.setEnabled(True)
        self.act_Border.setEnabled(False)
        self.act_JointSet.setEnabled(False)
        self.act_Tunnel.setEnabled(False)

        self.act_Calculate.setEnabled(True)
        self.act_LoadDLInputData.setEnabled(True)
        self.act_Confirm.setEnabled(True)
        self.act_LoadDCInputData.setEnabled(True)
        self.act_LoadDXFInputData.setEnabled(True)   #Ivan, dxf
        
    def refreshButtons(self):
        from Base import __currentStep__
        assert __currentStep__
        if __currentStep__ == 'FirstStep' :
            self.refreshButton4FirstStep()
        elif __currentStep__ == 'ShapesAvailable' :
            self.refreshButton4ShapesAvailableStep()
        elif __currentStep__ == 'SpecialStep':
            self.refreshButton4SpecialStep()
        
    def loadDCInputData(self):
        FreeCADGui.runCommand('DDA_ShowDCInputGraph')
        self.refreshButtons()

    def loadDXFInputData(self):              #Ivan, dxf
        FreeCADGui.runCommand('DDA_ShowDXFInputGraph')
        self.refreshButtons()

    def loadDLInputData(self):
        FreeCADGui.runCommand('DDA_ShowDLInputGraph')
        import Base
        Base.__currentStep__ = 'ShapesAvailable'
        self.refreshButtons()
                
    def generateBorder(self):
        FreeCADGui.runCommand('DDA_GenerateBorder')

    def drawAdditionalLines(self):
        FreeCADGui.runCommand('DDA_AdditionalLine')
        
    def drawBoundaryNodes(self):
        FreeCADGui.runCommand('DDA_BoundaryLine')
        import DDADatabase , Base
        self.refreshButtons()
        
    def showJointSetPanel(self):
        FreeCADGui.runCommand('DDA_JointSet')
        
    def showTunnelPanel(self):
        FreeCADGui.runCommand('DDA_Tunnel')
        
    def calculate(self):
        FreeCADGui.runCommand('DDA_DLCalculate')
        self.refreshButtons()
        
    def confirm(self):
        FreeCADGui.runCommand('DDA_DCInputDataStore')
            
    def GetResources(self):
        return {'Pixmap'  :'DL',
                'MenuText':  QtCore.QT_TRANSLATE_NOOP('DDA_DL','DLPanel'),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_DL','call DL panel out')}
        
    def Activated(self, name="None"):
        FreeCAD.Console.PrintMessage( 'Creator activing\n')
        if FreeCAD.activeDDACommand:
            FreeCAD.activeDDACommand.finish()
        self.doc = FreeCAD.ActiveDocument
        self.view = FreeCADGui.ActiveDocument.ActiveView
        if not self.doc:
            FreeCAD.Console.PrintMessage( 'FreeCAD.ActiveDocument get failed\n')
            self.finish()
        else:
            FreeCAD.activeDDACommand = self  # FreeCAD.activeDDACommand 在不同的时间会接收不同的命令 
            if not self.ui.isVisible():
                self.ui.show()
#                import DDAToolbars
#                DDAToolbars.lineToolbar.on()
            
        import Base
        Base.changeStage('PreDL')
        Base.changeStep4Stage('FirstStep')
        self.refreshButtons()
            
        # activate  DL Panel
        Base.setCurrentDDACommand(self)
        self.ui.show()
        
            
    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')
        
    def finish(self):
        pass
        
    def hideUI(self):
        self.ui.hide()
        
class DCCMD :
    '''
    The DDA Line Panel , call DL Panel out
    '''
    def __init__( self ):
        self.__initUI()
        self.__initConnections()

    def __initConnections(self):        
        '''
        connect actions to functions
        '''
        self.act_FixedPoint.triggered.connect(self.drawFixedPoint)
        self.act_LoadingPoint.triggered.connect(self.drawLoadingPoint)
        self.act_MeasuredPoint.triggered.connect(self.drawMeasuredPoint)
        self.act_HolePoint.triggered.connect(self.drawHolePoint)
        self.act_MaterialLine.triggered.connect(self.drawMaterialLine)
        self.act_GenerateBolts.triggered.connect(self.generateTunnelBolts)
#        self.act_Preview.triggered.connect(self.preview)
        self.act_Calculate.triggered.connect(self.calculate)
        self.act_Confirm.triggered.connect(self.confirm)
        self.act_LoadData.triggered.connect(self.loadDFInputData)

    def __initUI(self):
        '''
        init DLCMD's UI , using QToolbar
        '''
        self.mw = getMainWindow()
        self.ui = QtGui.QToolBar('DCCMD' , self.mw)
        self.ui.setVisible(False)
        self.mw.addToolBar(QtCore.Qt.TopToolBarArea , self.ui)
        self.ui.setMovable(True)
        self.act_FixedPoint = QtGui.QAction(QtGui.QIcon(':/icons/FixedPoint'),QtGui.QApplication.translate('DDA_DC','FixedPoint') ,self.ui)
        self.act_LoadingPoint = QtGui.QAction(QtGui.QIcon(':/icons/LoadingPont'),QtGui.QApplication.translate('DDA_DC','LoadingPoint'),self.ui)
        self.act_MeasuredPoint = QtGui.QAction(QtGui.QIcon(':/icons/MeasuredPoint'),QtGui.QApplication.translate('DDA_DC','MeasuredPoint') ,self.ui)
        self.act_HolePoint = QtGui.QAction(QtGui.QIcon(':/icons/HolePoint'),QtGui.QApplication.translate('DDA_DC','HolePoint' ),self.ui)
        self.act_MaterialLine = QtGui.QAction(QtGui.QIcon(':/icons/MaterialLine'),QtGui.QApplication.translate('DDA_DC','MaterialLine' ),self.ui)        
#        self.act_Preview = QtGui.QAction('Preview',self.ui)
        self.act_Calculate = QtGui.QAction(QtGui.QIcon(':/icons/Calculate'),QtGui.QApplication.translate('DDA_DC','Calculate'),self.ui)
        self.act_Confirm = QtGui.QAction(QtGui.QIcon(':/icons/Save'),QtGui.QApplication.translate('DDA_DC','Confirm'),self.ui)
        self.act_LoadData = QtGui.QAction(QtGui.QIcon(':/icons/LoadDFInput'),QtGui.QApplication.translate('DDA_DC','LoadDFInputData'),self.ui)
        self.act_GenerateBolts = QtGui.QAction(QtGui.QIcon(':/icons/boltsGenerator'),QtGui.QApplication.translate('DDA_DC','GenerateTunnelBolts'),self.ui)
        self.ui.addAction(self.act_FixedPoint)
        self.ui.addAction(self.act_LoadingPoint)
        self.ui.addAction(self.act_MeasuredPoint)
        self.ui.addAction(self.act_HolePoint)
        self.ui.addAction(self.act_MaterialLine)
#        self.ui.addAction(self.act_GenerateBolts) 
        self.ui.addSeparator()
#        self.ui.addAction(self.act_Preview)
        self.ui.addAction(self.act_Calculate)
        self.ui.addAction(self.act_Confirm)
        self.ui.addAction(self.act_LoadData)                
        
    def refreshButton4FirstStep(self):
        self.act_FixedPoint.setEnabled(False)
        self.act_LoadingPoint.setEnabled(False)
        self.act_MeasuredPoint.setEnabled(False)
        self.act_HolePoint.setEnabled(False)
        self.act_MaterialLine.setEnabled(False)
        self.act_GenerateBolts.setEnabled(False)
             
        self.act_Calculate.setEnabled(True)
        self.act_Confirm.setEnabled(False)
        self.act_LoadData.setEnabled(True)

    def refreshButton4ShapesAvailableStep(self):
        self.act_FixedPoint.setEnabled(True)
        self.act_LoadingPoint.setEnabled(True)
        self.act_MeasuredPoint.setEnabled(True)
        self.act_HolePoint.setEnabled(True)
        self.act_MaterialLine.setEnabled(True) 
        self.act_GenerateBolts.setEnabled(True)   
         
        self.act_Calculate.setEnabled(True)
        self.act_Confirm.setEnabled(True)
        self.act_LoadData.setEnabled(True)
        
    def refreshButtons(self):
        from Base import __currentStep__
        assert __currentStep__
        if __currentStep__ == 'FirstStep' :
            self.refreshButton4FirstStep()
        elif __currentStep__ == 'ShapesAvailable' :
            self.refreshButton4ShapesAvailableStep()
        
    def drawFixedPoint(self):
        FreeCADGui.runCommand('DDA_FixedPoint')
    
    def drawLoadingPoint(self):
        FreeCADGui.runCommand('DDA_LoadingPoint')
        
    def drawMeasuredPoint(self):
        FreeCADGui.runCommand('DDA_MeasuredPoint')
        
    def drawHolePoint(self):
        FreeCADGui.runCommand('DDA_HolePoint')
    
    def drawMaterialLine(self):
        FreeCADGui.runCommand('DDA_MaterialLine')
        
    def generateTunnelBolts(self):
        FreeCADGui.runCommand('DDA_GenerateTunnelBolts')
        
    def confirm(self):
        import os , shutil
        import Base
        path = os.getcwd()
        os.chdir(Base.__currentProjectPath__)
        shutil.copy('data.dc', 'backup.dc')
        if os.path.exists('data_backup.dc'):
            shutil.copy('data_backup.dc', 'data.dc')
        os.chdir(path)

        
        FreeCADGui.runCommand('DDA_DCInputChangesConfirm')
        FreeCADGui.runCommand('DDA_DCOnlyCalculate')
        
        os.chdir(Base.__currentProjectPath__)
        shutil.copy('data.dc' , 'data_backup.dc')
        os.remove('data.dc')
        os.rename('backup.dc', 'data.dc')
        os.chdir(path)
        
    def calculate(self):
        FreeCADGui.runCommand('DDA_DCCalculate')

    def loadDFInputData(self):
        FreeCADGui.runCommand('DDA_DisplayDFInputGraph')
        
    def GetResources(self):
        return {'Pixmap'  :'DC',
                'MenuText':  QtCore.QT_TRANSLATE_NOOP('DDA_DC','DCPanel'),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_DC','call DC panel out')}
        
    def Activated(self, name="None"):
        FreeCAD.Console.PrintMessage( 'Creator activing\n')
        if FreeCAD.activeDDACommand:
            FreeCAD.activeDDACommand.finish()
        self.doc = FreeCAD.ActiveDocument
        self.view = FreeCADGui.ActiveDocument.ActiveView
        
        import Base
        Base.changeStage('DC')
        
        # activate  DC Panel
        Base.setCurrentDDACommand(self)
        self.ui.show()
        
        self.featureName = name
        
        if not self.doc:
            FreeCAD.Console.PrintMessage( Base.translate('DDA_DC','FreeCAD.ActiveDocument get failed\n'))
            self.finish()
        else:
            FreeCAD.activeDDACommand = self  # FreeCAD.activeDDACommand 在不同的时间会接收不同的命令 
            self.ui.show()
            
    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')
        
    def finish(self):
        pass
        
    def hideUI(self):
        self.ui.hide()

class ExamplePanel(PySide.QtGui.QDialog):
    def __init__(self,parent=None):
        print 'abc'
        PySide.QtGui.QDialog.__init__(self,parent)
        print 'abcd'
        self.initUI()
        
    def initUI(self):
        from UIs import ui_ExamplePanel 
        self.ui = ui_ExamplePanel.Ui_Dialog()
        self.ui.setupUi(self)
        self.__initPanel()
        
    def __initPanel(self):
        from PySide import QtGui, QtCore
        table = self.ui.tableWidget
        table.setColumnCount(3)
        table.setRowCount(9)
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        for i in range(3):
            table.setColumnWidth(i , 300)
        for i in range(9):
            table.setRowHeight(i , 170)
        for k in range(27): # w7 examples of DDA
            i = k/3
            j = k%3
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setIcon(QtGui.QIcon(':/icons/%d.png'%k))
            table.setItem(i,j,item)
        table.cellClicked.connect(self.setupExample4Index) 
    
    def setupExample4Index(self, rowIdx , columnIdx):
#        print rowIdx , '  ' , columnIdx
        import FreeCAD, FreeCADGui, os, shutil
        import Base
        self.hide()
        idx = rowIdx*3+columnIdx # index of DDA example
        path = os.path.join(FreeCAD.getHomePath(), 'data/DDA_examples')
        dcfile = '%s/dc/DC%s.DC'%(path,str(idx).zfill(2))
        dffile = '%s/df/BL%s.DF'%(path,str(idx).zfill(2))
        dfparas = '%s/df/DF%s.DF'%(path,str(idx).zfill(2))

        if not os.path.exists(dcfile) or not os.path.exists(dffile) \
           or not os.path.exists(dfparas):
            Base.showErrorMessageBox('DataError'\
              , 'data files of DDA examples not found.\nPlease unzip the \"DDA_examples.zip\"under $FreeCADInstallPath/data')
            return
        shutil.copy( dcfile, '%s/data.dc'%Base.__currentProjectPath__)
        shutil.copy( dffile, '%s/data.df'%Base.__currentProjectPath__)
        shutil.copy( dfparas, '%s/parameters.df'%Base.__currentProjectPath__)

        Base.changeStage('DL')
        FreeCADGui.runCommand('DDA_ShowDCInputGraph')
        
        
    def GetResources(self):
        return {'Pixmap'  :'DDA_examples',
                'MenuText':  QtCore.QT_TRANSLATE_NOOP('DDA_ExamplePanel','ExamplePanel'),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_ExamplePanel','Display DDA\'s examples')}
        
    def Activated(self, name="None"):
        if FreeCAD.activeDDACommand:
            FreeCAD.activeDDACommand.finish()
        
        # activate  DC Panel
        import Base
        Base.setCurrentDDACommand(self)
        self.exec_()
        
    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')

    def finish(self):
        pass
        
    def hideUI(self):
        self.hide()



DLPanel = DLCMD()
DCPanel = DCCMD()
    
def hideDLAndDCPanel():
    DLPanel.ui.hide()
    DLPanel.ui.setVisible(False)
    DCPanel.ui.hide()
    DCPanel.ui.setVisible(False)
    
FreeCADGui.addCommand('DDA_DL', DLPanel)
FreeCADGui.addCommand('DDA_DC', DCPanel)
FreeCADGui.addCommand('DDA_Examples', ExamplePanel())
