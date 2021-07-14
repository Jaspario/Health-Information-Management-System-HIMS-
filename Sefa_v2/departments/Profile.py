from importLib import *
from interface.UiProfile import Ui_Profile

class Profile(QDialog,Ui_Profile):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.Load()
        self.__initUI__()
        self.signalSlot()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
        self.addLogo()
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.onClose)
        self.miniBtn.clicked.connect(self.mini) 
        self.closeBtn.clicked.connect(self.onClose)

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
    

    def mini(self):
        self.showMinimized()
    
    def onClose(self): 
        self.hide()
        self.parent.show()
    
    def Load(self):
        pass

    def Save(self):
        pass
