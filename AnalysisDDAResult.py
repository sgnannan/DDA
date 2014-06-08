'''
Created on 2014-1-10

@author: laine
'''
from CoordinateAxis import __baseColor__
from PyQt4 import QtCore , QtGui

####################################################
# the next two numbers are used when showing plots
####################################################
__graphWidth__ = 400.0
__graphHeight__ = 300.0


def convertStrs2Floats(nums):
    res = []
    for num in nums:
        res.append(float(num))
    return res

def checkFile(file):
    import os
    if not os.path.exists(file):
        import Base
        Base.showErrorMessageBox('FileError', 'file \"%s\" not found'%file)
        return False
    return True
        
def getMinAndMax(xLists , yLists):
    xMins = []
    xMaxs = []
    for nums in xLists:
        xMins.append(min(nums))
        xMaxs.append(max(nums))
    
    yMins =[]
    yMaxs =[]
    for nums in yLists:
        yMins.append(min(nums))
        yMaxs.append(max(nums))
        
    print min(xMins) , max(xMaxs) , min(yMins) , max(yMaxs)
    return min(xMins) , max(xMaxs) , min(yMins) , max(yMaxs)
        
def scaleVertices2Axis(values , min , max , AxisLen ):
    nums = []
    gap = max-min
    for v in values:
        t = v-min
        if gap*AxisLen==0:
            a=4
        tmp = t/gap*AxisLen
        assert(tmp>=0)
        nums.append(tmp)
    return nums
        
        
class DGAnalysiser:
    def __init__(self):
        self.__ifUseExistingData = True
        self.__ifAnalysesDisplacement = False
        self.__ifAnalysesMPs = False
        self.__ifAnalysesStress = False
        
        self.__graph = None
        self.__axisNodes = None
        
        self.__times = [] # a list contains real times at each step
        self.__stresses = [] # a list contains stress for one block at each step
        self.__MPDists = [] # a list contains distance for every measured points at each step
        self.__displacements=[]
        self.__blockNumber = 0
        
        # this toolbar is used to show current point 
        self.__toolbar = None
        self.__callDisplacement = None
        self.__callMP = None
        self.__callStress = None
        self.__docDisplacement = None
        self.__docMP = None
        self.__docStress = None 
        
        self.__displacementsRange = [] # min , max
        self.__MPRange = [] # min , max
        self.__stressRange = [] # min , max
        self.__timeRange = [] # min , max
        
        self.__timeFile = 'time.dg'
        self.__MPDistFile = 'measuredPoints.dg'
        self.__stressFile = 'stress.dg'
        self.__displacementFile = 'displacement.dg'
        
        import Base
        self.__projectPath = Base.__currentProjectPath__
        
    def __del__(self):
        del self.__graph
        
    def loadData(self ):
        self.__loadTimes()
        if self.__ifAnalysesDisplacement:   self.__loadDisplacement()
        if self.__ifAnalysesMPs         :   self.__loadMPDists()
        if self.__ifAnalysesStress      :   self.__loadStress()
    
    def setUseExistingData(self, flag):
        import os , Base
        path = Base.__currentProjectPath__
        if flag:
            if not checkFile(os.path.join(path,'time.dg')):
                return False
            if self.__ifAnalysesDisplacement and not checkFile(os.path.join(path,'time.dg')):
                return False
            if self.__ifAnalysesDisplacement and not checkFile(os.path.join(path,'displacement.dg')):
                return False
            if self.__ifAnalysesStress and not checkFile(os.path.join(path,'allStress.dg')):
                return False
            if self.__ifAnalysesMPs and not checkFile(os.path.join(path,'measuredPoints.dg')):
                return False
            self.__ifUseExistingData = True
        else:
            self.__ifUseExistingData = False
            
            
    
    def setAnalysesDisplacement(self,flag):
        self.__ifAnalysesDisplacement = flag
        
    def setAnalysesMPs(self,flag):
        self.__ifAnalysesMPs = flag
        
    def setAnalysesStress(self,flag):
        self.__ifAnalysesStress = flag    
    
    def setBlockNumber(self, number):
        self.__blockNumber = number
    
    def __loadTimes(self):
        import os
        self.__times = []
        f = open(os.path.join(self.__projectPath, self.__timeFile),'rb')
        self.__times = convertStrs2Floats(f.readlines())
        f.close()
        
    def __loadMPDists(self):
        import os
        self.__MPDists=[]
