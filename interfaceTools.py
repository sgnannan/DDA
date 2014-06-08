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


def calcIntersection(list1 , list2):
    '''
    calculate intersection of list1  and list2
    :param list1:
    :param list2:
    '''
    result = []
#        print 'list1 : ' , list1 , ' list2 : ' , list2
    i = j = 0
    if len(list1)>0 and len(list2)>0:
        while True:
            if list1[i] == list2[j]:
                result.append(list1[i])
                i+=1
                j+=1
            elif list1[i]>list2[j]:
                j+=1
            elif list1[i]<list2[j]:
                i+=1
            if i== len(list1) or j==len(list2):
                break
#        print 'result : ' , result
#        print '================================'
    return result

def calcUnion(list1 , list2):
    '''
    calculate intersection of list1  and list2
    :param list1:
    :param list2:
    '''
    result = []
#    print 'list1 : ' , list1 , ' list2 : ' , list2
    i = j = 0
    if len(list1)==0:
        result = list2[:]
    elif len(list2)==0:
        result = list1[:]
    else: 
        while True:
            if list1[i] == list2[j]:
                result.append(list1[i])
                i+=1
                j+=1
            elif list1[i]>list2[j]:
                result.append(list2[j])
                j+=1
            elif list1[i]<list2[j]:
                result.append(list1[i])
                i+=1                
            if i== len(list1) or j==len(list2):
                break
        if i<len(list1):
            result.extend(list1[i:])
        elif j<len(list2):
            result.extend(list2[j:])
#        print 'result : ' , result
#        print '================================'
    return result

class BlockRectangles:
    
    def __init__(self):
        self.blockRects = []
    
    def getXYRange(self,points):
        '''
        get xmin , xmax , ymin , ymax
        '''
#        xmin = points[0].x
#        xmax = points[0].x 
#        ymin = points[0].y
#        ymax = points[0].y
#        for i in range(1,len(points)):
#            if xmin>points[i].x:
#                xmin = points[i].x
#            elif xmax<points[i].x:
#                xmax = points[i].x
#            
#            if ymin>points[i].y:
#                ymin = points[i].y
#            elif ymax<points[i].y:
#                ymax = points[i].y

        xmin = points[0][0]
        xmax = points[0][0] 
        ymin = points[0][1]
        ymax = points[0][1]
        for i in range(1,len(points)):
            if xmin>points[i][0]:
                xmin = points[i][0]
            elif xmax<points[i][0]:
                xmax = points[i][0]
            
            if ymin>points[i][1]:
                ymin = points[i][1]
            elif ymax<points[i][1]:
                ymax = points[i][1]
                
        return xmin , xmax , ymin , ymax
    
    def addBlockRect(self, xmin , ymax , xmax , ymin):
        '''
        left-top and right-bottom vertex
        :param xmin:
        :param ymax:
        :param xmax:
        :param ymin:
        '''
        self.blockRects.append((xmin,ymax,xmax,ymin))

        
    def handleBlockXYRange(self,polygon):
        xmin , xmax , ymin , ymax = self.getXYRange(polygon)
        self.addBlockRect(xmin, ymax, xmax, ymin)
        
    def resetXYRange(self):
        self.blockRects = []

class LineSelection:
    def __init__(self):
        self.segments = [] # format of segments : [ ( startValue , endValue , blockNo ) ... ]
        
    def cmp(self , t):
        return t[0]  # use t[0] as base to compare
    
    def setData(self , tmpData):
        data = tmpData[:]
        data.sort(key=self.cmp)
        self.segments = data 
        
    def getIntersectedBlockNo(self , startValue , endValue):
        assert endValue > startValue
        result = []
        endIdx = self.getIndex(endValue)
        s=0
        while s<=endIdx :
            if startValue < self.segments[s][1]:
                result.append(self.segments[s][2]) # self.segments[s][2] is blockNo 
            s+=1
        result.sort()
        return result
        
    def getIndex(self , num):
        '''
        this function will find 'num''s index in 'coords'
        if 'num' is not in 'coords' , return i that coords[i]< 'num' < coords[i+1] 
        :param num:
        :param coords:
        '''
        t = len(self.segments)-1 
        while t>=0:
            if num>self.segments[t][0]:
                break
            t-=1
        return t
        
