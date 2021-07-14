from importLib import *

from departments.Pharmacy import Pharmacy
from departments.Account import Account
from departments.Clinic import Clinic
from departments.Lab import Lab
from departments.Profile import Profile
from departments.Appointment import Appointment

from interface.UiPatient import Ui_Patient
from interface.UiRegister import Ui_Register

class Patient(QMainWindow,Ui_Patient):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.parent     = parent
        self.Id         = parent.patientId
        self.unPack()
        self.__initUI__()
        self.signalSlot()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
        self.addLogo()

    def signalSlot(self):
        self.exitBtn.clicked.connect(self.Close)
        self.miniBtn.clicked.connect(self.mini)
        self.closeBtn.clicked.connect(self.Close)
        self.clinicBtn.clicked.connect(self.showClinicRecord)
        self.labBtn.clicked.connect(self.showLabRecord)
        self.pharmacyBtn.clicked.connect(self.showPharmacyRecord)
        self.accountBtn.clicked.connect(self.showAccountRecord)
        self.profileBtn.clicked.connect(self.showProfile)
        self.createApptBtn.clicked.connect(self.createAppt)

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        
    def unPack(self):
        self.clinic     = Clinic(self)
        self.lab        = Lab(self)
        self.pharm      = Pharmacy(self)
        self.acct       = Account(self)
        self.profile    = Profile(self)
        self.appt       = Appointment(self)
        pass

    def pack(self):
        pass

    def mini(self):
        self.showMinimized()
    
    def Close(self):
        self.pack()
        self.hide()
        self.parent.show()

    def showClinicRecord(self):
        self.hide()
        self.clinic.show()

    def showPharmacyRecord(self):
        self.hide()
        self.pharm.show()

    def showLabRecord(self):
        self.hide()
        self.lab.show() 

    def showAccountRecord(self):
        self.hide()
        self.acct.show()

    def showProfile(self):
        self.hide()
        self.profile.show() 

    def createAppt(self):
        self.hide()
        self.appt.show()


class Register(QDialog,Ui_Register):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent 
        self.__initUI__()
        self.signalSlot()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.cancel)
        self.miniBtn.clicked.connect(self.mini) 
        self.cancelBtn.clicked.connect(self.cancel)
        self.regBtn.clicked.connect(self.register)
    
    def mini(self):
        self.showMinimized()
    
    def cancel(self): 
        self.hide()
        self.parent.show() 

    def register(self):
        pass