#        if not self.__ifUseExistingData:
#            f = open(os.path.join(self.__projectPath, self.__MPDistFile) , 'rb')
#            for line in f.readlines():
#                self.__MPDists.append(convertStrs2Floats(line.split()))
#            f.close()
#        else:
        f = open(os.path.join(self.__projectPath, self.__MPDistFile) , 'rb')
        lines = f.readlines()
        f.close()
        mpDists = self.__MPDists
        MPsNumber = len(lines[0].split())
        for i in range(MPsNumber):
            mpDists.append([])
        for line in lines:
            nums = line.split()
            for i , num in enumerate(nums):
                mpDists[i].append(num)
        for i in range(MPsNumber):
            mpDists[i] = convertStrs2Floats(mpDists[i])
                    
        print 'len1 %d , len2 %d'%(len(self.__MPDists),len(self.__MPDists[0]))
        
    def __loadDisplacement(self):
        import os
        self.__displacements=[]
        f = open(os.path.join(self.__projectPath,self.__displacementFile) , 'rb')
        self.__displacements = convertStrs2Floats(f.readlines())
        f.close()

    def __loadStress(self):
        import os
        neededStress = []
        if self.__ifUseExistingData:
            f = open(os.path.join(self.__projectPath, 'allStress.dg') , 'rb')
            lines = f.readlines()
            framesNum = len(open(os.path.join(self.__projectPath, self.__timeFile) , 'rb').readlines())
            blocksNum = len(lines)/framesNum
            assert blocksNum*framesNum == len(lines)
            for i,line in enumerate(lines):
                if i%blocksNum==self.__blockNumber:
                    neededStress.append(line)
        else:
            neededStress = open(os.path.join(self.__projectPath, self.__stressFile) , 'rb').readlines() 
         
        self.__stresses=[]
        for line in neededStress:
            nums = line.split()
            self.__stresses.append((float(nums[0]),float(nums[1]),float(nums[2])))

    def showPolyLine(self, docName , shapeName , pts , color ):