class RectangleSelection:
    def __init__(self):
        self.XSelection = LineSelection()
        self.YSelection = LineSelection()
        
    def setData(self , rects):
        XCoords , YCoords = self.convertData(rects)
        assert len(XCoords)>0 and len(YCoords)>0
        self.XSelection.setData(XCoords)
        self.YSelection.setData(YCoords)
        
    def convertData(self, rects):
        XCoords = []
        YCoords = []
        rects = self.getNormalizedRects(rects)
        for i , r in enumerate(rects):
            XCoords.append(( r[0] , r[2] , i))
            YCoords.append(( r[1] , r[3] , i ))
#        print 'rects : ' , rects
#        print 'XCoords : ' , XCoords
#        print 'YCoords : ' , YCoords
        return XCoords , YCoords
        
    def getIntersectedRectsNo(self , X1 , Y1 , X2 , Y2):
        if X1>X2:
            X1 , X2 = X2 , X1
        if Y1>Y2:
            Y1 , Y2 = Y2 , Y1
        s1 = self.XSelection.getIntersectedBlockNo(X1, X2)
        s2 = self.YSelection.getIntersectedBlockNo(Y1, Y2)
#        print 'X intersects : ' , s1
#        print 'Y intersects : ' , s2
        return calcIntersection(s1,s2)
    
    def getNormalizedRects(self , rects):
        for i , r in enumerate(rects):
            rects[i] = self.normalizeRect(r)
        return rects

    def normalizeRect(self , rect):
        '''
        rect if format of (X1 , Y1 , X2 , Y2) , this function's result will guanrantee ( X1 , Y1 ) and ( X2 , Y2)
        are left-bottom and right-top vertices
        :param rect:
        '''
        r = rect
        if rect[0] > rect[2]:
            r = ( rect[2] , rect[1] , rect[0] , rect[3])
        if rect[1] > rect[3]: # left-top and right-bottom vertices , so rect[1] > rect[3]
            r = ( rect[0] , rect[3] , rect[2] , rect[1])
        return r


rectSelection = RectangleSelection()
blocksRects = BlockRectangles()
            
            
            
##########################################################
# the following class is used to calculate border.
# R1 _R6                          R5_ R4
#    ||  J________________________I ||
#    || /                         \ ||
#    ||/                           \||
#    ||A                          H| |
#    ||                            | |
#    || B                          | |
#    | \                          G/ |
#    |  \  _____________________  /  |
#    |  C\/D                   E\/F  |
#    |_______________________________|                           
#    R2                               R3
#  in this graph . A-B-C-D-E-F-G-H-I-J is the original boundary.
#  A-R6-R1-R2-R3-R4-R5-H is the result 
##########################################################

class BorderCalculator:
    def __init__(self):
        self.up = None  # the max y
        self.down = None # the min y
        self.left = None # the min x
        self.right = None # the max x
        
        self.leftIdx = None   # index of the most left and most up point . mainly to left 
        self.rightIdx = None  # index of the most right and most up point . mainly to right
        
        self.zValue = 0 # the z value of the points in result
        
        self.marginRatio = 0.05  # the ratio of border thickness to max(self.up-self.down , self.right-self.left)

    def __updateRadius4PointsInBase(self):
        import Base
        difference = self.up - self.down
        tmp = self.right - self.left
        if difference <tmp:
            difference = tmp        
        
        Base.__radius4Points__ = difference*0.02

    def __calculateRange(self , pts):
        '''
        in the former graph , this function return the indexes of point 'A' and point 'H'
        :param points: boundary points
        '''
        self.leftIdx = 0
        self.rightIdx = 0
        self.up = pts[0][1]
        self.down = pts[0][1]
        self.left = pts[0][0]
        self.right = pts[0][0]
        for i in range(1, len(pts)):
            p = pts[i]
            if p[0]<self.left or (p[0]==self.left and p[1] > pts[self.leftIdx][1]):
                self.leftIdx = i
                self.left = p[0]
                    
            if p[0]>self.right or (p[0]==self.right and p[1] > pts[self.rightIdx][1]):
                self.rightIdx = i
                self.right = p[0]
            
            if p[1]<self.down:
                self.down = p[1]
                    
            if p[1]>self.up:
                self.up = p[1]
                
