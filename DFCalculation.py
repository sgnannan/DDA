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

import os
import time
import FreeCADGui , FreeCAD
from FreeCAD import Base
from pivy import coin
from PySide import QtCore , QtGui

#from loadDataTools import ParseDFData
from Base import showErrorMessageBox , __currentProjectPath__ , __workbenchPath__
from DDATools import DataTable
from DDADatabase import df_inputDatabase
#import PyDDA

__BlockMaterialTabs__ = ( 'ma' , 'wx' , 'wy' , 'em' , 'pr' , 'sx' , 'sy' , 'sxy' , 'fa' , 'co' , 'es' , 'vx' , 'vy' , 'vr' )
__JointMaterialTabs__ = [ 'fa' , 'es' , 'co']
__LoadingPointParaTabs__ = [ 'ti' , 'hl' , 'vl']
__WaterParaTabs__ = [ 'x' , 'y']
__EarthquakeParaTabs__ =  [ 'x' , 'y' , 'z']
__rowHeight4Text__ = 18
def splitContent(content):
    texts = content.split()
    nums = {}
    try:
        for i in range(len(texts)/3):
            nums[texts[3*i].strip()] = float(texts[3*i+2])
    except:
        showErrorMessageBox('DataError', 'unvalid data read : (%s , %s)'%(texts[3*i],texts[3*i+2]))
    return nums

def organizeDictContent(nums, tabs):
    assert isinstance(nums, dict)
    content = []
    tmpS = [] 
    j=0
    for i in range(len(nums)):
        tmpS.append('%3s : %13.6f'%(tabs[i] , nums[tabs[i]]))
        j+=1
        if j%3==0:
            content.append(' '.join(tmpS))
            tmpS = []
    if len(tmpS)>0: content.append(' '.join(tmpS))
    return '\n'.join(content)

def organizeListContent(nums, tabs):
    assert isinstance(nums, list)
    content = []
    tmpS = [] 
    j=0
    for i in range(len(nums)):
        tmpS.append('%3s : %13.6f'%(tabs[i] , nums[tabs[i]]))
        j+=1
        if j%3==0:
            content.append(' '.join(tmpS))
            tmpS = []
    if len(tmpS)>0: content.append(' '.join(tmpS))
    return '\n'.join(content)

class BaseEditWidget(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.content = None
        
    def accept(self):
        self.refreshContent()
        #QtGui.QDialog.accept()
        self.hide() # accept() didn't hide dialog
        
    def outputContent(self):
        return self.content

class Ui_BlockMaterialEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_BlockMaterial 
        self.ui = ui_BlockMaterial.Ui_BlockMaterial()
        self.ui.setupUi(self)
        
    def setContent(self, content):
        self.content = content
        nums = splitContent(content)
        self.ui.massSpinB.setValue(nums['ma'])
        self.ui.weightXSpinB.setValue(nums['wx'])
        self.ui.weightYSpinB.setValue(nums['wy'])
        self.ui.ElasticitySpinB.setValue(nums['em'])
        self.ui.PoissonSpinB.setValue(nums['pr'])
        self.ui.stressXSpinB.setValue(nums['sx'])
        self.ui.stressYSpinB.setValue(nums['sy'])
        self.ui.stressXYSpinB.setValue(nums['sxy'])
        self.ui.FrictionSpinB.setValue(nums['fa'])
        self.ui.CohesionSpinB.setValue(nums['co'])
        self.ui.extensionSpinB.setValue(nums['es'])
        self.ui.speedXSpinB.setValue(nums['vx'])
        self.ui.speedYSpinB.setValue(nums['vy'])
        self.ui.speedRSpinB.setValue(nums['vr'])

    def refreshContent(self):
        nums = {}
        nums['ma'] = self.ui.massSpinB.value()
        nums['wx'] = self.ui.weightXSpinB.value()
        nums['wy'] = self.ui.weightYSpinB.value()
        nums['em'] = self.ui.ElasticitySpinB.value()
        nums['pr'] = self.ui.PoissonSpinB.value()
        nums['sx'] = self.ui.stressXSpinB.value()
        nums['sy'] = self.ui.stressYSpinB.value()
        nums['sxy'] = self.ui.stressXYSpinB.value()
        nums['fa'] = self.ui.FrictionSpinB.value()
        nums['co'] = self.ui.CohesionSpinB.value()
        nums['es'] = self.ui.extensionSpinB.value()
        nums['vx'] = self.ui.speedXSpinB.value()
        nums['vy'] = self.ui.speedYSpinB.value()
        nums['vr'] = self.ui.speedRSpinB.value()
        self.content = organizeDictContent(nums, __BlockMaterialTabs__)

class Ui_JointEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_JointMaterial
        self.ui = ui_JointMaterial.Ui_JointMaterial()
        self.ui.setupUi(self)

    def setContent(self, content):
        self.content = content
        nums = splitContent(content)
        self.ui.FrictionSpinB.setValue(nums['fa'])
        self.ui.extensionSpinB.setValue(nums['es'])
        self.ui.CohesionSpinB.setValue(nums['co'])

    def refreshContent(self):
        nums = {}
        nums['fa'] = self.ui.FrictionSpinB.value()
        nums['es'] = self.ui.extensionSpinB.value()
        nums['co'] = self.ui.CohesionSpinB.value()
        self.content = organizeDictContent(nums, __JointMaterialTabs__)
        
class Ui_LoadingPointParaEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_LoadingPointParameters4certainTime
        self.ui = ui_LoadingPointParameters4certainTime.Ui_LoadingPointParameters4certainTime()
        self.ui.setupUi(self)

    def setContent(self, content):
        self.content = content
        nums = splitContent(content)
        self.ui.timSpinB.setValue(nums['ti'])
        self.ui.horizontalLoadSpinB.setValue(nums['hl'])
        self.ui.verticalLoadSpinB.setValue(nums['vl'])

    def refreshContent(self):
        nums = {}
        nums['ti'] = self.ui.timSpinB.value()
        nums['hl'] = self.ui.horizontalLoadSpinB.value()
        nums['vl'] = self.ui.verticalLoadSpinB.value()
        self.content = organizeDictContent(nums, __LoadingPointParaTabs__)
        
class Ui_LoadingPointsEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.__contentList = ContentList(ifWithEditButton=True)
        self.__contentList.setTabs(__LoadingPointParaTabs__)
        self.__contentList.setEditWidget(Ui_LoadingPointParaEditWidget())
        self.initUI()
        
    def initUI(self):
        from UIs import ui_LoadingPointParameters
        self.ui = ui_LoadingPointParameters.Ui_LoadPointParameters()
        self.ui.setupUi(self)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.__contentList.getWidget())
        self.ui.groupBox.setLayout(layout)

    def setContent(self, content):
        self.content = content
