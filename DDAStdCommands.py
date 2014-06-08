'''
Created on 2014-1-9

@author: laine
'''
from PyQt4 import QtCore

def RedrawObject(objName):
    import FreeCAD
    if not objName:
        return
    print 'trigger obj \'%s\' in OperationObverser'%objName
    obj = FreeCAD.getDocument('DDA').getObject(objName)
    assert obj
    obj.ViewObject.RedrawTrigger = True

class DDA_NewDoc:
    '''
    create new document
    '''
    
    def GetResources(self):
        return {'Pixmap'  :'document-new',
                'MenuText': QtCore.QT_TRANSLATE_NOOP('DDA_NewDoc',"New"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_NewDoc',"Create a new empty documen")}

    def Activated(self):
        import Base
        Base.confirmDocumentExisting('DDA')
        
        import Base
        Base.enableSelectionObserver(True)
        
        import DDADatabase
        DDADatabase.enableOperationObverser(True)
        
#        global T
#        T.Activated()

    def isActive(self):
#        import FreeCAD
#        if FreeCAD.getDocument('DDA'):
#            return False
#        else:
#            return True
        return True
        
class DDA_Undo:
    '''
    undo one step
    '''
    
    def GetResources(self):
        return {'Pixmap'  :'edit-undo',
                'MenuText': QtCore.QT_TRANSLATE_NOOP('DDA_Undo',"undo"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_Undo',"undo one step")}

    def Activated(self):
        import Base
        database = Base.getDatabaser4CurrentStage()
        RedrawObject(database.undo())

    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')

    
class DDA_Redo:
    '''
    redo one step
    '''
    
    def GetResources(self):
        return {'Pixmap'  :'edit-redo',
                'MenuText': QtCore.QT_TRANSLATE_NOOP('DDA_Redo',"redo"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP('DDA_Redo',"redo one step")}

    def Activated(self):
        import Base
        database = Base.getDatabaser4CurrentStage()
        RedrawObject(database.redo())

    def IsActive(self):
        import Base
        return Base.ifReady4Drawing('DDA')

   
import FreeCADGui   
FreeCADGui.addCommand('DDA_NewDoc', DDA_NewDoc())
FreeCADGui.addCommand('DDA_Undo', DDA_Undo()) 
FreeCADGui.addCommand('DDA_Redo', DDA_Redo())