#        print 'left : %f    index  %f'%(self.left , self.leftIdx)
#        print 'right : %f    index  %f'%(self.right , self.rightIdx)
#        print 'up : %f'%self.up
#        print 'down : %f'% self.down
        self.__updateRadius4PointsInBase()

    def __calculateNewBoundaries(self , pts):
        '''
        in the former graph , this function calculate the 'A-R6-R1-R2-R3-R4-R5-H'
        the len(result) is also 8
        '''
        margin = self.right - self.left
        tmp = self.up - self.down
        if tmp>margin:
            margin = tmp
        minX = self.left - margin*self.marginRatio
        maxX = self.right + margin*self.marginRatio
        minY = self.down - margin*self.marginRatio
        maxY = self.up + margin*self.marginRatio
        
        p = pts[self.leftIdx]
        result = [(p[0] , p[1], self.zValue)]
        
        result.append((minX , pts[self.leftIdx][1] , self.zValue))
        result.append((minX , minY , self.zValue))
        result.append((maxX , minY , self.zValue))
        result.append((maxX , pts[self.rightIdx][1] , self.zValue))
        
        p = pts[self.rightIdx]
        result.append((p[0] , p[1], self.zValue))
        
        t = self.rightIdx
        while t!=self.leftIdx:
            t=(t+1)%len(pts)
            result.append((pts[t][0] , pts[t][1] , self.zValue))
        
        return result
    
    def calcualteBorder(self, pts):
        self.__calculateRange(pts)
        return self.__calculateNewBoundaries(pts)

####################################################
#
#   tunnel bolt elements generator
#     (currently only tunnel of type 2 has the bolt element generator)
#
####################################################

class TunnelBoltsGenerator:
    @staticmethod
    def generateBolts4Tunnel1(centerX , centerY , hAxesLength , vAxesLength \
                      , boltLength , boltLength2 , boltsDistance ):
        import DDACalcTools
        bolts = DDACalcTools.pyBolts()
        print bolts.size()
#        DDACalcTools.calcBolts4Type2Tunnel( float(centerX) , float(centerY) , float(hAxesLength) \
#              , float(vAxesLength) , float(boltLength) , float(boltLength2) , float(boltsDistance) , bolts)
        DDACalcTools.calcBolts4Type1Tunnel( centerX , centerY , hAxesLength \
              , vAxesLength , boltLength , boltLength2 , boltsDistance , bolts)
        
        return TunnelBoltsGenerator._convert2BoltElements(bolts)
        
    @staticmethod
    def generateBolts4Tunnel2(centerX , centerY , halfWidth , halfHeight \
                      , arcHeight , boltLength , boltLength2 , boltsDistance ):
        import DDACalcTools
        bolts = DDACalcTools.pyBolts()
        print bolts.size()
        DDACalcTools.calcBolts4Type2Tunnel( float(centerX) , float(centerY) , float(halfWidth), float(halfHeight) \
            , float(arcHeight) , float(boltLength) , float(boltLength2) , float(boltsDistance) , bolts)
        
        return TunnelBoltsGenerator._convert2BoltElements(bolts)
        
    @staticmethod
    def generateBolts4Tunnel3(centerX , centerY , hAxesLength , vAxesLength \
                      , cornerHeight , boltLength , boltLength2 , boltsDistance ):
        import DDACalcTools
        bolts = DDACalcTools.pyBolts()
        print bolts.size()
        DDACalcTools.calcBolts4Type3Tunnel( float(centerX) , float(centerY) , float(hAxesLength) , float(vAxesLength) \
            , float(cornerHeight) , float(boltLength) , float(boltLength2) , float(boltsDistance) , bolts)
        
        return TunnelBoltsGenerator._convert2BoltElements(bolts)
        
    @staticmethod
    def generateBolts4Tunnel4(centerX , centerY , radius , cornerHeight \
                      , ifRotate , boltLength , boltLength2 , boltsDistance ):
        import DDACalcTools
        bolts = DDACalcTools.pyBolts()
        print bolts.size()
        DDACalcTools.calcBolts4Type4Tunnel( float(centerX) , float(centerY) , float(radius), float(cornerHeight) \
            , float(ifRotate) , float(boltLength) , float(boltLength2) , float(boltsDistance) , bolts)
        
        return TunnelBoltsGenerator._convert2BoltElements(bolts)
        
        
    @staticmethod
    def _convert2BoltElements( bolts):
        from loadDataTools import BoltElement
        resultBolts=[]
        for bolt in bolts:
            p1 = ( bolt.startPoint.x , bolt.startPoint.y , 0 )
            p2 = ( bolt.endPoint.x , bolt.endPoint.y , 0 )
            resultBolts.append(BoltElement(p1 , p2 , 0 , 0 , 0))
            print "(%lf , %lf) (%lf , %lf)"%(bolt.startPoint.x  \
                    ,bolt.startPoint.y , bolt.endPoint.x,bolt.endPoint.y)
        return resultBolts