#        lines = content.split()
        self.__contentList.setContent(self.content)

    def refreshContent(self):
        self.content = '\n'.join(self.__contentList.outputContent())
#        return '\n'.join(content)
            

    
class Ui_WaterPointEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_WaterControlPoint
        self.ui = ui_WaterControlPoint.Ui_Dialog()
        self.ui.setupUi(self)
        
    def setContent(self, content):
        self.content = content
        nums = splitContent(content)
        self.ui.XSpinB.setValue(nums['x'])
        self.ui.YSpinB.setValue(nums['y'])

    def refreshContent(self):
        nums = {}
        nums['x'] = self.ui.XSpinB.value()
        nums['y'] = self.ui.YSpinB.value()
        self.content = organizeDictContent(nums, __WaterParaTabs__)
 
class Ui_EarthquakeEditWidget(BaseEditWidget):
    def __init__(self,parent=None):
        BaseEditWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_EarthquakeAccelerationVector
        self.ui = ui_EarthquakeAccelerationVector.Ui_EarthquakeAccelerationVector()
        self.ui.setupUi(self)
        
    def setContent(self, content):
        self.content = content
        nums = splitContent(content)
    
        self.ui.XSpinB.setValue(nums['x'])
        self.ui.YSpinB.setValue(nums['y'])
        self.ui.YSpinB.setValue(nums['z'])
        
    def refreshContent(self):
        nums = {}
        nums['x'] = self.ui.XSpinB.value()
        nums['y'] = self.ui.YSpinB.value()
        nums['z'] = self.ui.YSpinB.value()
        self.content = organizeDictContent(nums, __EarthquakeParaTabs__)
 

class ContentList:
    def __init__(self , ifWithEditButton=False):
        from PySide import QtGui,QtCore
        self.__widget = QtGui.QWidget() 
        self.__table = QtGui.QTableWidget()
        self.__table.setColumnCount(2)
        self.__table.setHorizontalHeaderLabels(['Content' , 'Edit'])
        self.__table.setColumnWidth(0,460)
        self.__table.setColumnWidth(1,60)
        
        self.__maxRowCount = 9999999
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.__table)
        if ifWithEditButton:
            self.addBtn = QtGui.QPushButton('Add')
            self.addBtn.setFixedSize(30,30)
            self.addBtn.pressed.connect(self.addItem)
            self.delBtn = QtGui.QPushButton('Del')
            self.delBtn.setFixedSize(30,30)
            self.delBtn.pressed.connect(self.delRow)
            self.delBtn.setEnabled(False)
            tmpLayout = QtGui.QVBoxLayout()
            tmpLayout.addStretch(1)
            tmpLayout.addWidget(self.addBtn)
            tmpLayout.addWidget(self.delBtn)
            tmpLayout.addStretch(1)
            layout.addLayout(tmpLayout)
            self.__table.setColumnWidth(0,420)
            
        self.__widget.setLayout(layout)
            
        self.__signalMapper = QtCore.QSignalMapper()
        self.__signalMapper.mapped.connect(self.eidtBtnClicked)