#        import Part
#        assert len(color)==4
#        from FreeCAD import Vector
#        res = []
#        for p in pts:
#            res.append(Vector(p[0],p[1],0))
#        
#        import Base
#        Base.addStatisticLine2Document(docName , shapeName, res, color)

        import Graph
        assert self.__graph
        self.__graph.showStatisticsLine(docName, shapeName, pts, color)


    
    def addAxisForDoc(self , DocName , xMin , xMax , yMin , yMax , title , texts , colors):
        # add coordinate axis    
        import FreeCADGui
        from pivy import coin
        self.__axisNodes = []
        node = coin.SoSeparator()
            
        try:
            sg = FreeCADGui.getDocument(DocName).ActiveView.getSceneGraph()
        except:
            raise
        from CoordinateAxis import addAxis2Scene
        sg.addChild(node)
        self.__axisNodes.append((sg, node))
        addAxis2Scene(node ,xMin , xMax , yMin , yMax , title , texts, colors)
        
    def clearAxises(self):
        for node in self.__axisNodes:
            node[0].removeChild(node[1])
    
    def showDisplacement(self):
        assert len(self.__times) == len(self.__displacements)
        # add Coordiante axis
        xMin , xMax , yMin , yMax = getMinAndMax([self.__times], [self.__displacements])
        self.__displacementsRange = [yMin , yMax]
        self.__timeRange = [xMin , xMax]
        xValues = scaleVertices2Axis(self.__times, xMin, xMax, __graphWidth__)
        yValues = scaleVertices2Axis(self.__displacements, yMin, yMax, __graphHeight__)
        self.addAxisForDoc('Displacement', xMin, xMax, yMin, yMax,'Max displacement for each time' \
                           , ['Displacement'], [(0.0,0.0,0.0,1.0)])
        pts = [(k,v , 0) for k,v in zip(xValues , yValues)]
        self.showPolyLine('Displacement','Displacement' , pts , (0.0,0.0,0.0,1.0))
        
        import Base
        Base.ViewFitScene('Displacement')

    def showStress(self):
        assert len(self.__times) == len(self.__stresses)
        texts = ['StressX' , 'StressY' , 'StressXY']
        colors = [(1.0,0.0,0.0,1.0),(0.0,1.0,0.0,1.0),(0.0,0.0,1.0,1.0)]
        tmp1 = [p[0] for p in self.__stresses]
        tmp2 = [p[1] for p in self.__stresses]
        tmp3 = [p[2] for p in self.__stresses]

        # add Coordiante axis
        xMin , xMax , yMin , yMax = getMinAndMax([self.__times], [tmp1,tmp2,tmp3])
        self.__stressRange = [yMin , yMax]
        self.__timeRange = [xMin , xMax]
        times = scaleVertices2Axis(self.__times, xMin, xMax, __graphWidth__)
        self.addAxisForDoc('Stress', xMin, xMax, yMin, yMax , 'Stress graph for block %d'%self.__blockNumber , texts , colors )
        
        tmp1 = scaleVertices2Axis(tmp1, yMin, yMax, __graphHeight__)
        pts1 = [(k,v,0) for k,v in zip(times , tmp1)]
        tmp2 = scaleVertices2Axis(tmp2, yMin, yMax, __graphHeight__)
        pts2 = [(k,v,0) for k,v in zip(times , tmp2)]
        tmp3 = scaleVertices2Axis(tmp3, yMin, yMax, __graphHeight__)
        pts3 = [(k,v,0) for k,v in zip(times , tmp3)]
        
        self.showPolyLine('Stress' , texts[0] , pts1, colors[0])
        self.showPolyLine('Stress' , texts[1] , pts2, colors[1])
        self.showPolyLine('Stress' , texts[2] , pts3, colors[2])
       
        import Base
        Base.ViewFitScene('Stress')

    def showMPDists(self):
        if len(self.__MPDists)==0:
            return
        assert len(self.__times) == len(self.__MPDists[0])

        xMin , xMax , yMin , yMax = getMinAndMax([self.__times], self.__MPDists)
        self.__MPRange = [yMin , yMax]
        self.__timeRange = [xMin , xMax]

        MPs = []
        times = scaleVertices2Axis(self.__times, xMin, xMax, __graphWidth__)
        for line in self.__MPDists:
            ts = scaleVertices2Axis(line, yMin, yMax, __graphHeight__)
            pts = [(k,v,0) for k,v in zip(times , ts)]
            if len(pts)>0:  MPs.append(pts)
        
        if len(MPs)==0:  return
        
        colors = []
        slice = 1/float(len(MPs))
        texts = []
        for i in range(len(MPs)):
            texts.append('MeasuredPoint%d'%i)
            t = i*slice
            if t<=0.33:     
                colors.append( (1.0, t/0.33 , 0.0, 1.0) )
            elif t<=0.67:
                tmp = t - 0.33   
                colors.append( (1.0-tmp/0.33 , 1.0 , tmp/0.33 , 1.0 ) )
            else:
                tmp = t-0.67
                colors.append( (0.0 , 1.0-tmp/0.33 , 1.0 , 1.0) )

        self.addAxisForDoc('MeasuredPoints', xMin, xMax, yMin, yMax,'Measured Points Displacemnts'\
                          , texts , colors)

        
        for i in range(len(colors)):
            self.showPolyLine('MeasuredPoints' , texts[i], MPs[i], colors[i])

        import Base
        Base.ViewFitScene('MeasuredPoints')
            
    def action(self, arg):
        return
        import FreeCADGui
        if arg["Type"] == "SoLocation2Event":  # mouse movement detection
            self.getDocuments()
            doc = FreeCADGui.ActiveDocument
            point = doc.ActiveView.getPoint(arg["Position"][0], arg["Position"][1])
            point.x = point.x/__graphWidth__*(self.__timeRange[1]-self.__timeRange[0])
