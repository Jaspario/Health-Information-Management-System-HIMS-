from Lib.importlib import *

from Include.interface.UiLabRecord import Ui_LabRecord
from Include.interface.UiLabReport import Ui_LabReport
from Include.interface.UiLabRequest import Ui_LabRequest

from Include.departments.Record import Record


class Lab(QtWidgets.QWidget,Ui_LabRecord):
    def __init__(self,parent=None,database=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent         = parent
        self.user           = parent.user
        self.patient        = parent.patient 
        self.patientbase    = database 
        self.tablename      = 'LabRecord'
        self.rowCount       = 0
        self.records        = [] 
        self.Unpack()

    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        screen = self.screen().size()
        width  = int(0.55*screen.width())
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
        self.getRecord(self.patient[10])
        
    def addNewRecord(self): 
        if self.rowCount>0: 
            index = self.rowCount-1  
            sealed = self.records[index].sealed
            if sealed == False:
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
        lab_record = Record(self)
        row = LabReport(self,lab_record)
        lab_record.getRowObjects(row)
        self.records.append(lab_record) 
        self.rowCount = self.rowCount+1

    def getRecord(self, id=None):
        columns = ("id INT PRIMARY KEY UNIQUE NOT NULL", "requestdate TEXT NOT NULL","collectiondate TEXT NOT NULL",
        "doctor TEXT NOT NULL","scientist TEXT NOT NULL","diagnosis TEXT NOT NULL","examination TEXT NOT NULL","pathalogy TEXT NOT NULL",
        "specimens TEXT NOT NULL","result TEXT NOT NULL","status TEXT NOT NULL")
        self.patientbase.createTable(table=self.table,columns=columns) 

        self.lab,msg=self.patientbase.getRows(table=self.tablename,field='id',keys=str(id))

        if self.lab != None:
            for rowIndex in range(0,len(self.lab)):
                self.table.setRowCount(rowIndex+1)
                lab_record = Record(self)
                row = LabReport(self,lab_record,self.lab[rowIndex])
                lab_record.getRowObjects(row)
                self.records.append(lab_record)
                self.rowCount = rowIndex+1


class   LabReport(QtWidgets.QWidget,Ui_LabReport):
    def __init__(self, parent=None,record=None,items=None):
        super().__init__(parent=None)
        self.__initUI__(parent)
        self.record = record
        self.parent = parent
        self.items  = items
        self.sealed = False
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        screen = self.screen().size()
        width  = int(0.75*screen.width())
        height = int(0.8*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot() 

    def _signalShots(self):
        self.submitBtn.clicked.connect(self.submitResult)
        self.addNewBtn.clicked.connect(self.addSample) 

    def Close(self):
        self.close()
        self.parent.show()
    
    def submitResult(self):
        pass

    def addSample(self):
        pass



class LabRequest(QtWidgets.QDialog,Ui_LabRequest):
    def __init__(self, parent=None,data=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)  
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)  
        self.setFixedSize(400,300)
        self._signalShots()
    
    def _signalShots(self):
        self.exitBtn.clicked.connect(self.Close)
        self.sendBtn.clicked.connect(self.SendReq)
        
    def Close(self):
        self.close()
    
    def SendReq(self):
        self.close()

