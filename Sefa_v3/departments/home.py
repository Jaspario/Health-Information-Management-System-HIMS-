from Importlib import *
from interface.UiFindPatient import Ui_FindPatient
from departments.Record import Register
from departments.Patient import Patient,Appointment

class Home(PySide2.QtWidgets.QDialog,Ui_FindPatient):
    
    def __init__(self, parent=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent 
        self.owner = parent.user
        self.__press_pos = self.pos()
        self.table = 'Patient'
        self.database = parent.database
        self.patient = None # holds all patient's records
        self.newpatient = None # registers new patient
        self.appointment = None # creates new appointment
        self.resultFound = False
        self.data = None  
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.5*screen.width()),int(0.8*(screen.height()-50))
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
        self.clearField()
        self.pinfoBox.hide()
        self.showStatus('')
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
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.__press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))
            
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)
        self.logoutBtn.clicked.connect(self.logOut)
        self.closeBtn.clicked.connect(self.closeRecord)
        self.sendBtn.clicked.connect(self.sendFile)
        self.searchBtn.clicked.connect(self.findPatient) 
        self.viewBtn.clicked.connect(self.openRecord)
        self.newBtn.clicked.connect(self.newPatient)
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

    def findPatient(self): 
        self.closeRecord()
        data, res = self.search()  
        if data != None:
            self.data = data[-1]
        if (res == True and self.data != None): 
            self.showStatus("Record Found!")
            self.setField(self.data)
        else:
            self.showStatus('Record not found!')
            self.clearField()
        
    def openRecord(self):  
        self.record = Patient(self)
        self.close()
        pass

    def newPatient(self):
        self.newpatient = Register(self)
        self.hide()
        pass

    def bookAppt(self):
        self.appt = Appointment(self)
        self.appt.show()
        self.hide()
        pass 

    def search(self):
        self.showStatus("Searching...")
        self.showProgress(True)

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

        self.showProgress(False)
        self.showStatus("")
        return result,False
    
    def setField(self,data=None):
        self.pinfoBox.show()
        if data!=None:
            self.fnamelbl.setText(data[0])
            self.lnamelbl.setText(data[1])
            self.genderlbl.setText(data[3])
            self.agelbl.setText(str(data[4]))
            self.classlbl.setText(data[5])
            self.pnumlbl.setText(str(data[10]))
            self.pstatuslbl.setText(data[11])
            self.doctorlbl.setText("")
            self.regdatelbl.setText("")
            self.lastvisitlbl.setText("") 
        self.viewBtn.setEnabled(True)
        self.bookBtn.setEnabled(True) 
        self.showProgress(False)

    def clearField(self):    
        self.resultFound = False
        self.data = None
        self.pinfoBox.hide()
        self.fnamelbl.clear()
        self.lnamelbl.clear()
        self.genderlbl.clear()
        self.agelbl.clear()
        self.pnumlbl.clear()
        self.pstatuslbl.clear()
        self.doctorlbl.clear()
        self.regdatelbl.clear()
        self.showProgress(False)
        self.viewBtn.setEnabled(False)
        self.bookBtn.setEnabled(False) 
        self.lastvisitlbl.clear()
        self.showStatus('')
    
    def showProgress(self,flag):
        if flag == True:
            self.progressBar.show()
            timer = PySide2.QtCore.QTimer()
            timer.timeout.connect(lambda: update_progress(1000))
            timer.start(10*10)
        else:
            self.progressBar.hide()
    
    def update_progress(self,count=1000): 
        for i in range(0,count):
            progress = n = n+i
            self.progressBar.setValue(progress) 
  
    def showStatus(self,msg=''):
        self.searchlbl.setText(msg)
        self.searchlbl.show()

        if msg == '': 
            timer = PySide2.QtCore.QTimer()
            timer.singleShot(500,self.searchlbl.hide)