#        self.__newLineAsSeparator = True # for joint, '\n' is separator, but for block not.
    
    def setVerticalLabels(self, labels):
        self.__table.setVerticalHeaderLabels(labels)

    
    def addItem(self):
        '''
        this function will be called only if ifWithEditButton is set True
        '''
        self.__editWidget.exec_()
        tmpContent = self.__editWidget.outputContent()
        self.__table.setRowCount(self.__table.rowCount()+1)
        self.addRow(self.__table.rowCount()-1)
        self.__table.cellWidget(self.__table.rowCount()-1,0).setText(tmpContent)
        if self.__table.rowCount()<self.__maxRowCount:
            self.addBtn.setEnabled(False)
        else:
            self.addBtn.setEnabled(True)
        self.addBtn.setEnabled(True)
    
    
    def getWidget(self):
        return self.__widget
        
    def setIfNewLineAsSeparator(self, flag):
        pass
#        self.__newLineAsSeparator = flag # for joint, '\n' is separator, but for block not.
        
    def setMaxRowCount(self, num):
        self.__maxRowCount = num
        
    def updateBtns4RowCount(self):
        if self.__table.rowCount()<self.__maxRowCount:
            self.addBtn.setEnabled(True)
        else:
            self.addBtn.setEnabled(False)
            
        if self.__table.rowCount()>0:
            self.delBtn.setEnabled(True)
        else:
            self.delBtn.setEnabled(True)
        
    def addRow(self , rowIdx ):
        label = QtGui.QLabel()
        label.setFont('Consolas')
        #label.setText(text)
        self.__table.setCellWidget(rowIdx , 0 , label)
        btn = QtGui.QPushButton()
        btn.setText('Edit')
        btn.setFixedWidth(50)
        #btn.setMinimumHeight(25)
        btn.setMaximumHeight(50)
        self.__table.setCellWidget(rowIdx , 1 , btn)
        btn.pressed.connect(self.__signalMapper.map)
        self.__signalMapper.setMapping( btn , rowIdx )
        
        
    def delRow(self ):
#        if not (rowIdx>=0 and rowIdx<self.__table.rowCount()):
        if self.__table.rowCount()==0:
            from Base import showErrorMessageBox
            showErrorMessageBox('dataError', 'Unvalid row')
        rowIdx = self.__table.rowCount()-1
        self.__signalMapper.removeMappings(self.__table.cellWidget(rowIdx,1),rowIdx)
        self.__table.removeRow(rowIdx)
        if self.__table.rowCount()>0:
            self.delBtn.setEnabled(False)
        else:
            self.delBtn.setEnabled(True)
        self.addBtn.setEnabled(True)
        
       
    def setRows(self , num):
        from PySide import QtGui,QtCore
        self.__table.setRowCount(num)
        for i in range(num):
            self.addRow(i)
    
    def setTabs(self , tabs):
        self.__tabs = tabs

    def setRawData(self , content , nums):
        '''
        content : a list, every line contains data(just numbers without tabs)
        tabs    : tabs ontains the tab for every number in a line 
        nums means : treat how many lines of data as an item  
        '''
        tabs = self.__tabs
        if len(content)==0: return
        
        self.setRows(len(nums))
        cou=0
        for i,num in enumerate(nums):
            tmpList = []
            for j in range(num):
                tmpList.append(organizeDictContent(dict(zip(tabs , content[cou+j])), tabs))
                    
            self.__table.cellWidget(i , 0).setText('\n'.join(tmpList))
            self.__table.cellWidget(i , 0).adjustSize()
            self.__table.cellWidget(i , 0).setWordWrap(True)
            cou+=num
            rowCount = max(len(tmpList) , tmpList[0].count('\n')+1)
            self.__table.setRowHeight(i ,rowCount*__rowHeight4Text__) # block paras is 5 lines
        
            
    def outputRawData(self):
        lines = []
        for i in range(self.__table.rowCount()):
            text = self.__table.cellWidget(i,0).text()
            texts = text.split('\n')
