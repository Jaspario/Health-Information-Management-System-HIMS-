from Importlib import *
from interface.UiClinicalRecord import Ui_ClinicalRecord
from interface.UiReview import Ui_Review 
from departments.Lab import LabRequest
from departments.Pharmacy import PharmRequest
from departments.Record import Record


class Clinic(PySide2.QtWidgets.QDialog,Ui_ClinicalRecord):
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
        self.status.setText(self.data[11])
        
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
        medrecord = Record(self)
        review = ReviewNote(self,medrecord)
        medrecord.getRowObjects(review)
        self.records.append(medrecord) 
        self.rowCount = self.rowCount+1
        review.show()
        self.hide()
    

class ReviewNote(PySide2.QtWidgets.QWidget,Ui_Review):

    def __init__(self, parent=None,r=None):
        super().__init__(parent=None)
        self.__initUI__()
        self.parent   = parent
        self.owner    = parent.owner  
        self.press_pos = self.pos()
        self.record   = r
        self.status   = "Sign"
        self.disable(False)
        self.pharm = PharmRequest(self.pharmBtn) 
        self.lab = LabRequest(self.labBtn)
        self.doctor.setText(self.parent.owner[0]+" "+self.parent.owner[1])

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.4*screen.width()),int(0.93*(screen.height()-50))
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
        self.saveBtn.clicked.connect(self.Sign)
        self.labBtn.clicked.connect(self.Lab)
        self.pharmBtn.clicked.connect(self.Pharmacy)

    def Close(self):
        self.close()
        self.parent.show()
        
    def Msg(self,text):
        msg = PySide2.QtWidgets.QMessageBox(self)
        msg.setIcon(msg.Question)
        msg.setWindowTitle("Sefa (HIMS) - Question?")
        msg.setText(text)
        msg.setStandardButtons(msg.Yes|msg.No)
        retcode = msg.exec_()
        if retcode == msg.Yes:
            return True
        return False

    def Sign(self): 
        if self.owner[2] != 'medical doctor':
            msg = PySide2.QtWidgets.QMessageBox(self)
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Sefa (HIMS) - Warning!")
            msg.setText("Only authorized medical doctor can sign this document!")
            msg.exec_()
            return   

        if self.saveBtn.text() == 'Close':
            self.Close()
        else:
            if self.reviewNote.toPlainText() == "":
                msg = PySide2.QtWidgets.QMessageBox(self)
                msg.setIcon(msg.Warning)
                msg.setWindowTitle("Sefa (HIMS) - Warning!")
                msg.setText("Please make a review note to sign this document!") 
                msg.exec_()
                return

            if self.Msg("Are you sure you want to sign this review?\nPlease note signed reviews cannot be edited!\n\nWould you like to continue?"):
                # commit to database then disable
                self.disable()
                self.updateTable()
                self.Close()

    def updateTable(self):
        self.record.items.clear()
        self.GetItems()
        for i in range(0,5):
            self.record.items.append(self.items[i])
        self.record.UpdateTable()

    def GetItems(self):
        self.items = []  
        date = str(datetime.time())
        doc  = self.doctor.text()
        diagnosis = self.dlist.toPlainText()
        prescription = self.plist.toPlainText()
        self.items.append(date)
        self.items.append(doc)
        self.items.append(diagnosis)
        self.items.append(prescription)
        self.items.append(self.status) 
    
    def disable(self,state=True):
        if state==True:
            self.reviewed = True
            self.enable   = False
            self.unsigned = False
            self.record.status = "Signed"
            self.status        = "Signed" 
        else:
            self.reviewed = False
            self.enable   = True
            self.unsigned = True
        self.updateState()
    
    def updateState(self): 
        self.reviewNote.setReadOnly(self.reviewed)
        self.labBtn.setEnabled(self.enable)
        self.pharmBtn.setEnabled(self.enable) 
        if self.status == "Signed":
            self.saveBtn.setText("Close") 

    def Lab(self): 
        self.lab.move(self.labBtn.x()+self.lab.size().width(), self.labBtn.y()-self.lab.size().height()+100)
        self.lab.show()
        pass
    
    def Pharmacy(self):
        self.pharm.move(self.pharmBtn.x()+self.pharm.size().width(), self.pharmBtn.y()-self.pharm.size().height()+100) 
        self.pharm.show()         
        pass
