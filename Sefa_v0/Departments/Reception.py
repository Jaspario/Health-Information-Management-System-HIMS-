from Departments._imports_ import *
from Departments.resources.interface._py.Ui_Reception import Ui_Reception

from Departments.Patient import __Patient__ 




class __Reception__(QMainWindow,Ui_Reception):
    
    def __init__(self, login=None):
        super().__init__() 
        self.__initUI__()
        self.login   = login
        self.patient = __Patient__(self)
        self.account = None
        self.lab     = None
        self.pharmacy= None
        self.clinic  = None
        #...

    def __initUI__(self):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #.....
        self.addLogo()
        self.SlotSignals()

    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def SlotSignals(self):
        self.exitBtn.clicked.connect(self.OnClickExit)
        self.minBtn.clicked.connect(self.showMinimized) 
        self.patientBtn.clicked.connect(self.OnClickPatient) 
        self.repLogOut.clicked.connect(self.LogOut) 

    def LogOut(self):
        # implement code to disconnect user from database
        self.hide()
        self.login.show()
    
    def OnClickExit(self):
        if mssgBox(self,"Do you want to exit this App?"):
            sys.exit()
    
    def OnClickPatient(self):  
        self.patient.show()

    def OnClickAccount(self):
        pass

    def OnClickClinic(self):
        pass

    def OnClickLab(self):
        pass

    def OnClickPharmacy(self):
        pass
    
    def OnClickAppointment(self):
        pass