class ReadustCamera:
    def GetResources(self):
        return {
                'MenuText':  'adjustCamera',
                'ToolTip': "adjust camera."}
    
    def Activated(self):
        import FreeCADGui

        centerX = 20
        centerY = 5
        height = 15
        
        import Base
        windowInfo = Base.__windowInfo__
        if windowInfo!=None and len(windowInfo)==4:
            centerX = (windowInfo[0]+windowInfo[1])/2
            centerY = (windowInfo[2]+windowInfo[3])/2
            height = (windowInfo[1]-windowInfo[0])*0.75
            
        print windowInfo
        print 'camera center : ( %f , %f )'% (centerX,centerY)
        camera = '#Inventor V2.1 ascii\n\n\nOrthographicCamera {\n  viewportMapping ADJUST_CAMERA\n  position %f %f 3\n  orientation 0 0 1  0\n  aspectRatio 1\n  focalDistance 5\n  height %f\n\n}\n'%(centerX,centerY,height)
        FreeCADGui.activeDocument().activeView().setCamera(camera)        
        
    def finish(self):
        pass

import FreeCADGui  
FreeCADGui.addCommand('DDA_ResetCamera', ReadustCamera())



def dxf2DDA():
    # f = open(Base.__currentProjectPath__ + '/1.dxf')
    
    import PySide 
    import Base
    if Base.__currentProjectPath__ == None:
        Base.showErrorMessageBox('Unvalid project path', \
                                 'Select a valid project path first.')
        return
    filename = PySide.QtGui.QFileDialog.getOpenFileName(None,\
                    'Open File', Base.__currentProjectPath__, 'DXF Files (*.dxf)')
    filename = str(filename[0])

    dxfDict = {}
    
    if filename:
        f = open(filename, 'rb')
        # jointList = []
        # FixedPoint = []
        # MeasurePoint= []
        
        cou=0
        
        line = f.readline().strip()
        while line:
            line = line.strip()
            if line == "LWPOLYLINE":      
                while line:
                    line = f.readline().strip()
                    if line == "8":
                        jointLayer = f.readline().strip()
                        
                        while not jointLayer in dxfDict.keys():
                            dxfDict[jointLayer] = []
                    
                    if line == "AcDbPolyline":
                        line = f.readline().strip()
                        line = f.readline().strip()
                        strPlineNumber = int(line)
                        line = f.readline().strip()
                        closed = int(f.readline().strip())
                        line = f.readline().strip()
                        line = f.readline().strip()
                        
                        for i in range(strPlineNumber):
                            if i == 0:
                                line = f.readline().strip()
                                if line == "10":
                                    str_start_x = float(f.readline().strip())
                                line = f.readline().strip()
                                if line == "20":                                
                                    str_start_y = float(f.readline().strip())
                            else:
                                if i == 1:
                                    start_x = str_start_x
                                    start_y = str_start_y
                                line = f.readline().strip()
                                if line == "10":
                                    end_x = float(f.readline().strip())
                                line = f.readline().strip()
                                if line == "20":
                                    end_y = float(f.readline().strip())                     
                                
                                dxfDict[jointLayer].append((start_x, start_y, end_x, end_y, jointLayer))
                                
                                start_x = end_x
                                start_y = end_y
                                if i == 1:
                                    index = len(dxfDict[jointLayer]) - 1 
                        if closed:
                                dxfDict[jointLayer].append((dxfDict[jointLayer][-1][2], dxfDict[jointLayer][-1][3], dxfDict[jointLayer][index][0], dxfDict[jointLayer][index][1], jointLayer))
                        break
            if line == "LINE":
                while line:
                    line = f.readline().strip()
                    if line == "8":
                        jointLayer = f.readline().strip()
                        
                        while not jointLayer in dxfDict.keys():
                            dxfDict[jointLayer] = []                    
                            
                    if line == "AcDbLine":
                        line = f.readline().strip()
                        if line == "10":
                            start_x = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "20":
                            start_y = float(f.readline().strip())
                        line = f.readline().strip()    
                        if line == "30":
                            start_z = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "11":
                            end_x = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "21":
                            end_y = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "31":
                            end_z = float(f.readline().strip())
    
                        dxfDict[jointLayer].append((start_x, start_y, end_x, end_y, jointLayer))
                        break
    
            if line == "POINT":
    
                while line:
                    line = f.readline().strip()
                    if line == "8":
                        pointLayer = f.readline().strip()
                        
                        while not pointLayer in dxfDict.keys():
                            dxfDict[pointLayer] = []                                        
                        
                    if line == "AcDbPoint":
                        line = f.readline().strip()
                        if line == "10":                        
                            point_x = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "20":                        
                            point_y = float(f.readline().strip())
                        line = f.readline().strip()
                        if line == "30":                        
                            point_z = float(f.readline().strip())
                            
                        dxfDict[pointLayer].append((point_x, point_y, point_z))
                        break
            line = f.readline()
            cou+=1
        f.close()
        print 'line number : ', cou
    return dxfDict

