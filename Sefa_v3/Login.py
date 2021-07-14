from Importlib import *
from interface.UiAuth import Ui_Auth
from departments.home import Home


class Auth(PySide2.QtWidgets.QDialog,Ui_Auth):
    
    def __init__(self, parent=None,database=None):
        super().__init__(parent=None)
        self.validate = False
        self.parent = parent
        self.user  = None
        self.data = self.user
        self.__press_pos = PySide2.QtCore.QPoint()
        self.database = database
        # define table header as a tuple
        columns  = ('usersname TEXT UNIQUE NOT NULL','password BLOB NOT NULL','firstname TEXT NOT NULL','lastname TEXT NOT NULL','gender TEXT NOT NULL','employeeID INT UNIQUE PRIMARY KEY NOT NULL','department TEXT NOT NULL','jobtitle TEXT NOT NULL','rank INT NOT NULL','phone INT UNIQUE NOT NULL','email BLOB','authorizedID INT NOT NULL','authorizedBy TEXT NOT NULL')
        self.database.createTable(table='Users',columns=columns) 
        self.__initUI__(parent)
        self.flipImages()
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlag(PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)

        screen = self.screen().size()
        w,h = int(0.65*screen.width()),int(0.9*(screen.height()-50))
        self.setFixedSize(w,h)
        self.bgLayer.setFixedSize(w,h)
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

        self.loginStatus.hide()
        self.regStatus.hide()
        self.updateStatus.hide()
        self._signalShot()

        self.child1 = None # find patient
        self.child2 = None # admin
        self.child3 = None # lab
        self.child4 = None # pharmacy
        self.child5 = None # medical
    
    def mousePressEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.__press_pos = event.pos()  

    def mouseReleaseEvent(self, event):
        if event.button() == PySide2.QtCore.Qt.LeftButton:
            self.__press_pos = PySide2.QtCore.QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():  
            self.move(self.pos() + (event.pos() - self.__press_pos))
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
        sys.exit()
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)
        self.loginBtn.clicked.connect(self.LoginClicked)
        self.password.returnPressed.connect(self.LoginClicked)
        self.updateBtn.clicked.connect(self.UpdateClicked)
        self.contactBtn.clicked.connect(self.ContactAuthorClicked)
        self.registerBtn.clicked.connect(self.RegisterClicked)
        self.reglinkBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.updatelinkBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.regCancelBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.updateCancelBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
    # get image 
    def getImage(self):
        file = random.choice([x for x in os.listdir(imgdir)
            if os.path.isfile(os.path.join(imgdir,x))])
        return os.path.join(imgdir,file)    
    # display image
    def displayImage(self):
        img = self.getImage()
        pixMap = PySide2.QtGui.QPixmap(img)
        if not pixMap.isNull(): 
            self.imgView.setScaledContents(True)
            pixMap = pixMap.scaled(self.imgView.size())
            self.imgView.setPixmap(pixMap)
    # flip images
    def flipImages(self): 
        timer = PySide2.QtCore.QTimer(self)
        timer.timeout.connect(self.displayImage)
        timer.start(300*30)
    # update employee info
    def UpdateClicked(self):
        pass
    # login registered employee
    def LoginClicked(self):
        self.user = self.userid.text()
        self.pswd = self.password.text()
        if self.user=="" or self.pswd=="":
            self.flashMsg("Invalid login details!")
            return 
        else:
            self.user,msg = self.database.login(table='Users',user=self.user,paswd=self.pswd)
            if msg == 'Invalid':
                self.flashMsg("Invalid username or password!")
                self.password.clear() 
            else:
                self.flashMsg(f"{msg} you are welcomed to {self.user[3]} department!") 
                self.data = self.user
                timer = PySide2.QtCore.QTimer(self) 
                timer.singleShot(3010,self.reveal) 
        return
    # register employee
    def RegisterClicked(self):
        #.... setup database
        regInfo = [ [self.regUserid.text(),self.userlbl.text()],
                    [self.regPaswd.text(),self.paswdlbl.text()],
                    [self.firstName.text().lower(),self.fnamelbl.text()],
                    [self.surname.text().lower(),self.lnamelbl.text()],
                    [self.gender.currentText().lower(),self.genlbl.text()],
                    [self.employeeID.text(),self.idlbl.text()],
                    [self.dept.currentText().lower(),self.deptlbl.text()],
                    [self.jobtitle.currentText().lower(),self.joblbl.text()], 
                    [self.rank.currentText(),self.ranklbl.text()],
                    [self.phone.text(),self.phonelbl.text()],
                    [self.email.text(),self.emaillbl.text()],
                    [self.authID.text(),self.authIdlbl.text()],
                    ] 
        for line in regInfo:
            if line[0] == '':
                print(f"Please input {line[1]}")
                return
            else:
                try:
                    index = regInfo.index(line) 
                    regInfo.__setitem__(index,line[0])
                except ValueError:
                    print(f"{line[1]} not present in list")
        # check in developer's console
        #for value in regInfo:
            #print(f"Store valued = {value}")

        if self.register(table='Users',data=regInfo):
            self.clearRegField()
            regInfo.clear()
        pass
    # contact system author
    def ContactAuthorClicked(self):
        pass

    def flashMsg(self,msg=""):
        timer = PySide2.QtCore.QTimer(self)
        if self.stackedWidget.currentIndex() == 0:
            self.loginStatus.setText(msg)
            self.loginStatus.show()
            timer.singleShot(3000,self.reset_status)
        else:
            self.regStatus.setText(msg)
            self.regStatus.show()
            timer.singleShot(3000,self.reset_status)
        return timer.isActive()==False

    def reset_status(self):
        if self.stackedWidget.currentIndex() == 0:
            self.loginStatus.setText("")
            self.loginStatus.hide()
        else:
            self.regStatus.setText("")
            self.regStatus.hide()
        # function register

    def register(self,table='',data=None): 
        data = list(data)
        field = 'firstname,lastname,rank'
        key = 'employeeID={}'.format(data[-1])  
        row = self.database.getRow(table,field,key)
        result = None
        if row == None:
            if data[-1]=='657895':
                result = 'VALID'
                data.append('System')
            else:
                result = 'INVALID'
        elif int(row[-1]) >= 8:
            result = 'VALID'
            data.append("{} {}".format(row[0],row[1])) 
        else:
            result = 'UNAUTHORIZED'
        self.flashMsg(result + " ID")
        
        if result == 'VALID':
            if self.database.tableInsert(table=table,data=data):
                #self.flashMsg('Successfully Registered {} {}'.format(data[2],data[3]))
                return True
        return False

    def clearRegField(self):
        self.regUserid.clear()
        self.regPaswd.clear()
        self.firstName.clear()
        self.surname.clear()
        self.gender.setCurrentIndex(0)
        self.employeeID.clear()
        self.jobtitle.clear()
        self.rank.setCurrentIndex(0)
        self.dept.clear()
        self.phone.clear()
        self.email.clear()
        self.authID.clear()
        self.stackedWidget.setCurrentIndex(0)

    def reveal(self):
        self.child1 = Home(self)
        self.child1.show()
        self.hide()
        self.password.clear() 