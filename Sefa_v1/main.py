# This Python file uses the following encoding: utf-8
import os, sys, random, Form, datetime

folder =sys.path[0]+"\\resources"
ui = Form.UI(folder)
if not ui.getModules():
    sys.exit()

from PySide2.QtWidgets import (QApplication,QWidget,QDialog,
QTableWidgetItem,QPushButton,QMessageBox,QLineEdit)
from PySide2.QtCore import Qt, QSize, QTimer,QPoint
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery
from Ui_Auth import Ui_Auth
from Ui_Start import Ui_Start
from Ui_Reception import Ui_Reception
from Ui_PForm import Ui_PForm
from Ui_PSearch import Ui_PSearch
from Ui_PRecord import Ui_PRecord
from Ui_dSchedule import Ui_dSchedule
from Ui_ApptDialog import Ui_ApptDialog
from Ui_Billing import Ui_Billing
from Ui_PReview import Ui_PReview


class Start(QDialog,Ui_Start):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__initUI__(parent)
        timer = QTimer(self)
        timer.singleShot(10*1000,self.Hide) 

    def __initUI__(self, parent):
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.addLogo()
        self.show()

    def addLogo(self):
        path = sys.path[0]+"\\resources\\Sefa Logo3.png" 
        pixmap = QPixmap(path)
        self.logo.setPixmap(pixmap.scaled(self.logo.width(),
        self.logo.height()))
        
    def Hide(self):  
       self.parent.show()
       self.close()
        





class Auth(QDialog,Ui_Auth):
    def __init__(self):
        super().__init__() 
        self.__initUI__()

    def __initUI__(self):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.UpdateImg()
        self.addLogo()
        self.SlotSignals()
        # mask passord inputs
        self.regPaswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.regPaswd.setStyleSheet('lineedit-password-character: 9679')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet('lineedit-password-character: 9679')
        
    def getImage(self):
        imgdir = sys.path[0]+"\\resources\\photos\\" 
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
    
    def LoginButtonClicked(self):
        print("Login Button Clicked")
        #....
        #.... connect to database and confirm login details
        recep = Reception(self)

    def RegButtonClicked(self):
        print("Register button Clicked!")
        #....
        #.... connect to database and insert new details
        self.stackedWidgets.setCurrentIndex(0)
    
    def addLogo(self):
        path = sys.path[0]+"\\resources\\Sefa Logo2.png" 
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(self.logo.size())
        self.logo.setPixmap(pixmap)
        self.imgView.setPixmap(pixmap)

    def SlotSignals(self):
        self.regCancel.clicked.connect(lambda: self.stackedWidgets.setCurrentIndex(0))
        self.linkReg.clicked.connect(lambda: self.stackedWidgets.setCurrentIndex(1))
        self.loginButton.clicked.connect(self.LoginButtonClicked)
        self.regButton.clicked.connect(self.RegButtonClicked)
        self.closeButton.clicked.connect(self.close)
        self.minButton.clicked.connect(self.showMinimized)
        self.authID.textChanged.connect(self.regButton.show)
        self.linkReg.pressed.connect(self.regButton.hide)
        self.regButton.pressed.connect(self.authID.clear)
        self.regCancel.pressed.connect(self.authID.clear)