import PySide

class importDXF(PySide.QtGui.QDialog):
    '''
    import dxf file to get the lines and points.
    '''
    def __init__(self,parent=None):
        PySide.QtGui.QDialog.__init__(self,parent)
        self.initUI()
        self.dxfDict = {}
        self.enumList = ["Joints","MaterialLines","BoltElements","FixPoints","LoadingPoints","MeasuredPoints","HolePoints"] 
        
    def initUI(self):
        from UIs import ui_DXFConvert
        self.ui = ui_DXFConvert.Ui_Dialog()
                
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.accepted.connect(self.write2dc)
        self.ui.pushButton.pressed.connect(self.addToTab)
        self.ui.pushButton_2.pressed.connect(self.delFromTab)
        
    def realImport(self, dxfDict):
        self.dxfDict = dxfDict    
        listItem = []        
        self.ui.dxfDict = self.dxfDict
        
        for key in self.dxfDict.keys():
            listItem.append(PySide.QtGui.QListWidgetItem(key))

        for i in range(len(listItem)):
            self.ui.listWidget.insertItem(i+1,listItem[i])
            
    def addToTab(self):
        '''
        add selected joints into the tabwidget.
        '''
        
        if not self.ui.listWidget.currentRow() >=0 \
            and self.ui.listWidget.currentRow()< self.ui.listWidget.size():
            import Base
            Base.showErrorMessageBox('Wrong Index', \
                    'Please select a joint first.')
            return

        self.ui.pushButton.pressed.disconnect(self.addToTab)
        text = str(self.ui.listWidget.currentItem().text()).strip()
        
        dialog = chooseJointType()
        dialog.exec_()
        
        if dialog.accepted:
        
            tabName = dialog.slection

            for i in range(7):
                if self.enumList[i] == tabName:
                    self.ui.tabWidget.setCurrentIndex(i)
                    flag = self.checkElements(text, i)
                    if flag == 1:
                        break
                    tempItem = PySide.QtGui.QListWidgetItem(text)
                    self.ui.tabWidget.currentWidget().children()[0].addItem(tempItem)
                    item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow()) 
                    item = None 

        self.ui.pushButton.pressed.connect(self.addToTab)
    
    def checkElements(self, text, i):
        flag = 0
        tempList = self.dxfDict[text]
        if i<3:
            for x in range(len(tempList)):
                if not len(tuple(tempList[x])) == 5:
                    import Base
                    Base.showErrorMessageBox('DataError', 'please check the DXF file, there is something else except lines in this layer!')
                    flag = 1
                    break
        else:
            for x in range(len(tempList)):
                if not len(tuple(tempList[x])) == 3:
                    import Base
                    Base.showErrorMessageBox('DataError', 'please check the DXF file, there is something else except points in this layer!')
                    flag = 1
                    break
        return flag
            
    def delFromTab(self):    
        '''
        del selected tab from tabwidget.
        '''
        listWidget = self.ui.tabWidget.currentWidget().children()[0]
        if not listWidget.currentRow() >=0 \
            and listWidget.currentRow()< listWidget.size():
            import Base
            Base.showErrorMessageBox('Wrong Index', \
                    'Please select a joint first.')
            return
        
        self.ui.pushButton_2.pressed.disconnect(self.delFromTab)
        item = listWidget.takeItem(listWidget.currentRow()) 
        text = str(item.text()).strip()
        item = None      
           
        tempItem = PySide.QtGui.QListWidgetItem(text)
        self.ui.listWidget.addItem(tempItem)
        self.ui.pushButton_2.pressed.connect(self.delFromTab)
        
    def write2dc(self):

        
        numsOfJoints = [0,0,0,0,0,0,0]          #nums of below
        