#            point.y = self.__displacementsRange[0]\
#                + point.y/__graphHeight__*(self.__displacementsRange[1] \
#                                            -self.__displacementsRange[0])
            if doc == self.__docDisplacement:
                point.y = self.__displacementsRange[0]\
                    + point.y/__graphHeight__*(self.__displacementsRange[1] \
                                                -self.__displacementsRange[0])
            elif doc == self.__docMP:
                point.y = self.__MPRange[0] \
                    +point.y/__graphHeight__*(self.__MPRange[1]-self.__MPRange[0])
            elif doc == self.__docStress:
                point.y = self.__stressRange[0] \
                    +point.y/__graphHeight__*(self.__stressRange[1]-self.__stressRange[0])
            self.__toolbar.displayPoint(point)

    def tryToGetDocument(self, docName , createIfNotExist=False):
        import FreeCAD , FreeCADGui
        doc = None
        try:
            doc = FreeCADGui.getDocument(docName)
        except:
            if createIfNotExist:
                FreeCAD.newDocument(docName)
                doc =  FreeCADGui.getDocument(docName)
                #print 'create doc %s'%docName
            else:
                doc = None
        return doc
        

    def getDocuments(self , createIfNotExist=False):
        if self.__ifAnalysesDisplacement:  self.__docDisplacement = self.tryToGetDocument('Displacement',createIfNotExist)
        if self.__ifAnalysesMPs         :  self.__docMP = self.tryToGetDocument('MeasuredPoints',createIfNotExist)
        if self.__ifAnalysesStress      :  self.__docStress = self.tryToGetDocument('Stress',createIfNotExist)

    def showAnalysis(self):
        import Base, Graph
        # graph must be new, to clear former polylines
        if self.__graph:
            self.__graph.clearLines()
            self.clearAxises()
        else:  
            self.__graph = Graph.AnalysisGraph()

        print '111  ' , Base.getCurrentTime()
        if self.__ifAnalysesDisplacement: self.showDisplacement()
        print '222  ' , Base.getCurrentTime()
        if self.__ifAnalysesMPs         : self.showMPDists()
        print '333  ' , Base.getCurrentTime()
        if self.__ifAnalysesStress      : self.showStress()
        print '444  ' , Base.getCurrentTime()


    def setupToolbar(self):
        from DDAToolbars import LineToolbar
        if not self.__toolbar:
            self.__toolbar = LineToolbar(False)
            self.__toolbar.on()
        else:
            self.__toolbar.on()

        self.getDocuments(True)
        # try to find related view and add event callback
        import FreeCADGui
        #doc = FreeCADGui.getDocument('Displacement')
#        doc = FreeCADGui.ActiveDocument
#        if doc: self.__callDisplacement = doc.ActiveView.addEventCallback("SoEvent", self.action)
#        return
    
        if self.__docDisplacement: self.__docDisplacement = self.__docDisplacement.ActiveView.addEventCallback("SoEvent", self.action)
        if self.__docMP: self.__callMP = self.__docMP.ActiveView.addEventCallback("SoEvent", self.action)
        if self.__docStress: self.__callStress = self.__docStress.ActiveView.addEventCallback("SoEvent", self.action)
        
    def uninstallToolbar(self):
        if self.__toolbar:
            self.__toolbar.offUi()
            
        # try to find related view and add event callback
#        import FreeCADGui
#        FreeCADGui.ActiveDocument.removeEventCallback("SoEvent", self.__callDisplacement)
#        return
        self.getDocuments()
        doc = FreeCADGui.getDocument('Displacement')
        if self.__callDisplacement: 
            self.__docDisplacement.ActiveView.removeEventCallback("SoEvent", self.__callDisplacement)
            self.__callDisplacement = None
        if self.__callMP:
            self.__docMP.ActiveView.removeEventCallback("SoEvent", self.__callMP)
            self.__callMP = None
        if self.__callStress: 
            self.__docStress.ActiveView.removeEventCallback("SoEvent", self.__callStress)
            self.__callStress = None
        
    def closeDocuments(self):
        import FreeCAD
        FreeCAD.closeDocument('Displacement')
        FreeCAD.closeDocument('MeasuredPoints')
        FreeCAD.closeDocuemnt('Stress')
      
class Ui_DGAnalysiser(QtGui.QDialog):
    '''
    DF Calculation Process 
    '''
    def __init__(self, owner,parent=None ):
        QtGui.QWidget.__init__(self,parent)
        self.initUI(owner)
        
    
    def initUI(self , owner):
        from UIs import ui_AnalysisResult
        self.ui = ui_AnalysisResult.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(owner.accepted)
        
        