#            if not self.__newLineAsSeparator:
            if self.__tabs == __BlockMaterialTabs__: # block
                lines.append(' '.join(texts))
            elif self.__tabs == __LoadingPointParaTabs__: # loading points
                lines.append(texts)
            else:
                lines.extend(texts)
        rawData = []
        for line in lines:
            tmpNums = []
            if self.__tabs == __LoadingPointParaTabs__: # loading points
                for nums in line:
                    nums2 = nums.split()
                    tmpNums.append([float(nums2[i]) for i in range(len(nums2)) if i%3==2]) 
            else:
                nums = line.split()
                tmpNums = [float(nums[i]) for i in range(len(nums)) if i%3==2]
            rawData.append(tmpNums)
        return rawData
    
    def setContent(self , data ):
        lines = data.split('\n')
        self.setRows(len(lines))
        for i in range(len(lines)):
            self.__table.cellWidget(i , 0).setText(lines[i])
            
    def outputContent(self):
        lines = []
        for i in range(self.__table.rowCount()):
            lines.append(self.__table.cellWidget(i,0).text())
        return lines            
    
    def setEditWidget(self, editWidget):
        self.__editWidget = editWidget
        
    def eidtBtnClicked(self, rowIdx):
        self.__editWidget.setContent(self.__table.cellWidget(rowIdx,0).text())
        self.__editWidget.exec_()
        content = self.__editWidget.outputContent()
        self.__table.cellWidget(rowIdx,0).setText( content )
        self.__table.setRowHeight(rowIdx ,(content.count('\n')+1)*__rowHeight4Text__)
        