#         jointLinesNum = 0
#         materialLinesNum = 0
# 
#         boltElementsNum = 0
#         fixedPointsNum = 0
#         loadingPointsNum = 0
#         measuredPointsNum = 0
#         holePointsNum = 0
        numsOfLayers = [0,0,0,0,0,0,0] 
        
        for j in range(7):
            listWidget = self.ui.tabWidget.widget(j).children()[0]
            numOfList = listWidget.count()
            numsOfLayers[j] = numOfList
            lenth = 0
            for i in range(numOfList):
                text = str(listWidget.item(i).text()).strip() 
                lenth += len(self.dxfDict[text])
            numsOfJoints[j] = lenth
#         print "numsOfJoints:",numsOfJoints
        
        if numsOfJoints[2] > 0:
            dialog = setBoltElementParameters()
            dialog.exec_()
            elasticityModulus = float(dialog.ui.elasticityModulus)
            extensionStrength = float(dialog.ui.extensionStrength)
            Prestress = float(dialog.ui.Prestress)
            
        import Base, os
        dda_file = open(os.path.join(Base.__currentProjectPath__, 'data.dc'), 'w')
        dda_file.write("0.002\n")       #Ivan 0.0002???       
        
        dda_file.write("%d   0\n"%numsOfJoints[0])
        dda_file.write("%d\n%d\n%d\n%d\n%d\n%d\n"%tuple(numsOfJoints[1:]))

        listWidget = self.ui.tab.children()[0]
        for i in range(numsOfLayers[0]):
            text = str(listWidget.item(i).text()).strip()   
#             print "text:",text
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
#                 print "dd",listOfLayer[j]
                nums = list(listOfLayer[j][:-1])
                nums.append(i)
                dda_file.write('%lf  %lf  %lf  %lf  %s\n'%tuple(nums))   
                               
        listWidget = self.ui.tab_7.children()[0]
        for i in range(numsOfLayers[1]):
            text = str(listWidget.item(i).text()).strip()   
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                nums = list(listOfLayer[j][:-1])
                nums.append(i)
                dda_file.write('%lf  %lf  %lf  %lf  %s\n'%tuple(nums))        
        
        listWidget = self.ui.tab_6.children()[0]
        for i in range(numsOfLayers[2]):
            text = str(listWidget.item(i).text()).strip()   
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                dda_file.write('%lf  %lf  %lf  %lf'%tuple(listOfLayer[j][:4]))                  
                dda_file.write('  %lf  %lf  %lf\n'%(elasticityModulus,extensionStrength,Prestress))         
        listWidget = self.ui.tab_2.children()[0]
        for i in range(numsOfLayers[3]):
            text = str(listWidget.item(i).text()).strip()   
