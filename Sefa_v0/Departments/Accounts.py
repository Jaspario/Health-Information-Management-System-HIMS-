from resources.interface._py.Ui_Billing import Ui_Billing


class __Billing__(QDialog,Ui_Billing):
    def __init__(self,parent):
        super().__init__(parent)
        self.__initUI__(parent)

    def __initUI__(self,parent):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.parent = parent
        self.addLogo()
        self.Show()
        self.SlotSignals()

    def addLogo(self):
        path = sys.path[0]+"\\resources\\Sefa Logo2.png" 
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(self.logo.size())
        self.logo.setPixmap(pixmap)

    def SlotSignals(self):
        self.closeButton.clicked.connect(self.Close)
        self.minButton.clicked.connect(self.showMinimized)
        self.remove.clicked.connect(self.Remove)
        self.print.clicked.connect(self.Print)
        self.calculate.clicked.connect(self.Calculate)
        self.add.clicked.connect(self.AddNew)

    def Close(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()
    
    def Remove(self):
        #used to pop up the last added item
        self.Close()
    
    def Print(self):
        #used to print the generated slip
        self.Close()

    def Calculate(self):
        #used to calculate the total cost
        self.Close()
    
    def AddNew(self):
        #used to add new item to the list
        self.Close()


