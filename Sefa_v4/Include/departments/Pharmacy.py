from Lib.importlib import *

from Include.interface.UiPharmacyRecord import Ui_PharmacyRecord
from Include.interface.UiPrescriptionForm import Ui_PrescriptionForm
from Include.interface.UiPharmRequest import Ui_PharmRequest

from Include.departments.Record import Record


class Pharmacy(QtWidgets.QDialog,Ui_PharmacyRecord):
    def __init__(self,parent=None,database=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent         = parent
        self.user           = parent.user
        self.patient        = parent.patient 
        self.patientbase    = database  
        self.tablename      = "PharmacyRecord"
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
        pharmrecord = Record(self)
        rowobj = Prescription(self,pharmrecord)
        pharmrecord.getRowObjects(rowobj)
        self.records.append(pharmrecord) 
        self.rowCount = self.rowCount+1

    def getRecords(self, id=None):
        columns = ("id INT PRIMARY KEY UNIQUE NOT NULL","date TEXT NOT NULL","dispensedate TEXT NOT NULL","doctor TEXT NOT NULL","pharmacist TEXT NOT NULL","diagnosis TEXT NOT NULL",
        "prescription TEXT NOT NULL","status TEXT NOT NULL")

        self.patientbase.createTable(table=self.tablename,columns=columns) 

        self.drug,msg=self.patientbase.getRows(table=self.table,field='id',keys=str(id))

        if self.drug != None:
            for rowIndex in range(0,len(self.drug)):
                self.table.setRowCount(rowIndex+1)
                pharm_record = Record(self)
                row = Prescription(self,pharm_record,self.drug[rowIndex])
                pharm_record.getRowObjects(row)
                self.records.append(pharm_record)
                self.rowCount = rowIndex+1

class Prescription(QtWidgets.QDialog,Ui_PrescriptionForm):
    def __init__(self, parent=None,record=None):
        super().__init__(parent=None)
        self.__initUI__(parent)
        self.record     = record
        self.parent     = parent
        self.patient    = parent.patient 
        self.status     = 'Sign'
        self.Unpack()

    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        width  = int(0.4*screen.width())
        height = int(0.8*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShots()  

    def Unpack(self): 
        self.fname.setText(self.patient[0])
        self.lname.setText(self.patient[1]) 
        self.patientID.setText(str(self.patient[10])) 

    def _signalShots(self):  
        self.closeBtn.clicked.connect(self.Close)
        self.dBtn.clicked.connect(self.Dispense)
    
    def Dispense(self):
        pass 

    def Close(self):
        self.close()
        self.parent.show()   

class PharmRequest(QtWidgets.QDialog,Ui_PharmRequest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.id     = parent.id
        self.setupUi(self) 
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)  
        self.setFixedSize(400,500) 
        self._signalShots()
    
    def _signalShots(self):
        self.exitBtn.clicked.connect(self.Close)
        self.sendBtn.clicked.connect(self.SendReq)
        
    def Close(self):
        self.close()
    
    def SendReq(self):
        self.close()
