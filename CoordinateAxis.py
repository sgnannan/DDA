'''
Created on 2014-1-14

@author: laine
'''
from pivy import coin
__baseColor__ = coin.SoBaseColor()
__baseColor__.rgb.setValue( 0.0 , 0.0 , 0.0 )

from pivy import coin
class _CoordinateAxis:
    '''
    this class is used to show a coordiante axis
    '''
    def __init__(self):
        self.__xMin = None
        self.__xMax = None
        self.__yMin = None
        self.__yMax = None
        self.__graphTitle = None
        self.__texts = []
        self.__AxisWidth = 400
        self.__AxisHeight = 300
        self.__scalesNum4XAxis = 20
        
        self.__hintTexts = []
        self.__hintColors = []

        self.__root = coin.SoSeparator()
        #################################
        # geomerty member
        #################################
        self.__axis = coin.SoSeparator() 
        self.__root.addChild(self.__axis)
        self.__axis.addChild(__baseColor__)
        self.__lineCoords = coin.SoCoordinate3()
        self.__axis.addChild(self.__lineCoords) 
        self.__lineset = coin.SoLineSet()
        self.__axis.addChild(self.__lineset)
        
        ################################
        #  texts
        ################################
        self.__rootTexts = coin.SoSeparator()
        self.__root.addChild(self.__rootTexts)
        
        
    def setXValues(self,xMin , xMax):
        self.__xMax = xMax
        self.__xMin = xMin
        
    def setYValues(self,yMin , yMax):
        self.__yMax = yMax
        self.__yMin = yMin
        
    def setAxisWidth(self , w):
        self.__AxisWidth = w
        
    def setAxisHeight(self , h):
        self.__AxisHeight = h
        
    def setGraphTitle(self , title):
        self.__graphTitle = title
        
    def setHintTextAndColors(self,texts , colors):
        '''
        the texts on right-top corner to explain the graph
        '''
        self.__hintTexts = texts
        self.__hintColors = colors

    def __createGraphTitle(self):
        font = coin.SoFont()
        font.name.setValue('Times-Roman')
        font.size.setValue(16)
        
        g = coin.SoSeparator()
        
        # translation
        t = coin.SoTranslation()
        t.translation.setValue( self.__AxisWidth/2 , self.__AxisHeight*1.1 , 0 )
        g.addChild(t)
        
        # color
        g.addChild(__baseColor__)
        
        #font
        g.addChild(font)
    
        # text
        text = coin.SoText3()
        text.string = self.__graphTitle
        text.justification = coin.SoText3.CENTER
        g.addChild(text)
        self.__root.addChild(g)       
        

    def __createAxis(self):
        # add herizonal and veritcal axis
        pts = [ (0,0,0),(self.__AxisWidth*1.05,0,0) \
              , (0,0,0),(0,self.__AxisHeight*1.05,0) ]

        # add arrows
        scaleLen =self.__AxisWidth/self.__scalesNum4XAxis
        pts.append((self.__AxisWidth*1.05         ,        0,0))
        pts.append((self.__AxisWidth*1.05-scaleLen, scaleLen,0))
        pts.append((self.__AxisWidth*1.05         ,        0,0))
        pts.append((self.__AxisWidth*1.05-scaleLen,-scaleLen,0))
        pts.append((0         , self.__AxisHeight*1.05          ,0))
        pts.append((scaleLen  , self.__AxisHeight*1.05-scaleLen ,0))
        pts.append((0         , self.__AxisHeight*1.05          ,0))
        pts.append((-scaleLen , self.__AxisHeight*1.05-scaleLen ,0))
        
        # add scales
        for i in range(self.__AxisWidth/scaleLen):
            pts.append(( i*scaleLen , 0         ,0 ))
            pts.append(( i*scaleLen , scaleLen  ,0 ))
            
        for i in range(self.__AxisHeight/scaleLen):
            pts.append(( 0        , i*scaleLen  ,0 ))
            pts.append(( scaleLen , i*scaleLen  ,0 ))
            
        self.__lineCoords.point.setValues(0,len(pts) , pts) 
        nums =[2]* (len(pts)/2)
        self.__lineset.numVertices.setValues(0,len(nums),nums)

    def __createTexts(self):
        font = coin.SoFont()
        font.name.setValue('Times-Roman')
        font.size.setValue(9)
        
        scaleLen = self.__AxisWidth/self.__scalesNum4XAxis
        # add x scales
        flag = False
        if self.__xMax-self.__xMin>10: flag = True
        nums = self.__AxisWidth/scaleLen
        for i in range(nums):
            g = coin.SoSeparator()
            # translation
            t = coin.SoTranslation()
            t.translation.setValue(i*scaleLen , -scaleLen*(i%3+1) , 0 )
            g.addChild(t)
            
            # color
            g.addChild(__baseColor__)
            
            #font
            g.addChild(font)
        
            # text
            text = coin.SoText3()
            if flag :
                text.string = '%d'%int((self.__xMax-self.__xMin)*i/nums)
            else:
                text.string = '%.4lf'%((self.__xMax-self.__xMin)*i/nums)
            text.justification = coin.SoText3.RIGHT
            g.addChild(text)
            self.__rootTexts.addChild(g)

        # add y scales
        nums = self.__AxisHeight/scaleLen
        for i in range(nums):
            g = coin.SoSeparator()
            
            # translation
            t = coin.SoTranslation()
            t.translation.setValue(-scaleLen , i*scaleLen , 0 )
            g.addChild(t)
            
            # color
            g.addChild(__baseColor__)
            
            #font
            g.addChild(font)
        
            # text
            text = coin.SoText3()
            text.string = '%.4lf'%(self.__yMin+(self.__yMax-self.__yMin)*i/nums)
            text.justification = coin.SoText3.RIGHT
            g.addChild(text)
            self.__rootTexts.addChild(g)       
            
    def __createHintTextsAndColors(self):
        rootHint = coin.SoSeparator()
        
        # hint lines
        colorLines = coin.SoSeparator()
        rootHint.addChild(colorLines)
        mat = coin.SoMaterial()
        mat.diffuseColor.setValues(0,len(self.__hintColors) , self.__hintColors)
        colorLines.addChild(mat)
        bind = coin.SoMaterialBinding()
        bind.value = coin.SoMaterialBinding.PER_PART
        colorLines.addChild(bind)

        lineCoords = coin.SoCoordinate3()
        colorLines.addChild(lineCoords) 
        lineset = coin.SoLineSet()
        colorLines.addChild(lineset)
        space = self.__AxisHeight/self.__scalesNum4XAxis

        startX = self.__AxisWidth*1.05
        pts = []
        for i , s in enumerate(self.__hintTexts):
            pts.append((startX         , self.__AxisHeight-i*space , 0))
            pts.append((startX + space , self.__AxisHeight-i*space , 0))
            
        lineCoords.point.setValues(0,len(pts) , pts) 
        nums =[2]* (len(pts)/2)
        lineset.numVertices.setValues(0,len(nums),nums)
        
        # add texts
        font = coin.SoFont()
        font.name.setValue('Times-Roman')
        font.size.setValue(9)
        scaleLen = self.__AxisHeight/self.__scalesNum4XAxis
        for i in range(len(self.__hintColors)):
            g = coin.SoSeparator()
            
            # translation
            t = coin.SoTranslation()
            t.translation.setValue(startX+space*2 , self.__AxisHeight-i*space , 0 )
            g.addChild(t)
            
            # color
            col = coin.SoBaseColor()
            col.rgb.setValue(self.__hintColors[i][:3])
            g.addChild(col)
            
            #font
            g.addChild(font)
        
            # text
            text = coin.SoText3()
            text.string = self.__hintTexts[i]
            text.justification = coin.SoText3.LEFT
            g.addChild(text)
            rootHint.addChild(g)       
        
        self.__root.addChild(rootHint)
        
            
    def createAxis(self):
        self.__createAxis()
        self.__createTexts()
        self.__createHintTextsAndColors()
        self.__createGraphTitle()
        return self.__root
    
def addAxis2Scene(rootScene , xMin , xMax , yMin , yMax , graphTitle , hintTexts , hintColors, axisWidth=400 , axisHeight=300):
    axis = _CoordinateAxis()
    axis.setAxisWidth(axisWidth)
    axis.setAxisHeight(axisHeight)
    axis.setXValues(xMin,xMax)
    axis.setYValues(yMin,yMax)
    axis.setHintTextAndColors(hintTexts, hintColors)
    axis.setGraphTitle(graphTitle)
    axisNode = axis.createAxis()
    
    rootScene.addChild(axisNode)