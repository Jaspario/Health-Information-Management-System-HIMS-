from Lib.importlib import *
from Include.interface.UiRegister import Ui_Register

class   Register(QtWidgets.QDialog,Ui_Register):
    def __init__(self, parent=None, database = None):
        super().__init__(parent=None)
        self.__initUI__(parent=None)
        self.parent = parent
        self.database = database
        self.user = parent.user 
        self.table = parent.table
        # define table header as a tuple
        columns  = ('firstname TEXT NOT NULL','lastname TEXT NOT NULL','othername TEXT NOT NULL','gender TEXT NOT NULL','age INT NOT NULL','class TEXT NOT NULL','origin TEXT NOT NULL','nationality TEXT NOT NULL','mobile INT UNIQUE NOT NULL','email BLOB','patientID INT PRIMARY KEY NOT NULL','status TEXT NOT NULL','address TEXT NOT NULL','state TEXT NOT NULL','country TEXT NOT NULL','regDate TEXT NOT NULL','admissionDate TEXT NOT NULL','kin_firstname TEXT NOT NULL','kin_lastname TEXT NOT NULL','kin_mobile INT UNIQUE NOT NULL','kin_relationship TEXT NOT NULL','kin_address TEXT NOT NULL','kin_state TEXT NOT NULL','kin_country TEXT')
        self.database.createTable(table=self.table,columns=columns) 
        dt = datetime.datetime.now() 
        self.regDate.setDateTime(dt)
        self.admissionDate.setDateTime(dt)
        self.show()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icondir)) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        width  = int(0.45*screen.width())
        height = int(0.85*(screen.height()-50))

        self.setFixedSize(width,height)
        self._signalShot()
        self.clearField() 

    def _signalShot(self):
        self.cancelBtn.clicked.connect(self.closeRegister)
        self.regBtn.clicked.connect(self.register) 

    def closeRegister(self):
        self.database.disconnect()
        self.clearField()
        self.pinfo.hide()
        self.close()
        self.parent.show()
        pass

    def bookAppt(self):
        pass 

    def clearField(self):
        self.pinfo.hide()
        self.fname.clear()
        self.lname.clear()
        self.age.clear() 

    def register(self): 
        if self.user[2] != 'receptionist':
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Sefa (HIMS)-Warning!")
            msg.setText('Only a receptionist is allow to modify or register a patient!') 
            msg.exec_() 
            return
        else: 
            data = [
            [self.fname.text().lower(),"Firstname"],
            [self.lname.text().lower(),"Lastname"],
            [self.oname.text().lower(),"Othername"],
            [self.gender.currentText(),"Gender"],
            [self.age.text(),"Age"],
            [self.pclass.currentText(),"Class"],
            [self.origin.text().lower(),"State of Origin"],
            [self.nationality.text().lower(),"Nationality"],
            [self.phone.text(),"Phone Number"], 
            [self.email.text(),"Patient's Email"],
            [self.patientID.text(),"Patient's ID/Number"],
            [self.status.currentText(),"Patient's Status"],
            [self.address.text().lower(),"Patient's Address"],
            [self.state.text().lower(),"Patient's State"],
            [self.country.text().lower(),"Patient's Country"],
            [self.regDate.text().replace('/','-'),'Registration Date'],
            [self.admissionDate.text().replace('/','-'),'Admission Date'],
            [self.kfname.text().lower(),'Next of Kin\'s First Name'],
            [self.klname.text().lower(),'Next of Kin\'s Last Name'],
            [self.kphone.text(),'Next of Kin\'s Phone Number'],
            [self.krelationship.currentText(),"Patient's Relationship with Next of kin"],
            [self.kaddress.text().lower(),"Next of kin's address"],
            [self.kstate.text().lower(),"Next of kin's state"],
            [self.kcountry.text().lower(),"Next of kin's country"]
            ]
            
            for line in data:
                if line[0] == '' and line[1]!="Patient's Email":
                    self.setInfo(f"Please input {line[1]}")
                    return
                else:
                    try:
                        index = data.index(line) 
                        data.__setitem__(index,line[0])
                    except ValueError:
                        print(f"{line[1]} not present in list")

            if self.database.tableInsert(table=self.table,data=data):
                self.setInfo('Successfully Registered {} {}'.format(data[0],data[1])) 
                self.closeRegister()
                return True
        return False
    
    def setInfo(self,msg=""):
        self.pinfo.setText(msg)
        self.pinfo.show()

        timer = QtCore.QTimer(self)
        timer.singleShot(1000,lambda: self.pinfo.hide())


class Record(QtWidgets.QTableWidget): 
    def __init__(self,parent=None):
        super().__init__(parent.table) 
        self.parent   = parent
        self.table    = parent.table
        self.index    = parent.rowCount
        self.sealed   = False
        self.row      = None
        self.items    = [] 
        self.recbtn   = QtWidgets.QPushButton("Create")
        self.addButton()

    def setTable(self):
        columns = self.table.columnCount()-1
        for i in range(0,columns): 
            item = QtWidgets.QTableWidgetItem(self.items[i]) 
            self.table.setItem(self.index,i,item) 

    def getRowObjects(self, obj):
        self.row    = obj 

    def addButton(self):
        self.recbtn.setFlat(False)
        #self.recbtn.setStyleSheet(widget)
        self.recbtn.setToolTip("Click to insert a record") 
        self.recbtn.setCursor(QtCore.Qt.PointingHandCursor)

        columns = self.table.columnCount()
        self.recbtn.clicked.connect(self.OnClickButton)
        self.table.setCellWidget(self.index,columns-1,self.recbtn)

    def UpdateTable(self):
        text = self.GetButtonText()
        self.recbtn.setText(text)
        self.setTable()

    def OnView(self):
        self.row.show() 
        self.parent.hide()

    def OnCreate(self):
        self.row.show()   
        self.parent.hide()

    def GetButtonText(self):
        res = "Create"
        if self.sealed == True:
            res = "View" 
        return res 
    
    def OnClickButton(self):
        if self.recbtn.text() == "Create":
            self.OnCreate()

        elif self.recbtn.text() == "View":
            self.OnView()