class Ui_DFMaterialPanel(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.initUI()
        
        self.__totalSteps = 0
        
    def initUI(self):
        from UIs import ui_DFMaterialPanel
        self.ui = ui_DFMaterialPanel.Ui_DFMaterialPanel()
        self.ui.setupUi(self)
        
        self.__initContentLists()
        self.ui.browseBtn.clicked.connect(self.selectEarthquakeFile)

    def enableEarthquake(self, flag):
        if flag==0:
            self.ui.stackedWidget.widget(4).setEnabled(False)
        else:
            self.ui.stackedWidget.widget(4).setEnabled(True)
            
    def selectEarthquakeFile(self):
        import PySide, Base
        fileDialog = PySide.QtGui.QFileDialog(None,'Select earthquake data file'\
                        , Base.__currentProjectPath__)
        fileDialog.setFileMode(PySide.QtGui.QFileDialog.ExistingFile)
        filename = None
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
        else:
            return
        
        lines = open(filename, 'rb').readlines()
        if len(lines)>self.__totalSteps+1: # first line is schema
            import Base
            Base.showErrorMessageBox('DataError'\
               , 'The number of earthquake data steps is bigger than total steps.')
            return False 
        print 'selected earthquake file: ', filename
        nums = lines[0].split()
        try:
            steps, gravity, timeInterval = \
                         int(nums[0]) \
                        ,float(nums[1]) \
                        ,float(nums[2])
            self.checkEarthquakeDataValid(lines[1:])
        except:
            import Base
            Base.showErrorMessageBox('DataError'\
               , 'Earthquake data is unvalid')
            return False
            
        if steps==None or gravity==None or timeInterval==None:
            import Base
            Base.showErrorMessageBox('DataError'\
               , 'Earthquake data is unvalid')
            return False
        
        if steps>self.__totalSteps:
            import Base
            Base.showErrorMessageBox('DataError'\
               , 'The number of earthquake steps is bigger than the number of total steps for DDA analysis.')
            return False
            
        
        self.ui.totalStepsSpinB.setValue(steps-1)
        self.ui.startStepsSpinB.setMaximum(self.__totalSteps-steps+1)
        self.ui.earthquakeFilenameLabel.setText(filename)
        self.setEarthquakeParas(0, gravity, timeInterval)


    def ifEarthquakeDataOK(self):
        import os
        return os.path.exists(self.ui.earthquakeFilenameLabel.text())
    
    def storeEarthquakeData(self):
        import Base
        import os
        if not self.ifEarthquakeDataOK():
            Base.showErrorMessageBox('Data Error', 'There are some errors for earthquake configuration.\nPlease check earthquake data.')
        lines = open(self.ui.earthquakeFilenameLabel.text(), 'rb').readlines()

        resultFile = open(os.path.join(Base.__currentProjectPath__, 'earthquake.df'),'wb')
        resultFile.write('%d %f %f\n'%(self.ui.startStepsSpinB.value()+len(lines)-1 \
                         , self.ui.gravitySpinB.value(), self.ui.timeSpinB.value()))
        resultFile.write('0 0 0\n'*self.ui.startStepsSpinB.value())
        resultFile.write(''.join(lines[1:]))
        resultFile.close()
        return True
        

    def checkEarthquakeDataValid(self, lines ):
        for line in lines:
            nums = line.split()
            x, y, z = float(nums[0]) ,float(nums[1]) ,float(nums[2])
            
    def setWaterUnitWeight(self, value):
        self.ui.waterUnitSpinB.setValue(value)
    
    def getWaterUnitWeight(self):
        return self.ui.waterUnitSpinB.value()
    
    def setEarthquakeParas(self, sectionAngle, gravityAcceleration, timeInterval):
        self.ui.sectionAngleSpinBox.setValue(sectionAngle)
        self.ui.gravitySpinB.setValue(gravityAcceleration)
        self.ui.timeSpinB.setValue(timeInterval)
    
    def getEarthquakeStartStep(self):
        return self.ui.startStepsSpinB.value()
    
    def setEarthquakeMaxSteps(self, num):
        diff = num-self.ui.totalStepsSpinB.value()
        if diff <0:
            return False
        self.__totalSteps = num
        self.ui.startStepsSpinB.setMaximum(diff)
        return True
        
    def getEarthquakeparas(self):
        return  self.ui.sectionAngleSpinBox.value() \
        ,self.ui.gravitySpinB.value(), self.ui.timeIntervalSpinB.value() \
        ,self.ui.startStepsSpinB.value()

    def __initContentLists(self):
        from PySide import QtCore, QtGui
        # block material
        self.__blockMatsList = ContentList()
        self.__blockMatsList.setTabs(__BlockMaterialTabs__)
        self.__blockMatsList.setEditWidget(Ui_BlockMaterialEditWidget())
        layout = QtGui.QVBoxLayout(self.ui.blockMatsGroupB)
        layout.addWidget(self.__blockMatsList.getWidget())
        self.ui.blockMatsGroupB.setLayout(layout)
        
        # joint material
        self.__jointMatsList = ContentList()
        self.__jointMatsList.setTabs(__JointMaterialTabs__)
        self.__jointMatsList.setEditWidget(Ui_JointEditWidget())
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.__jointMatsList.getWidget())
        self.ui.jointMatsGroupB.setLayout(layout)

        # loading points
        self.__loadingPointsList = ContentList(True)
        self.__loadingPointsList.setTabs(__LoadingPointParaTabs__)
        self.__loadingPointsList.setEditWidget(Ui_LoadingPointsEditWidget())
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.__loadingPointsList.getWidget())
        self.ui.LoadingPointMatsGroupB.setLayout(layout)
        
        # water
        self.__waterPointsList = ContentList(True)
        self.__waterPointsList.setTabs(__WaterParaTabs__)
        self.__waterPointsList.setEditWidget(Ui_WaterPointEditWidget())
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.__waterPointsList.getWidget())
        self.ui.waterMatsGroupB.setLayout(layout)

        # earthquake
        # there is no need to show earthquake data
#        self.__earthquakePointsList = ContentList(True)
#        self.__earthquakePointsList.setTabs(__EarthquakeParaTabs__)
#        self.__earthquakePointsList.setEditWidget(Ui_EarthquakeEditWidget())
#        layout = QtGui.QHBoxLayout()
#        layout.addWidget(self.__earthquakePointsList.getWidget())
#        self.ui.earthquakeMatsGroupB.setLayout(layout)
    
    def setHeaders4PageIdx(self, idx , headers):
        if idx==0:
            return self.__blockMatsList.setVerticalLabels(headers)
        elif idx==1:
            return self.__jointMatsList.setVerticalLabels(headers)
        elif idx==2:
            return self.__loadingPointsList.setVerticalLabels(headers)
        elif idx==3:
            return self.__waterPointsList.setVerticalLabels(headers)
        elif idx==4:
            return self.__earthquakePointsList.setVerticalLabels(headers)    
    

    def __getContentList4PageIdx(self, idx):
        if idx==0:
            return self.__blockMatsList
        elif idx==1:
            return self.__jointMatsList
        elif idx==2:
            return self.__loadingPointsList
        elif idx==3:
            return self.__waterPointsList
