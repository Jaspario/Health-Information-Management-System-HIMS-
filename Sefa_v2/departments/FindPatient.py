from importLib import *
from interface.UiFindPatient import Ui_FindPatient
from departments.Patient import Patient,Register,Appointment


class FindPatient(QDialog,Ui_FindPatient):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.__initUI__(parent)
        self.flag = False
        self.busy = False
        self.patientId = 0
        self.enableButtons(self.flag)
        self.signalSlot()
        self.patient = Patient(self)
        self.register = Register(self)
        self.appt = Appointment(self)
    
    def __initUI__(self,parent=None):
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
        self.progressBar.hide()
        self.addLogo()

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def signalSlot(self):
        self.exitBtn.clicked.connect(self.exit)
        self.miniBtn.clicked.connect(self.mini)
        self.closeBtn.clicked.connect(self.Close)
        self.logout.clicked.connect(self.logOut)
        self.newBtn.clicked.connect(self.showForm)
        self.patientBtn.clicked.connect(self.showPatient)
        self.bookBtn.clicked.connect(self.bookAppt)
        self.searchBtn.clicked.connect(self.onSearch)
        self.sendBtn.clicked.connect(self.sendFile)

    def exit(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Sefa (HIMS)")
        msg.setText("Do you want to exit this app?")
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        retcode = msg.exec_()
        if retcode == QMessageBox.Yes:
            self.close()
            sys.exit()
        return

    def mini(self):
        self.showMinimized()

    def Close(self):
        self.searchLabel.setText("") 
        self.enableButtons(False)
    
    def logOut(self):
        self.Close()
        self.hide()
        self.parent.show()

    def showPatient(self):
        self.hide()
        self.patient.show()

    def showForm(self):
        self.hide()
        self.register.show() 

    def sendFile(self):
        pass

    def bookAppt(self):
        self.hide()
        self.appt.show()  

    def onSearch(self):
        self.Close()
        timer = QTimer()
        timer.singleShot(10*10,self.search)

    def enableButtons(self,flag=True):
        if flag == True:
            self.result.show()
            self.patientBtn.setEnabled(True)
            self.bookBtn.setEnabled(True) 
        else:
            self.result.hide()
            self.patientBtn.setEnabled(False)
            self.bookBtn.setEnabled(False) 

    def search(self): 
            self.searchLabel.setText("Searching...")
            timer = QTimer()
            self.progressBar.show()     
            timer.singleShot(2000,self.reset)  
    
    def reset(self):
            self.searchLabel.setText("") 
            self.enableButtons(True)
            self.progressBar.hide()

