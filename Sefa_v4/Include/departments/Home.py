from Lib.importlib import *
from Include.interface.UiHome import Ui_Home
from Include.departments.Record import Register
from Include.departments.Patient import Patient,Appointment


class Home(QtWidgets.QWidget,Ui_Home):

    def __init__(self, parent=None, database=None):
        super().__init__(parent = None)
        self.__initUI__()
        self.parent = parent
        self.database = database
        self.user  = parent.user
        self.table = 'Patient'
        self.records  = None
        self.register = None
        self.appt = None
        self.resultFound = False
        self.patient = None # this is the patient's data
    
    def __initUI__(self):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir))  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)

        screen = self.screen().size()
        height = int(0.7*(screen.height()-50))
        width  = int(0.6*screen.width())

        self.setFixedSize(width,height)
        self._signalShot()
        self.clearField()
        self.pinfoBox.hide()
        self.showStatus('')
        self.progressBar.hide()
        
    # on click actions
    def _signalShot(self): 
        self.logOutBtn.clicked.connect(self.logOut)
        self.closeBtn.clicked.connect(self.closeRecord)
        self.sendBtn.clicked.connect(self.sendFile)
        self.searchBtn.clicked.connect(self.findPatient) 
        self.viewBtn.clicked.connect(self.openRecord)
        self.regNewBtn.clicked.connect(self.newPatient)
        self.bookBtn.clicked.connect(self.bookAppt)

    def closeRecord(self):
        self.database.disconnect()
        self.clearField()
        self.pinfoBox.hide()
        pass
    
    def logOut(self):
        self.closeRecord()
        self.close()
        self.parent.show()
        del self

    def sendFile(self):
        pass
    
    def openRecord(self):  
        self.record = Patient(self,database=self.database)
        self.close()
        pass

    def newPatient(self):
        self.newpatient = Register(self,database=self.database)
        self.hide()
        pass

    def bookAppt(self):
        print("getting Appointment Slip")
        self.appt = Appointment(self,database=self.database)
        self.appt.show()
        self.hide()
        pass 

    def findPatient(self): 
        self.closeRecord()
        data, res = self.Search()  
        if data != None:
            self.patient = data[-1]
        if (res == True and self.patient != None): 
            self.showStatus("Record Found!")
            self.setField(self.patient)
        else:
            self.showStatus('Record not found!')
            self.clearField()
    
    def Search(self):
        self.showStatus("Searching...")
        #self.showProgress(True)

        value = self.searchField.text().lower()
        result = None
        val = []

        if not value.isnumeric() and value != '': 
            s = value.split(' ',1)
        
            if len(s) <= 1:
                return result,False
            try: 
                val.append(s[0].strip())
                val.append(s[1].strip())
                val.append(s[2].strip())
            except IndexError:
                val.append(s[0].strip())
                val.append(s[1].strip())
            finally:
                value = val
  
            var = val[0],val[1] 
            result,msg = self.database.getRows(table=self.table,field='firstname=? AND lastname=?',keys=var)
            
            if msg == 'FALSE' or msg == 'INVALID' or msg=='':
                var = val[1],val[0]
                result,msg = self.database.getRows(table=self.table,field='firstname=? AND lastname=?',keys=var)
                
                if msg != 'FALSE' and msg !='':
                    return result,True
            else:
                return result,True

        elif value.isnumeric(): 
            result, msg = self.database.getRows(table=self.table,field='patientID',keys=value)
            if msg == 'TRUE':
                return result, True 

        #self.showProgress(False)
        self.showStatus("")
        return result,False
    
    def setField(self,data=None):
        #datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
        self.pinfoBox.show()
        if data!=None:
            self.fname.setText(data[0].title())
            self.lname.setText(data[1].title())
            self.gender.setText(data[3].title())
            self.age.setText(str(data[4]))
            self.pclass.setText(data[5].title())
            self.patientID.setText(str(data[10]))
            self.status.setText(data[11].title()) 
            self.regDate.setText(data[15])
            self.lastCheckup.setText(data[16])
        self.viewBtn.setEnabled(True)
        self.bookBtn.setEnabled(True) 
        #self.showProgress(False)

    def clearField(self):    
        self.resultFound = False
        self.patient = None
        self.pinfoBox.hide()
        self.fname.clear()
        self.lname.clear()
        self.gender.clear()
        self.age.clear()
        self.patientID.clear()
        self.status.clear()
        self.pclass.clear()
        self.regDate.clear()
        
        self.lastCheckup.clear()
        self.viewBtn.setEnabled(False)
        self.bookBtn.setEnabled(False) 
        self.showStatus('')

    def showStatus(self,msg=''):
        self.search.setText(msg)
        self.search.show()

        if msg == '': 
            timer = QtCore.QTimer()
            timer.singleShot(500,self.search.hide)