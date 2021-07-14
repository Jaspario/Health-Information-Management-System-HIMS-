from Lib.importlib import *

from Include.interface.UiPatient import Ui_Patient 
from Include.interface.UiApptSlip import Ui_ApptSlip
from Include.interface.UiProfile import Ui_Profile

from Include.departments.Clinic import Clinic
from Include.departments.Lab import Lab
from Include.departments.Pharmacy import Pharmacy



class Patient(QtWidgets.QWidget,Ui_Patient):
    def __init__(self,parent=None,database=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent   = parent
        self.user     = parent.user 
        self.patient  = parent.patient
        self.database = database 

        if self.patient!=None:
            self.fullname.setText(self.patient[1].title()+" "+self.patient[0].title()+" "+self.patient[2].title())
            self.patientID.setText(str(self.patient[10]))

        self.child1 = Profile(self) 
        self.child2 = Clinic(self,database)
        self.child3 = Lab(self,database) 
        self.child4 = Pharmacy(self,database)
        self.child5 = None#Account(self,database)
        self.child6 = Appointment(self,self.database)
        self.show()

    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir))  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        width  = int(0.55*screen.width())
        height = int(0.65*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot() 
            
    # on click actions
    def _signalShot(self):  
        self.closeBtn.clicked.connect(self.closeRecord)
        self.clinicalBtn.clicked.connect(self.showClinicRecord)
        self.labBtn.clicked.connect(self.showLabRecord)
        self.pharmacyBtn.clicked.connect(self.showPharmacyRecord)
        self.accountBtn.clicked.connect(self.showAccountRecord)
        self.profileBtn.clicked.connect(self.showProfile)
        self.bookBtn.clicked.connect(self.bookAppt)

    def closeRecord(self):
        self.close()
        self.parent.show()
        self.database.disconnect()  
        pass

    def showClinicRecord(self):
        dept = self.user[3]
        if dept != 'medical':
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Sefa (HIMS) - Warning!")
            msg.setText("Only authorized medical personnel can view this page!")
            msg.exec_()
            return

        self.child2.show()
        self.close()
        pass

    def showPharmacyRecord(self):
        self.child4.show()
        self.close()
        pass

    def showLabRecord(self):
        self.child3.show()
        self.close()
        pass 

    def showAccountRecord(self):
        #self.child5.show()
        #self.hide()
        pass

    def showProfile(self):
        self.child1.show()
        pass

    def bookAppt(self):
        self.child6.show() 
        pass


class Appointment(QtWidgets.QDialog,Ui_ApptSlip):
    def __init__(self,parent=None,database=None):
        super().__init__(parent = None)
        self.__initUI__(parent)
        self.database = database
        self.parent   = parent 
        self.patient  = parent.patient 
        self.patientID.setText(str(parent.patient[10])) 
        self.Load() # Load list of doctors available
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True) 

        screen = self.screen().size()
        width  = int(0.25*screen.width())
        height = int(0.3*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot() 
        
    
    def _signalShot(self):
        self.bookBtn.clicked.connect(self.book)
        self.cancelBtn.clicked.connect(self.cancel) 

    def cancel(self): 
        self.hide()
        self.parent.show()
    
    def Load(self):
       # print(type(self.database))
       # result, msg = self.database.getRows(table='Users',field='jobtitle',keys="medical doctor")
       # self.doclist.clear()
       # self.doclist.addItems(result)
        pass

    def book(self):
        pass



class Profile(QtWidgets.QWidget,Ui_Profile):

    def __init__(self, parent=None): 
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent
        self.patient = parent.patient
        self.user = parent.user
        self.unPack(self.patient)  
        
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True) 

        screen = self.screen().size()
        width  = int(0.45*screen.width())
        height = int(0.75*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot()

    # on click actions
    def _signalShot(self):  
        self.closeBtn.clicked.connect(self.closeProfile) 

    def closeProfile(self): 
        self.close()
        self.parent.show()
        del self
        pass

    def unPack(self,data=None):
        if data==None:
            return
        #for i in range(0,len(data)):
            #print(f"Check: {i} ",data[i])
        self.fname.setText(data[0].title())
        self.lname.setText(data[1].title())
        self.oname.setText(data[2].title())
        self.gender.setText(data[3].title())
        self.age.setText(str(data[4]))
        self.pclass.setText(data[5].title())
        self.origin.setText(data[6].title())
        self.nationality.setText(data[7].title())
        self.phone.setText("+234"+str(data[8]))
        self.email.setText(data[9])
        self.patientID.setText(str(data[10]))
        self.status.setText(data[11].title()) 
        self.address.setText(data[12].title())
        self.state.setText(data[13].title())
        self.country.setText(data[14].title())
        
        self.regDate.setText(data[15].replace("_",":"))
        self.admissionDate.setText(data[16].replace("_",":"))

        self.kfname.setText(data[17].title())
        self.klname.setText(data[18].title())
        self.kphone.setText("+234"+str(data[19]))
        self.krelationship.setText(str(data[20]).title()) 
        self.kaddress.setText(data[21].title())
        self.kstate.setText(data[22].title())
        self.kcountry.setText(data[23].title())
        return
        
    def pack(self):
        data = [
            self.fname.text(),self.lname.text(),self.oname.text(),
            self.gender.text(),self.age.text(),self.pclass.text(),
            self.origin.text(),self.nationality.text(),self.phone.text(),
            self.email.text(),self.id.text(),self.status.text(),
            self.address.text(),self.state.text(),self.country.text(),
            self.kfname.text(),self.klname.text(),self.kphone.text(),self.krelationship.text(),
            self.kaddress.text(),self.kstate.text(),self.kcountry.text()]
            
        pass

    def updateProfile(self):
        pass

    def editProfile(self,edit=False):
        self.phone.setReadOnly(edit),self.email.setReadOnly(edit),self.address.setReadOnly(edit),
        self.kfname.setReadOnly(edit),self.klname.setReadOnly(edit),self.kmobile.setReadOnly(edit),
        self.krelationship.setReadOnly(edit),self.kaddress.setReadOnly(edit)
        pass



