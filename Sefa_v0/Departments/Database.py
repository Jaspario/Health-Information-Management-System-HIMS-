from Departments._imports_ import *
from PySide2.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery

class __databaseHandler__(QSqlDatabase):
    def __init__(self):
        super().__init__() 
    
    def setupConnection(self):
        if self.con.contains(self.conn): 
            self.con = self.database(self.conn)
        else:
            self.setupDatabase()
        return
    
    def setupDatabase(self):
        self.con = self.addDatabase("QSQLITE",self.connName)
        self.con.setDatabaseName(self.dbname+".db") # 
        self.con.setHostName("localhost")
        self.con.setUserName("root")
        self.con.setPassword("")

    def connect(self):
        if not self.con.open():
            self.errorMsg("Database Error: %s" % self.con.lastError().databaseText())
        else:
            self.dbMsg("Connection Successful!")
            self.query = QSqlQueryModel(self.conn)


    def dbRegister(self,parent,info):
        employeeInfo     = []
        employeeInfo[0]  = parent.employeeID.text()
        employeeInfo[1]  = parent.regUserid.text()
        employeeInfo[2]  = parent.regPaswd.text()
        employeeInfo[3]  = parent.firstName.text()
        employeeInfo[4]  = parent.surname.text()
        employeeInfo[5]  = parent.gender.text()
        employeeInfo[6]  = parent.dept.text()
        employeeInfo[7]  = parent.jobTitle.text()
        employeeInfo[8]  = parent.rank.text()
        employeeInfo[9]  = parent.phone.text()
        employeeInfo[10] = parent.email.text()

        employeeInfo[11] = ""
        employeeInfo[12] = "parent.authID.text()"
        self.dbname      = "Employees" 
        # create a connection
        
        # create table
        sqlheader = """EmployeeID INTEGER PRIMARY KEY NOT NULL, Username VARCHAR(20) NOT NULL, Password INTEGER(8) NOT NULL,Firstname VARCHAR(40) NOT NULL,Lastname VARCHAR(40) NOT NULL,Gender VARCHAR(8),Department VARCHAR(40) NOT NULL,Job_Role VARCHAR(50) NOT NULL,Rank VARCHAR(40) NOT NULL,Phone_Number INTEGER(11) NOT NULL,Email VARCHAR(100) NOT NULL"""
        print(self.conn.tables)


    def dbCreateTable(self,sqlheader):
        self.query.exec(f"""CREATE TABLE {self.dbname} ({sqlheader})""")

    def dbUpdateTable(self,data):# data list to add to table
        columns = self.query.exec(f"""SELECT COLUMN_NAME FROM 
        INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {self.dbname} ORDER BY ORDINAL_POSITION""")
        self.query.exec(f"""INSERT INTO {self.dbname} ({columns})""")

    def dbLogin(self,user,pswd):
        print("Username: ",user," Password: ",pswd)
        if user=="" and pswd=="":
            dbMsg("Login Successful!")
            return True
        dbWarningMsg("Invalid Login Details!")
        return False 

    def dbVerifyAuthID(self,id,dept):
        # if id is valid:
        # use id to fetch the first name, last name, job_role, department, and rank of the authorized Id
        # if (department == new employee's department or Job_role == HR), and rank is > 8
            # id verified
        # else: return not valid
        # else return not valid
        return
    
    def dbVerifyLogin(self,user):
        # get line containing user: inline collect pswd,department,rank and jobrole
        # get pswd,and check if pswd rythmes
        # then store deparment,rank and jobrole. this would be used to set level of previledges before exit
        # return successful if successfull
        # else return unsuccessful
        return 





