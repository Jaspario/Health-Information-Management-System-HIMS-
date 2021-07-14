from Lib.importlib import *

from Include.interface.UiClinicalRecord import Ui_ClinicalRecord 
from Include.interface.UiReview import Ui_ReviewNote

from Include.departments.Record import Record
from Include.departments.Lab import LabRequest
from Include.departments.Pharmacy import PharmRequest

class Clinic(QtWidgets.QDialog,Ui_ClinicalRecord):
    def __init__(self,parent=None,database=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent         = parent
        self.user           = parent.user 
        self.patient        = parent.patient 
        self.patientbase    = database  
        self.tablename      = "Clinical"
        self.rowCount       = 0
        self.records        = []
        self.Unpack()

    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        width  = int(0.5*screen.width())
        height = int(0.8*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot() 
        
    # on click actions
    def _signalShot(self):  
        self.closeBtn.clicked.connect(self.closeRecord) 
        self.addNewBtn.clicked.connect(self.addNewRecord)

    def closeRecord(self):
        self.patientbase.disconnect()  
        self.close()
        self.parent.show()
        pass
    
    def Unpack(self): 
        self.fname.setText(self.patient[0])
        self.lname.setText(self.patient[1])
        self.gender.setText(self.patient[3])
        self.age.setText(str(self.patient[4]))
        self.pclass.setText(self.patient[5])
        self.patientID.setText(str(self.patient[10]))
        self.status.setText(self.patient[11])
        self.getRecords(self.patient[10])
        
    def addNewRecord(self): 
        if self.rowCount>0: 
            d = self.rowCount-1  
            status = self.records[d].sealed 
            if status == False:
                msg = QtWidgets.QMessageBox(self)
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
        med_record = Record(self)
        review = ReviewNote(self,med_record)
        med_record.getRowObjects(review)
        self.records.append(med_record) 
        self.rowCount = self.rowCount+1
        review.show()
        self.hide()

    def getRecords(self, id=None):
        columns = ("id INT PRIMARY KEY UNIQUE NOT NULL","date TEXT NOT NULL","doctor TEXT NOT NULL","diagnosis TEXT NOT NULL",
        "action TEXT NOT NULL","labresult TEXT NOT NULL","status TEXT NOT NULL")

        self.patientbase.createTable(table=self.table,columns=columns) 

        self.med,msg=self.patientbase.getRows(table=self.tablename,field='id',keys=str(id))

        if self.med != None:
            for rowIndex in range(0,len(self.med)):
                self.table.setRowCount(rowIndex+1)
                med_record = Record(self)
                row = ReviewNote(self,med_record,self.med[rowIndex])
                med_record.getRowObjects(row)
                self.records.append(med_record)
                self.rowCount = rowIndex+1
    

class ReviewNote(QtWidgets.QDialog,Ui_ReviewNote):

    def __init__(self,parent=None,record=None,items=None):
        super().__init__(parent=None)
        self.__initUI__()
        self.parent     = parent
        self.user       = parent.user  
        self.record     = record 
        self.id         = record.i
        self.items      = items
        self.status     = "Sign"
        self.pharm      = PharmRequest(self,items[-3]) 
        self.lab        = LabRequest(self,items[-1])

        self.disable(False)
        self.doctor.setText(self.user[0]+" "+self.user[1])

        if self.items != None:
            self.disable()
            self.updateTable()

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        width  = int(0.4*screen.width())
        height = int(0.8*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot() 

    def _signalShots(self): 
        self.saveBtn.clicked.connect(self.Sign)
        self.labBtn.clicked.connect(self.Lab)
        self.pharmBtn.clicked.connect(self.Pharmacy)

    def Sign(self): 
        if self.user[2] != 'medical doctor':
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Sefa (HIMS) - Warning!")
            msg.setText("Only authorized medical doctor can sign this document!")
            msg.exec_()
            return   

        if self.saveBtn.text() == 'Close':
            self.Close()
        else:
            if self.reviewNote.toPlainText() == "":
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(msg.Warning)
                msg.setWindowTitle("Sefa (HIMS) - Warning!")
                msg.setText("Please make a review note to sign this document!") 
                msg.exec_()
                return

            if self.Msg("Are you sure you want to sign this review?\nPlease note signed reviews cannot be edited!\n\nWould you like to continue?"):
                # commit to patientbase then disable
                self.disable()
                self.updateTable()
                self.Close()

    def updateTable(self):
        self.record.items.clear()
        
        if self.items == None: 
            self.GetItems()
            for i in range(0,len(self.items)):
                self.record.items.append(self.items[i]) 

        else:
            for i in range(0,len(self.items)):
                self.record.items.append(self.items[i])


        self.record.UpdateTable()

    def GetItems(self): 
        self.items  = []
        dt_string   = datetime.datetime.now().strftime("%d-%m-%Y %H_%M_%S")
        
        self.items.append(str(dt_string))
        self.items.append(self.doctor.text())
        self.items.append(self.diagnosis.toPlainText())
        self.items.append(self.pharm.prescriptions)
        self.items.append(self.lab.result)
        self.items.append(self.status) 
    

    def disable(self,state=True):
        if state==True:
            self.reviewed       = True
            self.enable         = False 
            self.record.sealed  = True
            self.status         = "Signed"
        else:
            self.reviewed = False
            self.enable   = True 

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
#22173058840