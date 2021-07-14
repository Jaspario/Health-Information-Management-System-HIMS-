from Departments._imports_ import*

from Departments.resources.interface._py.Ui_Auth import Ui_Auth
from Departments.resources.interface._py.Ui_Start import Ui_Start

from Departments.Database import __databaseHandler__
from Departments.Reception import __Reception__






class __Start__(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI__()
        self.parent = parent
        self.Show()

    
    def __initUI__(self):
        self.ui = Ui_Start()
        self.ui.setupUi(self)        
        self.setWindowFlag(Qt.FramelessWindowHint)  
        self.addLogo()

    def addLogo(self):
        pixmap = getLogo(self.ui.logo)
        self.ui.logo.setPixmap(pixmap)

    def Hide(self):
        self.parent.show() 
        self.hide() 


    def Show(self):
        self.show()
        timer = QTimer(self)
        timer.singleShot(2*1000,self.Hide)





class __Auth__(QDialog,Ui_Auth):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=None)
        self.__initUI__()
        self.database  = __databaseHandler__()
        self.reception = __Reception__(self) 
    
    
    def __initUI__(self):
        self.setupUi(self)        
        self.setWindowFlag(Qt.FramelessWindowHint) 
        #....
        self.addLogo()
        self.UpdateImg()
        #.... button Click
        self.SlotSignals()

    def SlotSignals(self):
        self.exitBtn.clicked.connect(self.OnClickExit)
        self.minBtn.clicked.connect(self.showMinimized)
        self.loginButton.clicked.connect(self.OnClickLogin)
        self.authID.textChanged.connect(self.regButton.show)
        self.regButton.pressed.connect(self.OnClickRegister)
        self.regButton.released.connect(self.authID.clear)
        self.regButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.linkReg.pressed.connect(self.regButton.hide)
        self.regCancel.pressed.connect(self.authID.clear)
        self.regCancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.linkReg.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self.imgView.setPixmap(pixmap)

    def getImage(self):
        imgdir = sys.path[0]+"\\Departments\\resources\\photos\\" 
        file = random.choice([x for x in os.listdir(imgdir)
                if os.path.isfile(os.path.join(imgdir,x))])
        return os.path.join(imgdir,file)
        
    def UpdateImg(self):
        timer = QTimer(self)
        timer.timeout.connect(self.DisplayImg)
        timer.start(300*60)
    
    def DisplayImg(self):
        img = self.getImage()
        pixMap = QPixmap(img)
        if not pixMap.isNull():
            pixMap = pixMap.scaled(self.imgView.size())
            self.imgView.setPixmap(pixMap)
    
    def OnClickExit(self):
        if mssgBox(self,"Do you want to exit this App?"):
            sys.exit()
    
    def OnClickLogin(self):
        self.user = self.username.text()
        self.pswd = self.password.text()
        # ....
        if self.database.dbLogin(self.user,self.pswd):
            self.hide()
            self.reception.show()
        self.password.clear()


    def OnClickRegister(self):
        #.... setup database
        if self.database.Register(self):
            msg = "Registration Successful!"
        else: msg = "Already registered!"
        self.label.setText(msg)
        self.label.show()