#        elif idx==4:
#            return self.__earthquakePointsList
        
    def setContent(self, pageIdx , content):
        contentList = self.__getContentList4PageIdx(pageIdx)
        if len(content)==0:
            return
        nums = []
        result = []
        if pageIdx==2  : # loading points or water
            for lst in content:
                nums.append(len(lst))
                result.extend(lst)
        else:                         # block, joint or earthquake
            nums = [1]*len(content)
            result = content
        contentList.setRawData(result , nums)

    def getContent(self, pageIdx):
        contentList = self.__getContentList4PageIdx(pageIdx)
        return contentList.outputRawData()

class Ui_DFPanel(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        from UIs import ui_DF
        self.ui = ui_DF.Ui_Dialog()
        self.ui.setupUi(self)
    
    def enableConfigPanel(self , flag):
        print 'set configuration panel : ' , flag
        self.ui.btn_ReadPara.setEnabled(flag)
        self.ui.btn_Config.setEnabled(flag)
        self.ui.buttonBox.setEnabled(flag)
        self.ui.StaticDynamicSpinB.setEnabled(flag)
        self.ui.stepsNumSpinB.setEnabled(flag)
        self.ui.maxRatioSpinB.setEnabled(flag)
        self.ui.timeIntervalSpinB.setEnabled(flag)
        self.ui.springStiffnessSpinB.setEnabled(flag)
        self.ui.SORSpinB.setEnabled(flag)
        self.ui.comboBox.setEnabled(flag)
       

class DFCalculation:
    '''
    process DF
    '''
    def __init__(self):
        self.current_path = __workbenchPath__
        self.origin_path = os.getcwd()
        self.dataParser = None
        #self.__initConfigUI()
        self.__initUI()
        self.__initConnections()
        self.__mainWidget.ui.comboBox.currentIndexChanged.connect(self.__matsWidget.enableEarthquake)
                
        
    def __initUI(self):
        '''
        init the DF configuration Panel
        '''
        self.__mainWidget = Ui_DFPanel()
        self.__matsWidget = Ui_DFMaterialPanel()
        
        
    def __initConnections(self):
        '''
        init connections in self.configUI.ui
        '''
        self.__mainWidget.ui.btn_ReadPara.pressed.connect(self.__readParameters)
        self.__mainWidget.ui.btn_ReadData.pressed.connect(self.__readBlocksData)
        #self.__mainWidget.ui.btn_Calc.pressed.connect(self.__calculateDF)
        self.__mainWidget.ui.buttonBox.accepted.connect(self.accept)
        self.__mainWidget.ui.btn_Config.pressed.connect(self.__configMats)
    
    def __configMats(self):
        
        if self.__matsWidget.setEarthquakeMaxSteps(self.__mainWidget.ui.stepsNumSpinB.value()):
            self.__matsWidget.show()
        else:
            import Base
            Base.showErrorMessageBox("DataError", "The sum of Earthquake steps and earthquake start step numer is bigger than total steps for DDA analysis.\nPlease modify total step number.")
    
    def __readBlocksData(self):
        '''
        read block data from file
        '''
        import Base , os
        filename = os.path.join(Base.__currentProjectPath__ , 'data.df')
        if not os.path.exists(filename):
            Base.showErrorMessageBox('FileNotFound', '\'data.df\' file was not found in project path.')
            return
        
        from loadDataTools import ParseDFInputGraphData
        self.dataParser = ParseDFInputGraphData()
        
        if not self.dataParser.parse(str(filename)):
            showErrorMessageBox('Data Error' , 'the schema of file is incorrected')
            self.__mainWidget.ui.loadDataLabel.setText('faild')
            return

        self.__mainWidget.ui.loadDataLabel.setText('sucessed')

        print 'DF data parse successfully'    
        self.__mainWidget.enableConfigPanel(True)
        
        from DDADatabase import df_inputDatabase
        data = df_inputDatabase
        self.__mainWidget.ui.blockNumLineE.setText(str(len(df_inputDatabase.blockMatCollections)))
        print df_inputDatabase.blockMatCollections
        self.__mainWidget.ui.jointNumLineE.setText(str(len(df_inputDatabase.jointMatCollections)))
        print df_inputDatabase.jointMatCollections
        self.dataParser = None
        
        self.__setDefaultParameters()
        
    def __setDefaultParameters(self):
        from DDADatabase import df_inputDatabase as dfDB
        # block material
        self.__matsWidget.setContent(0,[[0.0]*14]*len(dfDB.blockMatCollections))
        nums = list(dfDB.blockMatCollections)
        for i , n in enumerate(nums):
            nums[i] = str(n)
        self.__matsWidget.setHeaders4PageIdx(0, nums)
        # joint material
        self.__matsWidget.setContent(1, [[0.0]*3]*len(dfDB.jointMatCollections))
        nums = list(dfDB.jointMatCollections)
        for i , n in enumerate(nums):
            nums[i] = str(n)
        self.__matsWidget.setHeaders4PageIdx(1, nums)
        # loading points
        self.__matsWidget.setContent(2, [[[0.0]*3]*2]*len(dfDB.loadingPoints))

                                            
    
    def __readParameters(self):
        '''
        read parameters from file
        '''
        import Base
        filename = os.path.join(Base.__currentProjectPath__ , 'parameters.df')
        if not os.path.exists(filename):
            Base.showErrorMessageBox('FileNotFound', '\'parameters.df\' file was not found in project path.')
            return

        from loadDataTools import ParseDFInputParameters
        parasParser = ParseDFInputParameters()
        
        if not parasParser.parse(str(filename)):
            showErrorMessageBox('Data Error' , 'the schema of file is incorrected')
            self.__mainWidget.ui.loadParasLabel.setText('faild')
            return        
        self.__mainWidget.ui.loadParasLabel.setText('sucessed')

        self.__storePara2Panel()
        
    def __storePara2Panel(self):
        from DDADatabase import df_inputDatabase
        paras = df_inputDatabase.paras
        
        self.__mainWidget.ui.StaticDynamicSpinB.setValue(paras.ifDynamic)
        self.__mainWidget.ui.stepsNumSpinB.setValue(paras.stepsNum)
        self.__mainWidget.ui.maxRatioSpinB.setValue(paras.ratio)
        self.__mainWidget.ui.timeIntervalSpinB.setValue(paras.OneSteptimeLimit)
        self.__mainWidget.ui.springStiffnessSpinB.setValue(paras.springStiffness)
        self.__mainWidget.ui.SORSpinB.setValue(paras.SOR)
        self.__mainWidget.ui.comboBox.setCurrentIndex(paras.ifRightHand)
        
        self.__matsWidget.setContent(0,  paras.blockMats )
        print 'blocks mats import done'
        self.__matsWidget.setContent(1, paras.jointMats)
        print 'joints mats import done'
        if(len(paras.loadingPointMats))>0:
            self.__matsWidget.setContent(2, paras.loadingPointMats)
            print 'loading points import done'
        if len(paras.waterControlPoints)>0:
            self.__matsWidget.setWaterUnitWeight(paras.waterUnitWeight)
            self.__matsWidget.setContent(3, paras.waterControlPoints)
        if paras.ifRightHand==1:
            self.__matsWidget.setEarthquakeParas(paras.sectionAngle\
                  , paras.gravityAcceleration , paras.earthquakeTimeInterval)
            self.__matsWidget.setEarthquakeMaxSteps(paras.stepsNum)
#            self.__matsWidget.setContent(4, paras.earthquakePoints)
            
        
    def __storePanelData2Database(self):
        from DDADatabase import df_inputDatabase
        paras = df_inputDatabase.paras
        paras.ifDynamic = self.__mainWidget.ui.StaticDynamicSpinB.value()
        paras.stepsNum = self.__mainWidget.ui.stepsNumSpinB.value()
        paras.ratio = self.__mainWidget.ui.maxRatioSpinB.value()
        paras.OneSteptimeLimit = self.__mainWidget.ui.timeIntervalSpinB.value()
        paras.springStiffness = self.__mainWidget.ui.springStiffnessSpinB.value()
        paras.SOR = self.__mainWidget.ui.SORSpinB.value()
        paras.ifRightHand = self.__mainWidget.ui.comboBox.currentIndex()
        
        paras.blockMats = self.__matsWidget.getContent(0)
        print 'blocks mats export done'
        paras.jointMats = self.__matsWidget.getContent(1)
        print 'joints mats export done'
        if(len(paras.loadingPointMats))>0:
            paras.loadingPointMats = self.__matsWidget.getContent(2)
            print 'loading points export done'
        #water
        paras.waterUnitWeight = self.__matsWidget.ui.waterUnitSpinB.value()
        paras.waterControlPoints = self.__matsWidget.getContent(3)
        
        #earthquake
        paras.sectionAngle = self.__matsWidget.ui.sectionAngleSpinBox.value()
        paras.gravityAcceleration = self.__matsWidget.ui.gravitySpinB.value()
        paras.earthquakeTimeInterval = self.__matsWidget.ui.timeSpinB.value()
#        paras.earthquakePoints = self.__matsWidget.getContent(4)
        
    def __saveParameters2File(self):
        '''
        save parameters to self.current_path/parameters.df,and revise df_Ff.c
        '''
        import Base
        outfile = open(Base.__currentProjectPath__+'/parameters.df',  'wb' )
        print Base.__currentProjectPath__+'/parameters.df'
        if not outfile:
            showErrorMessageBox('File open failed' , 'Can\'t open parameters.df')
            return
        
        # schema
        from DDADatabase import df_inputDatabase
        paras = df_inputDatabase.paras
        tmpUI = self.__mainWidget.ui
        outfile.write('%f\n%d\n%d\n%d\n%f\n%f\n%f\n'%(paras.ifDynamic\
                        , int(paras.stepsNum) , int(paras.blockMatsNum)\
                        , int(paras.jointMatsNum) , paras.ratio\
                        , paras.OneSteptimeLimit , paras.springStiffness))
        print 'schema store done.'
        
        # fixed points and loading points
        if len(df_inputDatabase.fixedPoints)>0:
            fps = len(df_inputDatabase.fixedPoints)
            outfile.write('0 '*fps )
            print 'fixed points : ' ,fps 
        if len(paras.loadingPointMats)>0:
            for lp in paras.loadingPointMats:
                outfile.write('%d '%len(lp))
            print 'loading points : ' , paras.loadingPointMats 
        outfile.write('\n')
        for lp in paras.loadingPointMats:
            for nums in lp:
                outfile.write( '%f %f %f\n'%tuple(nums))
        print 'fixed points and loading points materials store done.'
         
        # block materials
        for block in paras.blockMats:
            outfile.write( '%f %f %f %f %f\n%f %f %f\n%f %f %f\n%f %f %f\n'%(block[0] ,block[1] ,block[2]\
                               ,block[3] ,block[4] ,block[5] ,block[6] ,block[7] ,block[8] ,block[9] ,block[10]\
                               ,block[11] ,block[12] ,block[13]))
        print 'block materials store done.'
        
        # joints materials
        for joint in paras.jointMats:
            outfile.write( '%f %f %f\n'%(joint[0] ,joint[1] ,joint[2]))
        print 'joint materials store done.'
        
        # rest parameters
        if paras.ifRightHand==1: # right hand
            outfile.write('%s\n0 1 2\n'%str(self.__mainWidget.ui.SORSpinB.value()))
        else:
            outfile.write('%s\n0 0 0\n'%str(self.__mainWidget.ui.SORSpinB.value()))
        print 'all parameters store done.'
        
        # water
        outfile.write('%f\n%d %f\n'%(paras.sectionAngle \
                  ,len(paras.waterControlPoints) , paras.waterUnitWeight))
        for nums in paras.waterControlPoints:
            outfile.write('%f %f\n'%tuple(nums))
        outfile.close()
        
        #earthquake
        if not paras.ifRightHand: return
        self.__matsWidget.storeEarthquakeData()
        
    def accept(self):
        self.__storePanelData2Database()
        import Base
        Base.delaycommand(self.__calculateDF)

    def __calculateDF(self):
        '''
        save parameters to self.current_path/parameters.df , and then start calculation
        '''
        self.__saveParameters2File()

        print 'Calculation button pressed'
        
        def __calc():
            import FreeCADGui
            FreeCADGui.runCommand('DDA_DFCalc')
            import DDAGui
            DDAGui.setInterval4Calculation(self.__mainWidget.ui.spinB_framesInterval.value())
            
        import Base
        Base.delaycommand(__calc)        
        
    def GetResources(self):
        return {'Pixmap'  :'DF',
                'MenuText':  QtCore.QT_TRANSLATE_NOOP('DFCalculation','DFCalculation'),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DFCalculation',"DF calculation process.")}
                
    def Activated(self, name="None"):
        FreeCAD.Console.PrintMessage( 'Creator activing\n')
        if FreeCAD.activeDDACommand:
            FreeCAD.activeDDACommand.finish()
        self.doc = FreeCAD.ActiveDocument
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.featureName = name
        
        if not self.doc:
            FreeCAD.Console.PrintMessage( 'FreeCAD.ActiveDocument get failed\n')
            self.finish()
        else:
            FreeCAD.activeDDACommand = self  # FreeCAD.activeDDACommand 在不同的时间会接收不同的命令
            import Base
            Base.__currentStage__ = 'DF' 
            #self.ui.show()

        # Hide Panel
        Base.setCurrentDDACommand(self)
        self.__mainWidget.show()
        
        # clear Dcoument 
        import DDADisplay
        DDADisplay.clearDocument()
        
        
        
    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')
        
    
    def finish(self):
        pass
        
    def hideUI(self):
        self.__mainWidget.hide()
        import DDAGui
        DDAGui.clearCalculator()

FreeCADGui.addCommand('DFCalculation', DFCalculation())