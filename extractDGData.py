'''
Created on 2014-1-10

@author: laine

this file is used to extract data from data.dg file
1. block stress for specific block identified by number
2. safety factor
3. measured points movement 
'''

# coding=gbk

filename = 'D:/DDAProject/data.dg'
from math import sqrt
class DGExtracter:
    def __init__(self):
        self.__blocksNum = 0
        self.__verticesNum = 0
        self.__graphsNum = 0
        self.__boltsNum = 0
        self.__fixedPointsNum = -1
        self.__measuredPointsNum = -1
        self.__loadingPointsNum = -1
        self.__fileName = None
        self.__file = None
        
        self.__lastMPs = []
        self.__MPDists = []
        self.__safetyFactors = []
        self.__stress = []
        self.__realTimes = []
        self.__realDists = []
        self.__ifSaveMPMovements = False
        self.__ifSaveDists = False
        self.__ifSaveSafetyFacotr = False
        self.__SaveStressBlockNum = -1
        
    def setFile(self , filename):
        self.__fileName = filename
    
    def saveStress4Block(self , idx=-1):
        self.__SaveStressBlockNum = idx
        
    def setSaveMPMovements(self, flag):
        self.__ifSaveMPMovements = flag
        
    def setSaveDists(self,flag):
        self.__ifSaveDists=flag
    
    def outputExtractedData(self):
        import os
        import Base
        ofTime = open(os.path.join(Base.__currentProjectPath__,'time.dg'),'wb')
        for t in self.__realTimes:
            ofTime.write('%lf\n'%t)
        ofTime.close()
        
        if self.__ifSaveMPMovements and len(self.__MPDists)>0 and len(self.__MPDists[0])>0:
            ofMPs = open(os.path.join(Base.__currentProjectPath__,'measuredPoints.dg') , 'wb')
            for i in range(len(self.__MPDists[0])):
                for j in range(len(self.__MPDists)): 
                    ofMPs.write('%25lf    '%self.__MPDists[j][i])
                ofMPs.write('\n')
            ofMPs.close()
        print 'measured points movements extracted done.'
            
        if self.__ifSaveSafetyFacotr:
            ofSF = open(os.path.join(Base.__currentProjectPath__,'safetyFactors.dg') , 'wb')
            for f in self.__safetyFactors:
                ofSF.write('%25lf\t'%f)
            ofSF.write('\n')
            ofSF.close() 
            
        print 'safety factors  extracted done.'
        
        if self.__ifSaveDists and len(self.__realDists)>0:
            ofDist = open(os.path.join(Base.__currentProjectPath__,'displacement.dg') , 'wb')
            for d in self.__realDists:
                ofDist.write('%lf\n'%d)
            ofDist.close()
        print 'distances  extracted done.'
            
        if self.__SaveStressBlockNum!=-1:
            ofSt = open(os.path.join(Base.__currentProjectPath__,'stress.dg') , 'wb')
            for s in self.__stress:
                ofSt.write('%25lf\t%25lf\t%25lf\n'%s)
            ofSt.close() 

        print 'all data extracted done.'

    def __parseSchema(self):
        
        self.__file = open(self.__fileName , 'rb')
        nums = self.__file.readline().split()
        self.__blocksNum = int(nums[0])
        self.__fixedPointsNum = int(nums[1])
        self.__loadingPointsNum = int(nums[2])
        self.__measuredPointsNum = int(nums[3])
        self.__boltsNum = int(nums[4])
        self.__verticesNum = int(nums[5])  
        self.__graphsNum = int(nums[6])    
        
        for i in range(self.__measuredPointsNum):
            self.__MPDists.append([])
        
        self.__file.readline()   # read windowInfo
        
        # read blocks' orders
        for i in range(self.__blocksNum):
            self.__file.readline()
        
    def __parse1Graph(self ):
        line = self.__file.readline()
        assert line[0] == '<'   # read <<<step>>> n
        
        t = 0 
        # read blocks' infomation
        while t<self.__verticesNum :
            self.__file.readline()
            t+=1

        t=0
        # read fixed points and loading points
        while t< self.__fixedPointsNum + self.__loadingPointsNum:
            self.__file.readline() # (x , y) No.
            self.__file.readline() # speedX , speedY
            t+=1
            
        t=0
        # read measured points
        # t represent index of measured point
        while t<self.__measuredPointsNum:
            # (x , y) No.
            nums = self.__file.readline().split()
            X = float(nums[0])
            Y = float(nums[1])
            tmp=0
            if len(self.__lastMPs)==self.__measuredPointsNum:
                p = self.__lastMPs[t]
                tmp = sqrt((X-p[0])*(X-p[0]) + (Y-p[1])*(Y-p[1]))
                self.__lastMPs[t] = (X,Y,0)
            else:
                tmp=0
                self.__lastMPs.append((X,Y,0)) 

            if len(self.__MPDists[t])>0:
                tmpDist = tmp+self.__MPDists[t][-1]
            else:
                tmpDist = tmp
            self.__MPDists[t].append(tmpDist)
            
            # speedX , speedY
            self.__file.readline()                
            t+=1
            
        t=0
        # read bolts
        while t<self.__boltsNum:
            self.__file.readline() # u , v , r
            self.__file.readline() # stressX , stressY , stressXY
            t+=1      

        t=0
        # read block stress
        while t< self.__blocksNum:
            nums = self.__file.readline() # stressX , stressY , stressXY
            if self.__SaveStressBlockNum!=-1:
                if t==self.__SaveStressBlockNum:
                    nums = nums.split()
                    self.__stress.append((float(nums[0]),float(nums[1]),float(nums[2])))
            t+=1
            
        # read time
        nums = self.__file.readline().split()
        self.__realTimes.append(float(nums[1]))
        self.__realDists.append(float(nums[0]))
             
    def extractData(self):
        import Base
        try:
            self.__parseSchema()
        except:
            print 'unvalid data'
            raise
        
        t=0
        while t<self.__graphsNum:
            try:
                self.__parse1Graph() 
                if t%100==0:
                    print 'step %d parsed done at time '% t , Base.getCurrentTime()
            except:
                print 'unvalid data at step %d'%t
            t+=1
            
#extracter = DGExtracter()
#extracter.setFile(filename)
#extracter.saveStress4Block(1)
#extracter.setSaveMPMovements(True)
#extracter.setSaveDists(True)
#extracter.extractData()
#extracter.outputExtractedData()