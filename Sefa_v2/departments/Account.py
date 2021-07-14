from importLib import *
from interface.UiAccountRecord import Ui_AccountRecord
from departments.Records import Records

class Account(QDialog,Ui_AccountRecord):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.Load()
        self.__initUI__()
        self.signalSlot()
        self.addLogo()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.onClose)
        self.miniBtn.clicked.connect(self.mini) 

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
    
    def mini(self):
        self.showMinimized()
    
    def onClose(self):
        self.Save()
        self.hide()
        self.parent.show()
    
    def Load(self):
        pass

    def Save(self):
        pass
