from Importlib import *

from interface.UiPatient import Ui_Patient 
from interface.UiProfile import Ui_Profile
from interface.UiApptSlip import Ui_ApptSlip

from departments.Clinic import Clinic
from departments.Lab import Lab
from departments.Pharmacy import Pharmacy
from departments.Account import Account


class Patient(PySide2.QtWidgets.QMainWindow,Ui_Patient):
    def __init__(self,parent=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent
        self.owner  = parent.owner
        self.press_pos = PySide2.QtCore.QPoint()
        self.data = parent.data 
        self.database = parent.database 
        if self.data!=None:
            self.patientID = str(self.data[10])
            self.status = self.data[11]
            self.cardNum.setText(self.patientID)
            self.fullname.setText(self.data[0]+" "+self.data[1]+" "+self.data[2])
        self.child1 = Profile(self) 
        self.child2 = Clinic(self)
        self.child3 = Lab(self) 
        self.child4 = Pharmacy(self)
        self.child5 = Account(self)
        self.child6 = Appointment(self)
        self.show()
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.63*screen.width()),int(0.7*(screen.height()-50))
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
            self.press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.press_pos))
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)   
        self.closeBtn.clicked.connect(self.closeRecord)
        self.clinicBtn.clicked.connect(self.showClinicRecord)
        self.labBtn.clicked.connect(self.showLabRecord)
        self.pharmacyBtn.clicked.connect(self.showPharmacyRecord)
        self.accountBtn.clicked.connect(self.showAccountRecord)
        self.profileBtn.clicked.connect(self.showProfile)
        self.bookBtn.clicked.connect(self.bookAppt)

    def closeRecord(self):
        self.database.disconnect()  
        self.close()
        self.parent.show()
        pass

    def showClinicRecord(self):
        dept = self.owner[3]
        if dept != 'medical':
            msg = PySide2.QtWidgets.QMessageBox(self)
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
        self.child5.show()
        self.hide()
        pass

    def showProfile(self):
        self.child1.show()
        pass

    def bookAppt(self):
        self.child6.show()
        self.hide()
        pass

class Profile(PySide2.QtWidgets.QDialog,Ui_Profile):

    def __init__(self, parent=None): 
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent
        self.data = parent.data
        self.press_pos = PySide2.QtCore.QPoint()
        self.owner = parent.owner 
        self.unPack(parent.data)  
        
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True) 

        screen = self.screen().size()
        w,h = int(0.42*screen.width()),int(0.99*(screen.height()-50))
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
    
    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.press_pos))
    # exit application
    def exitApp(self):
        msg = PySide2.QtWidgets.QMessageBox(self)
        msg.setIcon(msg.Question)
        msg.setWindowTitle("Sefa (HIMS)-Exit App?")
        msg.setText("Do you want to exit this app?")
        msg.setStandardButtons(msg.Yes|msg.No)
        retcode = msg.exec_()

        if retcode == msg.Yes:
            self.pack()
            self.close() 
            del self
            sys.exit()
        else:
            return
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)   
        self.closeBtn.clicked.connect(self.closeProfile) 
        self.updateBtn.clicked.connect(self.updateProfile)
        self.editBtn.clicked.connect(self.editProfile)

    def closeProfile(self):
        self.pack()  
        self.close()
        self.parent.show()
        del self
        pass

    def unPack(self,data=None):
        if data==None:
            return
        #for i in range(0,len(data)):
            #print(f"Check: {i} ",data[i])
        self.fname.setText(data[0])
        self.lname.setText(data[1])
        self.mname.setText(data[2])
        self.gender.setText(data[3])
        self.age.setText(str(data[4]))
        self.pclass.setText(data[5])
        self.origin.setText(data[6])
        self.nationality.setText(data[7])
        self.mobile.setText("+234"+str(data[8]))
        self.email.setText(data[9])
        self.id.setText(str(data[10]))
        self.status.setText(data[11]) 
        self.address.setText(data[12].title()+", "+data[13].title()+", "+data[14].title())
        
        self.regdate.setText(data[15].replace("_",":"))
        self.admdate.setText(data[16].replace("_",":"))

        self.kfname.setText(data[17].title())
        self.klname.setText(data[18].title())
        self.kmobile.setText("+234"+str(data[19]))
        self.krelation.setText(str(data[20]).title()) 
        self.kaddress.setText(data[21].title()+", "+data[22].title()+", "+data[23].title())
        self.editProfile(True)
        return
        
    def pack(self):
        data = [
            self.fname.text(),self.lname.text(),self.mname.text(),
            self.gender.text(),self.age.text(),self.pclass.text(),
            self.origin.text(),self.nationality.text(),self.mobile.text(),
            self.email.text(),self.id.text(),self.status.text(),
            self.address.text().split(",")[-2],self.address.text().split(",")[-1],
            self.kfname.text(),self.klname.text(),self.kmobile.text(),self.krelation.text(),
            self.kaddress.text(),self.kaddress.text().split(",")[-2],self.kaddress.text().split(",")[-1]
            ]
        self.editProfile(True)
        pass

    def updateProfile(self):
        pass

    def editProfile(self,edit=False):
        self.mobile.setReadOnly(edit),self.email.setReadOnly(edit),self.address.setReadOnly(edit),
        self.kfname.setReadOnly(edit),self.klname.setReadOnly(edit),self.kmobile.setReadOnly(edit),
        self.krelation.setReadOnly(edit),self.kaddress.setReadOnly(edit)
        pass

class Appointment(PySide2.QtWidgets.QDialog,Ui_ApptSlip):
    def __init__(self,parent=None):
        super().__init__(parent = None)
        self.__initUI__(parent)
        self.parent = parent 
        self.data = parent.data
        self.press_pos = PySide2.QtCore.QPoint()
        self.Load() # Load list of doctors available
        self.cardNum.setText(str(self.data[10])) 
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True) 

        screen = self.screen().size()
        w,h = int(0.32*screen.width()),int(0.39*(screen.height()-50))
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

    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.press_pos))
    
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.cancel)
        self.miniBtn.clicked.connect(self.showMinimized) 
        self.bookBtn.clicked.connect(self.book)
        self.cancelBtn.clicked.connect(self.cancel) 

    def cancel(self): 
        self.hide()
        self.parent.show()
    
    def Load(self):
        pass

    def book(self):
        pass

