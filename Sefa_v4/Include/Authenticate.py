from Lib.importlib import * 
from Include.interface.UiAuthenticate import Ui_Authenticate
from Include.departments.Home import Home

class Login(QtWidgets.QDialog,Ui_Authenticate):
    
    def __init__(self, parent=None,database=None):
        super().__init__(parent=None)
        self.parent = parent
        self.database = database
        # define table header as a tuple
        columns  = ('usersname TEXT UNIQUE NOT NULL','password BLOB NOT NULL','firstname TEXT NOT NULL','lastname TEXT NOT NULL','gender TEXT NOT NULL','employeeID INT UNIQUE PRIMARY KEY NOT NULL','department TEXT NOT NULL','jobtitle TEXT NOT NULL','rank INT NOT NULL','phone INT UNIQUE NOT NULL','email BLOB','authorizedID INT NOT NULL','authorizedBy TEXT NOT NULL')
        self.database.createTable(table='Users',columns=columns) 
        self.__initUI__(parent)
        self.flipImages()

        self.child1 = None # find patient
        self.child2 = None # admin
        self.child3 = None # lab
        self.child4 = None # pharmacy
        self.child5 = None # medical
        self.user   = None # login details

    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        w,h = int(0.65*screen.width()),int(0.9*(screen.height()-50))
        self.setFixedSize(w,h)

        self.loginStatus.hide()
        self.regStatus.hide()
        self.updateStatus.hide()
        self._signalShot()

    # get image 
    def getImage(self):
        file = random.choice([x for x in os.listdir(imgdir)
            if os.path.isfile(os.path.join(imgdir,x))])
        return os.path.join(imgdir,file)    

    # display image
    def displayImage(self):
        img = self.getImage()
        pixMap = QtGui.QPixmap(img)
        if not pixMap.isNull(): 
            self.imgView.setScaledContents(True)
            pixMap = pixMap.scaled(self.imgView.size())
            self.imgView.setPixmap(pixMap)

    # flip images
    def flipImages(self): 
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.displayImage)
        timer.start(300*30)

    # on click actions
    def _signalShot(self): 
        self.loginBtn.clicked.connect(self.LoginClicked)
        self.password.returnPressed.connect(self.LoginClicked)
        self.updateBtn.clicked.connect(self.UpdateClicked)
        self.contactBtn.clicked.connect(self.ContactAuthorClicked)
        self.registerBtn.clicked.connect(self.RegisterClicked)
        self.reglinkBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.updatelinkBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.regCancelBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.updateCancelBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))

# update employee info
    def UpdateClicked(self):
        pass
    # login registered employee
    def LoginClicked(self):
        user = self.userid.text()
        pswd = self.password.text()
        if user=="" or pswd=="":
            self.flashMsg("Invalid login details!")
            return 
        else:
            user,msg = self.database.login(table='Users',user=user,paswd=pswd)
            if msg == 'Invalid':
                self.flashMsg("Invalid username or password!")
                self.password.clear() 
            else:
                self.flashMsg(f"{msg} you are welcomed to {user[3]} department!") 
                self.user = user
                timer = QtCore.QTimer(self) 
                timer.singleShot(3010,self.reveal) 
        return
    # register employee
    def RegisterClicked(self):
        #.... setup database
        regInfo = [ [self.regUserid.text(),"Username"],
                    [self.regPaswd.text(),"Password"],
                    [self.firstname.text().lower(),"Firstname"],
                    [self.surname.text().lower(),"Lastname"],
                    [self.gender.currentText().lower(),"Gender"],
                    [self.employeeID.text(),"Employment ID"],
                    [self.dept.currentText().lower(),"Department"],
                    [self.jobtitle.currentText().lower(),"Job Title"], 
                    [self.rank.currentText(),"Rank"],
                    [self.phone.text(),"Phone Number"],
                    [self.email.text(),"Email"],
                    [self.authID.text(),"Authorized ID"],
                    ] 
        for line in regInfo:
            if line[0] == '':
                self.flashMsg(f"Please input {line[1]}")
                return
            else:
                try:
                    index = regInfo.index(line) 
                    regInfo.__setitem__(index,line[0])
                except ValueError:
                    print(f"{line[1]} not present in list")

        if self.register(table='Users',data=regInfo):
            self.clearRegField()
            regInfo.clear()
        return

    # contact system author
    def ContactAuthorClicked(self):
        pass
    

    def flashMsg(self,msg=""):
        timer = QtCore.QTimer(self)
        if self.stackedWidget.currentIndex() == 2:
            self.loginStatus.setText(msg)
            self.loginStatus.show()
            timer.singleShot(3000,self.reset_status)
        elif self.stackedWidget.currentIndex() == 0:
            self.regStatus.setText(msg)
            self.regStatus.show()
            timer.singleShot(3000,self.reset_status)
        else:
            self.updateStatus.setText(msg)
            self.updateStatus.show()
            timer.singleShot(3000,self.reset_status)
        return timer.isActive()==False

    def reset_status(self):
        if self.stackedWidget.currentIndex() == 2:
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
                self.flashMsg('Successfully Registered {} {}'.format(data[2],data[3]))
                return True
        return False

    def clearRegField(self):
        self.regUserid.clear()
        self.regPaswd.clear()
        self.firstname.clear()
        self.surname.clear() 
        self.employeeID.clear()  
        self.phone.clear()
        self.email.clear()
        self.authID.clear()
        self.stackedWidget.setCurrentIndex(2)
        self.flashMsg("")

    def reveal(self):
        self.child1 = Home(self,database=self.database)
        self.child1.show()
        self.hide()
        self.password.clear() 