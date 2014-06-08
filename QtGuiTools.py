'''
Created on 2013-12-26

@author: laine
'''
###############################################
#
# this class is based on QWidget, this widget will
# give information while exiting if needed
#
###############################################

from PyQt4 import QtCore , QtGui
class ExitWithInfoWidget(QtGui.QDialog):
    '''
    This class bases on QWidget, the only difference is that
    this class will show a QDialog if user click the 'X' to close widget
    '''
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ifShowDialogWhileExit = True
       
    def setupUi(self, label , dataTable):
        self.label = label 
        self.dataTable = dataTable 
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.dataTable.table)
        
        btnBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok \
                            | QtGui.QDialogButtonBox.Cancel)
        btnBox.setCenterButtons(True)
        btnBox.accepted.connect(self.tryToSave)
        btnBox.rejected.connect(self.discard)
        layout.addWidget(btnBox)
        
        self.setLayout(layout)

    def tryToSave(self):
        # clear select state
        self.dataTable.changeCurrentItem()
        
        print self.dataTable.checkTable(),  self.dataTable.ifEmpty()
        if not self.dataTable.checkTable() or \
            (self.dataTable.table.rowCount>0 and self.dataTable.ifEmpty()):
            QtGui.QMessageBox.critical(self, 'DataError', 'please input float number')
            print 'call critical dialog'
        else:
            self.ifShowDialogWhileExit = True 
            self.accept()

    def discard(self):
        # clear select state
        self.dataTable.changeCurrentItem()

        self.ifShowDialogWhileExit = True 
        self.__clearTable()
        self.reject()

    def __clearTable(self):
        self.dataTable.clearContent()
        
    def closeEvent(self,event):
        if not self.ifShowDialogWhileExit:
            self.ifShowDialogWhileExit = True # reset the value
            return 
        reply = QtGui.QMessageBox.question(self, 'Message', \
            "Do you want to save data before exiting?", QtGui.QMessageBox.Yes\
            , QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.tryToSave()
            event.ignore()
        else:
            self.discard()

        self.ifShowDialogWhileExit = True # reset the value