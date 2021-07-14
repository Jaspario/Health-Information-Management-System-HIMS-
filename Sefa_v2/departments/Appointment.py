from importLib import *
from interface.UiApptSlip import Ui_ApptSlip

class Appointment(QDialog,Ui_ApptSlip):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.Load() # Load list of doctors available
        self.__initUI__()
        self.signalSlot()
        self.addLogo()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.cancel)
        self.miniBtn.clicked.connect(self.mini) 
        self.bookBtn.clicked.connect(self.book)
        self.cancelBtn.clicked.connect(self.cancel)

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def mini(self):
        self.showMinimized()
    
    def cancel(self): 
        self.hide()
        self.parent.show()
    
    def Load(self):
        pass

    def book(self):
        pass