class DGAnalysiserCmd:
    '''
    choose workbench for DDA
    '''
    def __init__(self):
        self.__analysiser = None
        self.__ui = None
        
    def GetResources(self):
        return {'Pixmap'  :'plot',
                'MenuText': QtCore.QT_TRANSLATE_NOOP('DDA_DGAnalysiser',"Analyses DG result"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_DGAnalysiser',"Analyses DG result")}

    def Activated(self):
        import FreeCAD
        if FreeCAD.activeDDACommand:
            FreeCAD.activeDDACommand.finish()

        import Base , os
        filename = os.path.join(Base.__currentProjectPath__,'data.dg')
        if not os.path.isfile(filename):
            Base.showErrorMessageBox('FileNotFound'\
                    , 'File \'data.dg\' not found at project path')
            self.Deactivated()
            return
        
        import Base
        Base.changeStage('DC')
        FreeCADGui.runCommand('DDA_DisplayDFInputGraph')
        
        FreeCADGui.runCommand("Std_ViewFitAll")
        
        if not self.__ui:
            self.initUi(filename)
        self.__ui.show()

    def initUi(self,filename):
        self.__ui = Ui_DGAnalysiser(self)
        f = open(filename , 'rb')
        blocksNum = int(f.readline().split()[0])
        f.close()
        self.__ui.ui.spinBox_No.setMaximum(blocksNum-1)
        self.__ui.ui.spinBox_No.setMinimum(0)
        self.__ui.ui.spinBox_No.setSingleStep(1)
        self.__ui.ui.spinBox_No.valueChanged.connect(self.__updateColor)
        
    def __updateColor(self , No):
        import FreeCAD
        from DDADatabase import df_inputDatabase
        colors = [( 0.0 , 0.4 , 0.4 , 1.0 )]*len(df_inputDatabase.blocks)
        colors[No] = ( 0.0 , 0.8 , 0.0 , 1.0 )
        FreeCAD.getDocument('DDA').getObject('Block').ViewObject.DiffuseColor = colors

    def __stopAnalysis(self):
        self.__stopAnalysisFlag = True
        
    def __setStopAnalysisFlag(self, flag):
        self.__stopAnalysisFlag = flag
        
    def __getStopAnalysisFlag(self):
        return self.__stopAnalysisFlag
        
    def accepted(self):
        import Base
        from extractDGData import DGExtracter
        import os
        from PySide import QtCore, QtGui
        bar = QtGui.QProgressDialog('extracting data...','stop Analysis' , 0 , 100 , None , QtCore.Qt.WindowModal)
        bar.canceled.connect(self.__stopAnalysis)
        bar.setValue(0)
        bar.setVisible(True)
        
        self.__setStopAnalysisFlag(False)
        if not self.__ui.ui.checkBox_useExistingData.isChecked():
            extracter = DGExtracter()
            extracter.setFile(os.path.join(Base.__currentProjectPath__,'data.dg'))
            if self.__ui.ui.checkBox_stress.isChecked(): extracter.saveStress4Block(self.__ui.ui.spinBox_No.value())
            extracter.setSaveMPMovements(self.__ui.ui.checkBox_MP.isChecked())
            extracter.setSaveDists(self.__ui.ui.checkBox_displacement.isChecked())
            print 'extracting data  ' , Base.getCurrentTime()
            extracter.extractData()
            print 'extracting data done  ' , Base.getCurrentTime()
            if self.__getStopAnalysisFlag(): return
            bar.setValue(20)
            bar.setLabelText('outputing data...')
            print 'outputing extracting data  ' , Base.getCurrentTime()
            extracter.outputExtractedData()
            print 'outputing extracting data done  ' , Base.getCurrentTime()
            if self.__getStopAnalysisFlag(): return
        bar.setValue(40)
        
       
        if not self.__analysiser: 
            self.__analysiser = DGAnalysiser()
        else:
            self.__analysiser.uninstallToolbar()
        self.__analysiser.setAnalysesDisplacement(self.__ui.ui.checkBox_displacement.isChecked())
        self.__analysiser.setAnalysesMPs(self.__ui.ui.checkBox_MP.isChecked())
        self.__analysiser.setAnalysesStress(self.__ui.ui.checkBox_stress.isChecked())
        self.__analysiser.setBlockNumber(self.__ui.ui.spinBox_No.value())
        self.__analysiser.setUseExistingData(self.__ui.ui.checkBox_useExistingData.isChecked())
        bar.setLabelText('loading outputed data...')
        print 'loading data   ' , Base.getCurrentTime()
        self.__analysiser.loadData()
        print 'loading data  done   ' , Base.getCurrentTime()
        if self.__getStopAnalysisFlag(): return
        bar.setValue(50)
        bar.setLabelText('analysesing and showing data...')
        self.__analysiser.setupToolbar()
        print 'show analysising ' , Base.getCurrentTime()
        self.__analysiser.showAnalysis()
        print 'show analysising done ' , Base.getCurrentTime()
        bar.setValue(100)
                
    def finish(self):
        self.__analysiser.uninstallToolbar()
        self.__analysiser.closeDocuments()
        self.__ui.hide()

    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')

    def Deactivated(self):
        import FreeCAD
        self.finish()
        FreeCAD.activeDDACommand=None
        
import FreeCADGui
FreeCADGui.addCommand('DDA_DGAnalysiser', DGAnalysiserCmd())
#dgAnalysis = DGAnalysiser()
#dgAnalysis.loadData()
#dgAnalysis.showDisplacement()
#dgAnalysis.showMPDists()
#dgAnalysis.showStress()
#dgAnalysis.setupToolbar()