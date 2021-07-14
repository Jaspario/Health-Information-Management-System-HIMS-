from importLib import *
from interface.UiAuth import Ui_Auth
from interface.UiStart import Ui_Start
from departments.FindPatient import FindPatient
from resources.Database import SqLiteDB
from PySide2.QtWidgets import QStackedWidget

class __Start__(QDialog,Ui_Start):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI__(parent)
        self.Show()

    def __initUI__(self,parent=None):
        self.parent = parent
        self.setupUi(self)        
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.addLogo()

    def addLogo(self):
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def Hide(self):
        self.close()
        self.setHidden(True) 

    def Show(self):
        self.show()
        timer = QTimer(self)
        timer.singleShot(1*1000,self.Hide)





class __Auth__(QDialog,Ui_Auth):

    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.__initUI__(parent=parent)
        self.home = FindPatient(self)
        self.dbname= "Employees.db" 
        self.table = "employees"
        self.id_validated = False
        self.regInfo = ""
        # define table header as a tuple
        columns  = ('usersname TEXT UNIQUE NOT NULL','password BLOB NOT NULL','firstname TEXT NOT NULL','lastname TEXT NOT NULL','gender TEXT NOT NULL','employeeID INT UNIQUE PRIMARY KEY NOT NULL','department TEXT NOT NULL','jobtitle TEXT NOT NULL','rank INT NOT NULL','phone INT UNIQUE NOT NULL','email BLOB','authorizedID INT NOT NULL','authorizedBy TEXT NOT NULL')
        self.database =  SqLiteDB(database=self.dbname,table=self.table,columns=columns)
        self.signalSlot()
        self.flipView()

    def __initUI__(self,parent=None): 
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir)) 
        self.addLogo()

    def signalSlot(self):
        self.exitBtn.clicked.connect(self.exit)
        self.miniBtn.clicked.connect(self.mini)
        self.loginBtn.clicked.connect(self.onLogin)
        self.authID.textChanged.connect(self.regButton.show)
        self.regUserid.editingFinished.connect(self.validate_username)
        self.regButton.pressed.connect(self.OnClickRegister)
        self.regButton.released.connect(self.authID.clear) 
        self.reglinkBtn.pressed.connect(self.regButton.hide)
        self.regCancel.pressed.connect(self.authID.clear)
        self.regCancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.reglinkBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        pixmap = getLogo(self.imgView)
        self.imgView.setPixmap(pixmap)
    
    def getImage(self):
        file = random.choice([x for x in os.listdir(imgdir)
            if os.path.isfile(os.path.join(imgdir,x))])
        return os.path.join(imgdir,file)
        
    def displayImage(self):
        img = self.getImage()
        pixMap = QPixmap(img)
        if not pixMap.isNull(): 
            pixMap = pixMap.scaled(self.imgView.size())
            self.imgView.setPixmap(pixMap)

    def flipView(self): 
        timer = QTimer(self)
        timer.timeout.connect(self.displayImage)
        timer.start(300*30)

    def exit(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Sefa (HIMS)")
        msg.setText("Do you want to exit this app?")
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        retcode = msg.exec_()
        if retcode == QMessageBox.Yes:
            self.close()
            sys.exit()
        return
    
    def mini(self):
        self.showMinimized()
        return
    
    def onLogin(self):
        self.user = self.userid.text()
        self.pswd = self.password.text()
        if self.user=="" or self.pswd=="":
            self.flashMsg("Please input your complete details!")
            return
        else:
            result = self.database.login(user=self.user,paswd=self.pswd)
            if result == 'Invalid':
                self.flashMsg("Invalid username or password!")
            elif self.flashMsg(f"Welcome {result}"):
                self.hide()
                self.home.show()
        self.password.clear()


    def flashMsg(self,msg=""):
        timer = QTimer(self)
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

    def OnClickRegister(self):
        #.... setup database
        regInfo = [ [self.regUserid.text(),self.userlbl.text()],
                    [self.regPaswd.text(),self.paswdlbl.text()],
                    [self.firstName.text(),self.fnamelbl.text()],
                    [self.surname.text(),self.lnamelbl.text()],
                    [self.gender.currentText(),self.genlbl.text()],
                    [self.employeeID.text(),self.idlbl.text()],
                    [self.dept.text(),self.deptlbl.text()],
                    [self.jobTitle.text(),self.joblbl.text()], 
                    [self.rank.currentText(),self.ranklbl.text()],
                    [self.phone.text(),self.phonelbl.text()],
                    [self.email.text(),self.emaillbl.text()],
                    [self.authID.text(),self.authIdlbl.text()],
                    ]
        print(regInfo)
        for line in regInfo:
            if line[0] == '':
                print(f"Please input {line[1]}")
                return
            else:
                try:
                    index = regInfo.index(line)
                    cline = line[0].replace(" ","_")
                    regInfo.__setitem__(index,cline)
                except ValueError:
                    print(f"{line[1]} not present in list")

        # check in developer's console
        for value in regInfo:
            print(f"Store valued = {value}")

        self.Register(data=regInfo)
        regInfo.clear()
        return

# function register
    def Register(self,table='',data=None):  
        print("Register {} id gotten{}".format(data,data[-1]))
        result = ''
        if table == '':
            table = self.database.dbtable
        try:
            self.database.connect()
            with self.database.con:
                cur = self.database.con.cursor()
                cur.execute(f"SELECT firstname,lastname,rank FROM {table} WHERE employeeID={self.database.scrub(data[-1])}")
                row = cur.fetchone()  
                if row == None: 
                    if self.database.scrub(data[-1]) == "657895":
                        result = 'Accepted'
                    else:result = 'Unrecognized'
                elif  row[-1] >= 8: 
                    result = 'Accepted'
                else:
                    result = 'Unauthorized'

                if result == 'Accepted':                
                    data = list(data)
                    if row == None:
                        data.append("System")
                    else:
                        data.append("{} {}".format(row[0],row[1])) 

                    if self.database.tableInsert(table=table,data=data):
                        timer = QTimer(self)
                        timer.singleShot(3100,self.clearRegField)
                        self.database.printTable()
                        self.flashMsg(f"{data[2]} {data[3]} is successfully regitered!")
                    else:
                        self.database.printTable()
                        print(f"Failed to regiter {data[2]} {data[3]}!")
                cur.close()
            self.database.disconnect()

        except self.database.Error() as e:
            print("Error occurred accessing database Error:{}".format(e))   
    
        self.flashMsg(result +" ID")
        return

    def validate_username(self):
        query = f"SELECT * FROM {self.table} WHERE username={self.regUserid.text()}"
        try:
            self.database.connect()
            cur = self.database.con.cursor()
            cur.execute(query)
            print(cur.fetchone())
            if cur.fetchone() is not None:
                self.flashMsg(f"Sorry {self.regUserid.text()} is already taken!")
            cur.close()
            self.database.Close()
        except self.database.Error() as e: 
            self.flashMsg("Name available")
            return True 
        return False

    def clearRegField(self):
        self.regUserid.clear()
        self.regPaswd.clear()
        self.firstName.clear()
        self.surname.clear()
        self.gender.setCurrentIndex(0)
        self.employeeID.clear()
        self.jobTitle.clear()
        self.rank.setCurrentIndex(0)
        self.dept.clear()
        self.phone.clear()
        self.email.clear()
        self.authID.clear()
        self.stackedWidget.setCurrentIndex(0)
