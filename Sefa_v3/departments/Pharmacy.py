from Importlib import *
from interface.UiPharmacyRecord import Ui_PharmacyRecord
from interface.UiPrescriptionForm import Ui_PrescriptionForm
from interface.UiPharmRequest import Ui_PharmRequest
from departments.Record import Record


class Pharmacy(PySide2.QtWidgets.QDialog,Ui_PharmacyRecord):
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
        w,h = int(0.4*screen.width()),int(0.9*(screen.height()-50))
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
        pharmrecord = Record(self)
        rowobj = Prescription(self,pharmrecord)
        pharmrecord.getRowObjects(rowobj)
        self.records.append(pharmrecord) 
        self.rowCount = self.rowCount+1


class Prescription(PySide2.QtWidgets.QDialog,Ui_PrescriptionForm):
    def __init__(self, parent=None,record=None):
        super().__init__(parent=None)
        self.__initUI__(parent)
        self.record = record
        self.parent = parent
        self.data   = parent.data 
        self.status = 'Sign'
        self.Unpack()

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.4*screen.width()),int(0.9*(screen.height()-50))
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

    def Unpack(self):
        id = self.data[10]
        self.fname.setText(self.data[0])
        self.lname.setText(self.data[1]) 
        self.cardNum.setText(str(id)) 

    def _signalShots(self):
        self.exitBtn.clicked.connect(self.Close)  
        self.dBtn.clicked.connect(self.Dispense) 

    def Close(self):
        self.close()
        self.parent.show()
    
    def Dispense(self):
        pass    


class PharmRequest(PySide2.QtWidgets.QDialog,Ui_PharmRequest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True) 
        #x,y=self.parent.pos().x()+200,self.parent.pos().y()-310     
        self.setFixedSize(400,500) 
        self.press_pos = self.pos()
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
        self.sendBtn.clicked.connect(self.SendReq)
        
    def Close(self):
        self.close()
    
    def SendReq(self):
        self.close()

