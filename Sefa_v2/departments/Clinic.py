from importLib import *
from interface.UiClinicalRecord import Ui_ClinicalRecord 
from interface.UiReview import Ui_Review 
from departments.Records import Records

class Clinic(QWidget,Ui_ClinicalRecord):
    def __init__(self,parent=None):
        super().__init__()
        self.__initUI__(parent)
        self.min = 50
        self.min = 0
        self.rowCount = 0
        self.records = []
        self.Load()
        self.signalSlot()
        self.addLogo()
    
    def __initUI__(self,parent=None):
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
    
    def Load(self):
        pass

    def Save(self):
        pass
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.onClose)
        self.miniBtn.clicked.connect(self.mini)
        self.closeBtn.clicked.connect(self.onClose)
        self.addNewBtn.clicked.connect(self.OnClickAddNew)

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
    

    def mini(self):
        self.showMinimized()
    
    def onClose(self):
        self.Save()
        self.hide()
        self.parent.show()

    def OnClickAddNew(self): 
        if self.rowCount>0: 
            d = self.rowCount-1  
            status = self.records[d].status
            print("Item gotten: ",status, " row = ",d)
            if status == "Unsigned":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Sefa (HIMS) - Warning!")
                msg.setText("An unsigned record was created! Sign record to continue.")
                msg.exec_()
                return 
            else:
                self.AddNew()
        else:
            self.AddNew()
    
    def AddNew(self):
        self.table.setRowCount(self.rowCount+1)
        record = Records(self)
        review = ReviewNote(self,record)
        record.viewObject(review)
        self.records.append(record) 
        self.rowCount = self.rowCount+1
    
    

class ReviewNote(QDialog,Ui_Review):
    def __init__(self, parent=None,r=None):
        super().__init__()
        self.__initUI__()
        self.parent   = parent 
        self.record   = r
        self.status   = "Sign"
        self.disable(False)
        self.SlotSignals()

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.addLogo()

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def SlotSignals(self):
        self.exitBtn.clicked.connect(self.Close) 
        self.cancelBtn.clicked.connect(self.Close)
        self.saveBtn.clicked.connect(self.Sign)
        self.labBtn.clicked.connect(self.Lab)
        self.pharmBtn.clicked.connect(self.Pharmacy)

    def Close(self):
        self.close()
        self.parent.show()
        
    def Msg(self,text):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Sefa (HIMS) - Question?")
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        retcode = msg.exec_()
        if retcode == QMessageBox.Yes:
            return True
        return False

    def Sign(self):
        if self.reviewNote.toPlainText() == "":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Sefa (HIMS) - Warning!")
            msg.setText("Please make a review note to sign this document!") 
            msg.exec_()
            return

        if self.Msg("Are you sure you want to sign this review?\nPlease note signed reviews cannot be edited!\n\nWould you like to continue?"):
            # commit to database then disable
            self.disable()
            self.updateTable()
            self.close()
            self.parent.show()
    
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
        diagnosis = self.diagnosisDisplay.toPlainText()
        prescription = self.prescriptionDisplay.toPlainText()
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
        self.saveBtn.setText(self.status)
        if self.status == "Signed":
            self.cancelBtn.setText("Close")
        self.reviewNote.setReadOnly(self.reviewed)
        self.labBtn.setEnabled(self.enable)
        self.pharmBtn.setEnabled(self.enable)
        self.saveBtn.setEnabled(self.unsigned)
        self.saveBtn.setText(self.status)

    def Lab(self):
        pass
    
    def Pharmacy(self):
        pass