#             print "text2:",text
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                dda_file.write('%lf  %lf  %lf  %lf\n'%(listOfLayer[j][0],listOfLayer[j][1],listOfLayer[j][0],listOfLayer[j][1]))          
        
        listWidget = self.ui.tab_3.children()[0]
        for i in range(numsOfLayers[4]):
            text = str(listWidget.item(i).text()).strip()   
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                dda_file.write('%lf  %lf\n'%(listOfLayer[j][0],listOfLayer[j][1]))     
                
        listWidget = self.ui.tab_4.children()[0]
        for i in range(numsOfLayers[5]):
            text = str(listWidget.item(i).text()).strip()   
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                dda_file.write('%lf  %lf\n'%(listOfLayer[j][0],listOfLayer[j][1]))  
                
        listWidget = self.ui.tab_5.children()[0]
        for i in range(numsOfLayers[6]):
            text = str(listWidget.item(i).text()).strip()   
            listOfLayer = self.dxfDict[text]
            for j in range(len(listOfLayer)):
                dda_file.write('%lf  %lf\n'%(listOfLayer[j][0],listOfLayer[j][1]))                                      

        dda_file.close()
        
    def findIndex(self, text):
        tabIndex = -1
        count = self.tabWidget.count()
        for i in range(count):
            if text == self.tabWidget.tabText(i):
                tabIndex = i
                break
        return tabIndex
    
    
            
class chooseJointType(PySide.QtGui.QDialog):
    '''
    choose the type of joints.
    '''
    def __init__(self,parent=None):
        PySide.QtGui.QDialog.__init__(self,parent)
        self.initUI()
        self.initConnections()
        self.slection = None

    def initUI(self):
        from UIs import ui_type
        self.ui = ui_type.Ui_Dialog()
                
        self.ui.setupUi(self)
        self.ui.radioButton_3.setChecked(True)
        self.buttonContent = self.ui.radioButton_3.text()
        
    def initConnections(self):
        self.ui.radioButton.clicked.connect(self.radioChanged)
        self.ui.radioButton_2.clicked.connect(self.radioChanged)
        self.ui.radioButton_3.clicked.connect(self.radioChanged)
        self.ui.radioButton_4.clicked.connect(self.radioChanged)
        self.ui.radioButton_5.clicked.connect(self.radioChanged)
        self.ui.radioButton_6.clicked.connect(self.radioChanged)
        self.ui.radioButton_7.clicked.connect(self.radioChanged)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.accepted.connect(self.setValue)
        
    def radioChanged(self):
        if self.ui.radioButton.isChecked():
            self.buttonContent = self.ui.radioButton.text()
        elif self.ui.radioButton_2.isChecked():
            self.buttonContent = self.ui.radioButton_2.text()
        elif self.ui.radioButton_3.isChecked():
            self.buttonContent = self.ui.radioButton_3.text()
        elif self.ui.radioButton_4.isChecked():
            self.buttonContent = self.ui.radioButton_4.text()
        elif self.ui.radioButton_5.isChecked():
            self.buttonContent = self.ui.radioButton_5.text()            
        elif self.ui.radioButton_6.isChecked():
            self.buttonContent = self.ui.radioButton_6.text()
        elif self.ui.radioButton_7.isChecked():
            self.buttonContent = self.ui.radioButton_7.text()
            
    def setValue(self):
        self.slection = self.buttonContent
        
class setBoltElementParameters(PySide.QtGui.QDialog):
    '''
    set the parameters if num of boltElements not zero.
    '''
    def __init__(self,parent=None):
        PySide.QtGui.QDialog.__init__(self,parent)
        self.initUI()

    def initUI(self):
        from UIs import ui_boltElement
        self.ui = ui_boltElement.Ui_parameters()
                
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
