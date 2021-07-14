from Departments._imports_ import *
from Departments.resources.interface._py.Ui_Patient import Ui_Patient
from Departments.resources.interface._py.Ui_Record import Ui_Record
from Departments.resources.interface._py.Ui_PReview import Ui_Review


class __Patient__(QDialog,Ui_Patient):
    def __init__(self, parent=None):
        super().__init__()
        self.__initUI__(parent)
        self.parent = parent
        self.record = __PatientRecord__(self)
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)  
        self.addLogo()
        self.SlotSignals() 
    
    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def SlotSignals(self): 
        self.exitBtn.clicked.connect(self.OnClickExit)
        self.minBtn.clicked.connect(self.showMinimized) 
        self.pclose.clicked.connect(self.OnClickClose)
        self.psearchBtn.clicked.connect(self.OnClickSearch)
        self.recordBtn.clicked.connect(self.OnClickRecord)

    def OnClickClose(self):
        self.close()
        self.parent.show()
     
    def OnClickExit(self):
        if mssgBox(self,"Do you want to exit this App?"):
            sys.exit()
        return
    
    def OnClickSearch(self):
        self.searchLabel.setText("Searching...")
        return

    def OnClickRecord(self):
        self.record.show()




class __PatientRecord__(QDialog,Ui_Record):
    def __init__(self, parent): 
        super().__init__(parent)
        self.__initUI__(parent)
        self.parent = parent 
        self.maxEntry = 50 # maximum number of rows
        self.recordID = 0 # patient's id
        self.preview  = []
        self.records  = []
        self.rowCount = 0

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)  
        self.addLogo()
        self.SlotSignals() 
    
    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def SlotSignals(self): 
        self.exitBtn.clicked.connect(self.OnClickClose)
        self.closeBtn.clicked.connect(self.OnClickClose)
        self.addNewBtn.clicked.connect(self.OnClickAddNew)

    def OnClickClose(self):
        self.close()

    def OnClickAddNew(self): 
        self.table.setRowCount(self.rowCount+1)
        self.records.append(Record(self)) 
        self.rowCount = self.rowCount+1
    

class Record(Ui_Record):
    def __init__(self, parent):
        self.table    = parent.table
        self.status   = "Unsigned"
        self.items    = [] 
        self.index    = parent.rowCount
        self.button   = QPushButton("Create")
        #....
        self.addButton()

    def setTable(self):
        for i in range(0,5): 
            item = QTableWidgetItem(self.items[i])
            self.table.setItem(self.index,i,item)   

    def addButton(self):
        self.button.clicked.connect(self.OnClickButton)
        self.table.setCellWidget(self.index,5,self.button)
        print(f"Created button item with value {self.button}")

    def UpdateTable(self):
        text = self.GetButtonText()
        self.button.setText(text)
        self.setTable()
    
    def OnClickButton(self):
        if self.button.text() == "Create":
            self.OnCreate()
        elif self.button.text() == "View":
            self.OnView()

    def OnView(self):
        self.review.show()

    def OnCreate(self):
        self.review = __Review__(self) 
        self.review.show()  
        print("A new record for patient 0000000000 has been created!")

    def GetButtonText(self):
        res = "Create"
        if self.status == "Signed":
            res = "View" 
        return res



class __Review__(QDialog,Ui_Review):
    def __init__(self, parent=None):
        super().__init__()
        self.parent   = parent 
        self.status   = "Sign"
        self.reviewed = False
        self.commit   = True
        self.unsigned = True
        self.__initUI__(parent)

    def __initUI__(self,parent):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.reviewNote.setReadOnly(self.reviewed)
        self.commitBtn.setEnabled(self.commit)
        self.saveBtn.setEnabled(self.unsigned)
        self.saveBtn.setText(self.status)
        self.addLogo()
        self.SlotSignals()

    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def SlotSignals(self):
        self.exitBtn.clicked.connect(self.OnClickClose) 
        self.cancelBtn.clicked.connect(self.OnClickClose)
        self.saveBtn.clicked.connect(self.OnClickSave)
        self.commitBtn.clicked.connect(self.OnClickCommit)

    def OnClickClose(self):
        self.close()
        self.parent.show()
    
    def OnClickSave(self):
        if dbMsg("Are you sure you want to sign this review?\n Please note signed reviews cannot be edited!\n Would you like to continue?"):
        # commit to database then disable
            self.disable()
            self.parent.items.clear()
            self.GetItems()
            for i in range(0,5):
                self.parent.items.append(self.items[i])
            self.parent.UpdateTable()
            self.close()
            self.parent.show()

    def OnClickCommit(self):
        pass

    def GetItems(self):
        self.items = []
        date = str(datetime.time())
        doc  = self.doctor.text()
        diagnosis = self.diagnosisDisplay.toPlainText()
        prescription = self.prescriptionDisplay.toPlainText()
        print("Date time: ",date," doc name: ",doc," diagnosis: ",diagnosis," prescription: ",prescription," status: ",self.status)
        self.items.append(date)
        self.items.append(doc)
        self.items.append(diagnosis)
        self.items.append(prescription)
        self.items.append(self.status) 
    
    def disable(self):
        self.reviewed = True
        self.commit = False
        self.unsigned = False
        self.saveBtn.setText("Signed")
        self.parent.status = "Signed"
        self.status = "Signed"
        self.reviewNote.setReadOnly(self.reviewed)
        self.commitBtn.setEnabled(self.commit)
        self.saveBtn.setEnabled(self.unsigned)
        self.saveBtn.setText(self.status)