class Reception(QDialog,Ui_Reception):
    def __init__(self, parent):
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
        self.repLogOut.clicked.connect(self.LogOut)
        self.closeButton.clicked.connect(self.LogOut)
        self.minButton.clicked.connect(self.showMinimized)
        self.recordBtn.clicked.connect(self.Search)
        self.billingBtn.clicked.connect(self.Bill)
        self.docScheduleBtn.clicked.connect(self.DocSchedule)
        self.createAptBtn.clicked.connect(self.CreateAppt)

    def LogOut(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()
    
    def Search(self):
        search = PSearch(self)
    
    def CreateAppt(self):
        appt = ApptDialog(self)
    
    def Bill(self):
        bill = Billing(self)
    
    def DocSchedule(self):
        schedule = DocScheduler(self)


class DocScheduler(QDialog,Ui_dSchedule):
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

    def Close(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()

class ApptDialog(QDialog,Ui_ApptDialog):
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
        self.bookBtn.clicked.connect(self.Book)
        self.cancelBtn.clicked.connect(self.Close)
        self.doclists.clicked.connect(self.GetAvailableDoctor)
        self.scheduledTime.clicked.connect(self.Gettime)

    def Close(self):
        # run other things
        self.close() 
    
    def Show(self): 
        # run other things
        self.show()
    
    def Book(self):
        # send schedule and update doctors schedule status
        # request to print slip
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Print Slip")
        msg.setText("Would you like to print slip")
        yesBtn = QPushButton(msg,"Yes")
        noBtn  = QPushButton(msg,"No")
        msg.addButton(yesBtn|noBtn)
        yesBtn.clicked.connect(self.PrintSlip)
        noBtn.clicked.connect(msg.Abort)
        msg.exec_()
    
    def GetAvailableDoctor(self):
        # get available doctors from database
        # show list of available doctors
        pass

    def Gettime(self):
        #time = scheduledTime.text()
        pass

    def PrintSlip(self):
        print("slip printed!")
        pass

        

class Billing(QDialog,Ui_Billing):
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


class PSearch(QDialog,Ui_PSearch):
    def __init__(self, parent):
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
        self.pCloseSearch.clicked.connect(self.Close)
        self.closeButton.clicked.connect(self.Close)
        self.minButton.clicked.connect(self.showMinimized)
        self.pCreateNew.clicked.connect(self.Register)
        self.pSearch.clicked.connect(self.Search)

    def Close(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()
    
    def Search(self):
        # ...
        # found
        p = []
        precord = PRecord(self,p)
    
    def Register(self):
        pform = PForm(self)




class PForm(QWidget,Ui_PForm):
    def __init__(self, parent):
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
        self.pCancel.clicked.connect(self.Close)
        self.closeButton.clicked.connect(self.Close)
        self.minButton.clicked.connect(self.showMinimized)

    def Close(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()
    
    def Register(self):
        #... database register
        #... pass variable of patients 
        #fname = self.pFirstname.text()
        #lname = self.pLastname.text()
        #g = self.pGender.text()
        #a = self.pAge.text()
        #c = self.pClass.text()
        #ad= self.pDoctor.text()
        p = []
        #... p = [fname,lname,g,a,c,ad]
        precord = PRecord(self,p)



class PRecord(QDialog,Ui_PRecord):
    def __init__(self, parent,patient):
        super().__init__(parent)
        self.__initUI__(parent)
        self.tindex = 0 #table index
        #self.recordID = patient.id

    
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
        self.addNewBtn.clicked.connect(self.AddNew)
        self.closeBtn.clicked.connect(self.Close)
        self.deleteBtn.clicked.connect(self.Delete)
    
    def Show(self):
        # ... this function unpacks and 
        # shows patient's record
        self.parent.close()
        self.show()  

    def AddNew(self): 
        self.table.setRowCount(self.tindex+1)
        item1 = QTableWidgetItem("19/01/2021")
        self.table.setItem(self.tindex,0,item1)
        item2 = QTableWidgetItem("Dr. Ahmadu Bello")
        self.table.setItem(self.tindex,1,item2)
        item3 = QTableWidgetItem("ChickPox,Typhoid")
        self.table.setItem(self.tindex,2,item3)
        item4 = QTableWidgetItem("Prescription")
        self.table.setItem(self.tindex,3,item4)
        item5 = QPushButton("View")
        item5.clicked.connect(self.OnClickView)
        self.table.setCellWidget(self.tindex,4,item5)
        self.tindex = self.tindex+1 #increment
        print("Added new record "+str(self.tindex))

    def Close(self):
        # ...this function repacks closes 
        # the patient's record
        print("Patient record closed")
        self.close()
        self.parent.show()

    def Delete(self):
        # ... this function only deletes newly created 
        # or unsigned records
        print("Record deleted!")
    
    def OnClickView(self):
        button = self.sender()
        index = self.table.indexAt(button.pos())
        if index.isValid():
            if button.text()=="View":
                self.OnView(index)
            else:
                self.OnCreate()
        print(index.row(),index.column())

    def OnView(self,index):
        date = self.table.itemAt(QPoint(int(index.row()),0))
        print("Date: ",date.text())
        if not (date.text() == ""):
            wnd=PReview(self)
        else:
            self.OnCreate()

    def OnCreate(self):
        print("A new record for patient 0000000000 has been created!")

class PReview(QDialog,Ui_PReview):
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
        self.cancel.clicked.connect(self.Close)
        self.save.clicked.connect(self.Save)
        self.commit.clicked.connect(self.Commit)
        self.commit_2.clicked.connect(self.Commit("Prescription"))

    def Close(self):
        self.close()
        self.parent.show()
    
    def Show(self):
        self.parent.close()
        self.show()
    
    def Save(self):
        self.Close()
    
    def Commit(self,cat=""):
        self.Close()



class DatabaseHandle(QSqlDatabase):
    def __init__(self):
        super().__init__() 

    def setupConnection(self):
        if self.contains(self.conn):
            print("this connection exist")

        else: # setup new connection
            self.addDatabase("QSQLITE",self.conn)
            self.setDatabaseName(self.dbname+".db") # 
            self.setHostName(self.dept)
            self.setUserName(self.user)
            self.setPassword(self.pswd)
    
    def connect(self,user="",pswd=""):
        self.database(self.conn)
        if not self.isOpen():
            try: 
                self.res = self.open(user,pswd)
            except:
                self.errorMsg("Database Error: %s" % self.lastError().databaseText())
            finally:
                self.dbMsg("Connection Successful!")
                self.query = QSqlQueryModel(self.conn)
        else:
            self.dbMsg("Existing Connection Found!") 

    def dbRegister(self,parent):
        self.fname  = parent.fname     #employee's firstname
        self.lname  = parent.lname     #employee's last name
        self.dept   = parent.dept      #employee's department
        self.Id     = parent.Id        #employee's id
        self.role   = parent.role      #job title
        self.rank   = parent.rank      #rank or additonal role
        self.user   = parent.username  #employee's username
        self.pswd   = parent.pswd      #employee's pswd
        self.conn   = self.user+"_"+self.Id+"_con"
        self.dbname = "Employees" 

        # create a connection
        self.setupConnection()
        self.connect()
        # create table
        self.query.exec("""
                        CREATE TABLE Employees_db(
                            EmployeeID INTEGER PRIMARY KEY NOT NULL,
                            Username VARCHAR(20) NOT NULL,
                            Password INTEGER(8) NOT NULL,
                            Firstname VARCHAR(40) NOT NULL,
                            Lastname VARCHAR(40) NOT NULL,
                            Department VARCHAR(40) NOT NULL,
                            Role VARCHAR(50) NOT NULL,
                            Rank VARCHAR(40) NOT NULL,
                            Email VARCHAR(100) NOT NULL
                        )
                        """)
        print(self.conn.tables())

    
    def setupDatabase(self,dbname):
        self.dbname = dbname
        
    def errorMsg(self,msg):
        msgBox = QMessageBox(self.parent)
        msgBox.setIcon(QMessageBox().Critical())
        msgBox.setText(msg)
        msgBox.setWindowTitle("Database - Error!")
        retcode = msgBox.exec_()
        sys.exit(1) # exit with failure

    def dbCreateTable(self,sqlheader):
        self.query.exec(f"""CREATE TABLE {self.dbname} ({sqlheader})""")

    def dbUpdateTable(self,data):# data list to add to table
        columns = self.query.exec(f"""SELECT COLUMN_NAME FROM 
        INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {self.dbname} ORDER BY ORDINAL_POSITION""")
        self.query.exec(f"""INSERT INTO {self.dbname} ({columns})""")

    def dbMsg(self,msg):
        msgBox = QMessageBox(self.parent)
        msgBox.setIcon(QMessageBox().Information())
        msgBox.setText(msg)
        msgBox.setWindowTitle("Database")
        retcode = msgBox.exec_()
        return msg
    
    def dbCheckPriviledge(self):
        pass

    def dbValidateLogin(self,user,pswd):
        pass

    def dbLogin(self,login):

        pass

    def dbClose(self,name):
        pass
    
    def dbGet(self,label,data):
        pass















class Main:
    def __init__(self):
        super().__init__()

            

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    # ... 
    #parents = [Reception()]

    auth = Auth()
    dialog = Start(auth) 
    # ...
    sys.exit(app.exec_())
