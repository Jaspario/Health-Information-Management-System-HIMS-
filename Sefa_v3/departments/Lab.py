from Importlib import *
from interface.UiLabRecord import Ui_LabRecord
from interface.UiLabReport import Ui_LabReport
from interface.UiLabRequest import Ui_LabRequest
from departments.Record import Record


class Lab(PySide2.QtWidgets.QDialog,Ui_LabRecord):
    def __init__(self,parent=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent
        self.owner = parent.owner
        self.press_pos = PySide2.QtCore.QPoint()
        self.data = parent.data 
        self.rowCount = 0
        self.records = []
        self.Unpack()
        self.database = parent.database  
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.5*screen.width()),int(0.9*(screen.height()-50))
        self.setFixedSize(w,h)
        self.adjustSize()
        self.setGeometry(
            PySide2.QtWidgets.QStyle.alignedRect(
                PySide2.QtCore.Qt.LeftToRight,
                PySide2.QtCore.Qt.AlignCenter,
                self.size(),
                PySide2.QtWidgets.QApplication.instance().desktop().availableGeometry()
                )
                )

        self.logo.setFixedSize(PySide2.QtCore.QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self._signalShot() 
    # exit application
    def exitApp(self):
        msg = PySide2.QtWidgets.QMessageBox(self)
        msg.setIcon(msg.Question)
        msg.setWindowTitle("Sefa (HIMS)-Exit App?")
        msg.setText("Do you want to exit this app?")
        msg.setStandardButtons(msg.Yes|msg.No)
        retcode = msg.exec_()

        if retcode == msg.Yes:
            self.quit() 
            
    def quit(self):
        self.close()
        self.parent.quit() 
    
    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.press_pos))
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)   
        self.closeBtn.clicked.connect(self.closeRecord) 
        self.addNewBtn.clicked.connect(self.addNewRecord)

    def closeRecord(self):
        self.database.disconnect()  
        self.close()
        self.parent.show()
        pass
    
    def Unpack(self):
        id = self.data[10]
        self.fname.setText(self.data[0])
        self.lname.setText(self.data[1])
        self.gender.setText(self.data[3])
        self.age.setText(str(self.data[4]))
        self.pclass.setText(self.data[5])
        self.cardNum.setText(str(id))
        #self.status.setText(self.data[11])
        
    def addNewRecord(self): 
        if self.rowCount>0: 
            d = self.rowCount-1  
            status = self.records[d].status
            if status == "Unsigned":
                msg = PySide2.QtWidgets.QMessageBox(self)
                msg.setIcon(msg.Warning)
                msg.setWindowTitle("Sefa (HIMS) - Warning!")
                msg.setText("An unsigned record was created! Sign record to continue.")
                msg.exec_()
                return 
            else:
                self.newRecord()
        else:
            self.newRecord()
    
    def newRecord(self):
        self.table.setRowCount(self.rowCount+1)
        labrecord = Record(self)
        rowobj = LabReport(self,labrecord)
        labrecord.getRowObjects(rowobj)
        self.records.append(labrecord) 
        self.rowCount = self.rowCount+1

class   LabReport(PySide2.QtWidgets.QDialog,Ui_LabReport):
    def __init__(self, parent=None,record=None):
        super().__init__(parent=None)
        self.__initUI__(parent)
        self.record = record
        self.parent = parent
        self.status = 'Sign'
        self.press_pos = self.pos()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.75*screen.width()),int(0.8*(screen.height()-50))
        self.setFixedSize(w,h)
        self.adjustSize() 
        self.setGeometry(
            PySide2.QtWidgets.QStyle.alignedRect(
                PySide2.QtCore.Qt.LeftToRight,
                PySide2.QtCore.Qt.AlignCenter,
                self.size(),
                PySide2.QtWidgets.QApplication.instance().desktop().availableGeometry()
                )
                )

        self.logo.setFixedSize(PySide2.QtCore.QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self._signalShots()  

    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.globalPos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = PySide2.QtCore.QPoint(event.globalPos() - self.press_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.press_pos = event.globalPos()

    def _signalShots(self):
        self.exitBtn.clicked.connect(self.Close) 
        self.miniBtn.clicked.connect(self.showMinimized)
        self.closeBtn.clicked.connect(self.Close)
        self.submitBtn.clicked.connect(self.submitResult)
        self.addBtn.clicked.connect(self.addSample) 

    def Close(self):
        self.close()
        self.parent.show()
    
    def submitResult(self):
        pass

    def addSample(self):
        pass

class LabRequest(PySide2.QtWidgets.QDialog,Ui_LabRequest):
    def __init__(self, parent=None,pos=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint)  
        #x,y=self.parent.pos().x()+300,self.parent.pos().y()-170  
        #x,y=self.parent.pos().x(),self.parent.pos().y() 
        self.setFixedSize(400,300) 
        self.logo.setFixedSize(PySide2.QtCore.QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self._signalShots()

    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.press_pos))
    
    def _signalShots(self):
        self.exitBtn.clicked.connect(self.Close)
        self.sendReqBtn.clicked.connect(self.SendReq)
        
    def Close(self):
        self.close()
    
    def SendReq(self):
        self.close()

