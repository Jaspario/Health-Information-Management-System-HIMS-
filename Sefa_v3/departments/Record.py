from Importlib import *
from interface.UiRegister import Ui_Register  


class Register(PySide2.QtWidgets.QDialog,Ui_Register):
    def __init__(self, parent=None):
        super().__init__(parent=None) 
        self.__initUI__(parent) 
        self.parent = parent
        self.owner = parent.owner
        self.table = parent.table
        self.database = parent.database
        # define table header as a tuple
        columns  = ('firstname TEXT NOT NULL','lastname TEXT NOT NULL','othername TEXT NOT NULL','gender TEXT NOT NULL','age INT NOT NULL','class TEXT NOT NULL','origin TEXT NOT NULL','nationality TEXT NOT NULL','mobile INT UNIQUE NOT NULL','email BLOB','patientID INT PRIMARY KEY NOT NULL','status TEXT NOT NULL','address TEXT NOT NULL','state TEXT NOT NULL','country TEXT NOT NULL','regDate TEXT NOT NULL','admissionDate TEXT NOT NULL','kin_firstname TEXT NOT NULL','kin_lastname TEXT NOT NULL','kin_mobile INT UNIQUE NOT NULL','kin_relationship TEXT NOT NULL','kin_address TEXT NOT NULL','kin_state TEXT NOT NULL','kin_country')
        self.database.createTable(table=self.table,columns=columns) 
        self.show()
    # initialize ui
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowIcon(PySide2.QtGui.QIcon(icondir)) 
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        
        screen = self.screen().size()
        size = PySide2.QtCore.QSize(int(0.42*screen.width()),int(0.92*(screen.height()-50)))
        self.setFixedSize(size)
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
        self.clearField() 
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
    
    #def mousePressEvent(self, event):
        #if event.recbtn() == PySide2.QtCore.Qt.Leftrecbtn:
            #self.__press_pos = event.pos()  

    #def mouseReleaseEvent(self, event):
        #if event.recbtn() == PySide2.QtCore.Qt.Leftrecbtn:
            #self.__press_pos = PySide2.QtCore.QPoint()

    #def mouseMoveEvent(self, event):
        #if not self.__press_pos.isNull():  
            #self.move(self.pos() + (event.pos() - self.__press_pos))
    # on click actions
    def _signalShot(self):
        self.exitBtn.clicked.connect(self.exitApp)
        self.miniBtn.clicked.connect(self.showMinimized)
        self.cancelBtn.clicked.connect(self.closeRegister)
        self.regBtn.clicked.connect(self.register)
        self.bookBtn.clicked.connect(self.bookAppt)

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
        self.pfname.clear()
        self.plname.clear()
        self.pgender.setCurrentIndex(0)
        self.page.clear()
        self.bookBtn.setEnabled(False) 

    def register(self): 
        timer = PySide2.QtCore.QTimer(self)
        if self.owner[2] != 'receptionist':
            msg = PySide2.QtWidgets.QMessageBox(self)
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Sefa (HIMS)-Warning!")
            msg.setText('Only a receptionist is allow to modify or register a patient!') 
            msg.exec_() 
            return
        else:
            dt = datetime.datetime.now()
            dt_string = dt.strftime("%d-%m-%Y %H_%M_%S")
            print("Date:", dt_string)
            return
            data = [
            [self.pfname.text().lower(),self.pfnamelbl.text().strip(':')],
            [self.plname.text().lower(),self.plnamelbl.text().strip(':')],
            [self.poname.text().lower(),self.ponamelbl.text().strip(':')],
            [self.pgender.currentText(),self.pgenderlbl.text().strip(':')],
            [self.page.text(),self.pagelbl.text().strip(':')],
            [self.pclass.currentText(),self.pclasslbl.text().strip(':')],
            [self.porigin.text().lower(),self.porigin.text().strip(':')],
            [self.pnationality.text().lower(),self.pnationalitylbl.text().strip(':')],
            [self.pmobile.text(),self.pmobilelbl.text().strip(':')],
            [self.pemail.text(),self.pemaillbl.text().strip(':')],
            [self.pnumber.text(),self.pnumberlbl.text().strip(':')],
            [self.pstatus.currentText(),self.pstatuslbl.text().strip(':')],
            [self.paddressL1.text().lower(),self.paddressL1lbl.text().strip(':')],
            [self.pstate.text().lower(),self.pstatelbl.text().strip(':')],
            [self.pcountry.text().lower(),self.pcountrylbl.text().strip(':')],
            [dt_string,'Registration Date'],
            [dt_string,'Admission Date'],
            [self.pkfname.text().lower(),'Next of Kin First Name'],
            [self.pklname.text().lower(),'Kin ' + self.pklnamelbl.text().strip(':')],
            [self.pkmobile.text(),'Kin '+ self.pkmobilelbl.text().strip(':')],
            [self.pkrelationship.currentText(),'Kin '+ self.pkrelationshiplbl.text().strip(':')],
            [self.pkaddressL1.text().lower(),'Kin '+ self.pkaddressL1lbl.text().strip(':')],
            [self.pkstate.text().lower(),'Kin '+self.pkstatelbl.text().strip(':')],
            [self.pkcountry.text().lower(),'Kin '+self.pkcountrylbl.text().strip(':')]
            ]
            
            for line in data:
                if line[0] == '':
                    print(f"Please input {line[1]}")
                    return
                else:
                    try:
                        index = data.index(line) 
                        data.__setitem__(index,line[0])
                    except ValueError:
                        print(f"{line[1]} not present in list")
            # check in developer's console
            #for value in data:
                #print(f"Store valued = {value}")

            if self.database.tableInsert(table=self.table,data=data):
                self.pinfo.setText('Successfully Registered {} {}'.format(data[0],data[1]))
                timer.singleShot(1000,lambda: self.pinfo.setText(''))
                self.closeRegister()
                return True
        return False

class Record(PySide2.QtWidgets.QTableWidget): 
    def __init__(self,parent=None):
        super().__init__(parent.table) 
        self.parent   = parent
        self.table    = parent.table
        self.status   = "Unsigned"
        self.row      = None
        self.items    = [] 
        self.index    = parent.rowCount
        self.recbtn   = PySide2.QtWidgets.QPushButton("Create")
        self.addButton()

    def setTable(self):
        columns = self.table.columnCount()-1
        for i in range(0,columns): 
            item = PySide2.QtWidgets.QTableWidgetItem(self.items[i]) 
            self.table.setItem(self.index,i,item) 

    def getRowObjects(self,obj):
        self.row    =obj 

    def addButton(self):
        self.recbtn.setFlat(False)
        self.recbtn.setStyleSheet(widget)
        self.recbtn.setToolTip("Click to insert a record") 
        self.recbtn.setCursor(PySide2.QtCore.Qt.PointingHandCursor)
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
        if self.status == "Signed":
            res = "View" 
        return res 
    
    def OnClickButton(self):
        if self.recbtn.text() == "Create":
            self.OnCreate()
        elif self.recbtn.text() == "View":
            self.OnView()



