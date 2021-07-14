import sqlite3 as lit, re, pandas as pd

class   SqLiteDB(object):
    def __init__(self, database='',table='',columns=()):
        self.dbname = database
        self.dbtable = table
        self.con = None

        if database!= '' or table != '' or columns != '':
            self.connect()
            self.createTable(table=table,columns=columns)
            self.printTable(table=table)
            self.disconnect()
    

    def connect(self):
        if self.dbname=='':
            print("Connect Error: No database found!")
            return False
        try:
            self.con = lit.connect(self.dbname)
            print("Successfully connected!")
            return True
        except lit.Error as e:
            print("Connect Error: {}".format(e.args[0]))
        return False


    def disconnect(self):
        if self.con != None:
            self.con.close()
        self.con = None


    def createTable(self, table='', columns=()):
        if self.dbname=='':
            print("Table Error: No database found!")
            return False
        
        if table == '':
            table = self.dbtable

        if self.con == None:
            self.connect()

        columns  = ",".join(w for w in columns)

        with self.con:
            try:
                cur = self.con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(table,columns))
                print('Successfully created {} table'.format(table))
                cur.close()
                return True
            except lit.Error as e:
                print("Table Error: {}".format(e.args[0]))
        self.disconnect()
        return False


    def tableInsert(self, table='', data=None):
        if self.dbname=='':
            print("Insert Error: No database found!")
            return False
        
        if table == '':
            table = self.dbtable

        if self.con == None:
            self.connect()

        # check data    
        data  = ",".join(self.validate(w) for w in data) 

        with self.con:
            try:
                cur = self.con.cursor()
                cur.execute("INSERT INTO {} VALUES ({})".format(table,data))
                print('Successfully inserted ({}) into {} table'.format(data,table))
                cur.close() 
                return True
            except lit.Error as e:
                print("Insert Error: {}".format(e.args[0])) 
        return False


    def printTable(self, table=''):
        if self.dbname=='':
            print("Print Error: No database found!")
            return False 

        temp = table
        if table=='' and self.dbtable == '':            
            print("Print Error: No table was specified!")
        else:
            temp = self.dbtable

        if self.con == None:
            self.connect()

        with self.con:
            cur = self.con.cursor()
            try: 
                cur.execute('SELECT * FROM {}'.format(temp))
                data = pd.DataFrame(cur.fetchall())
                print("Collected Table: \n{}".format(data))
                cur.close() 
                return data
            except lit.Error as e:
                print("Print Error: {}".format(e.args[0]))
        self.disconnect()


    def scrub(self, string=None,char1='',char2=''):
        return "".join(w for w in string if w.isalnum() or w == '_' or w=='-' or w==char1 or w==char2)


    def checkEmail(self, string=None):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        string = self.scrub(string,'@','.')           
        if(re.search(regex, string)):
            return string    
        return False


    def format(self, string=None):
        regex = re.compile('[@_!#$%=^&*()<>?\'\"/\|}{~:]') 

        if self.checkEmail(string) != False:
            return  string
        elif(regex.search(string) == None):
            return string
        else:
            return self.scrub(string)


    def validate(self, string=None):
        try:
            string = self.format(string)
            if string.isnumeric() and string != str(string):
                return str(string)
            elif string == "'{}'".format(self.scrub(string)):
                return string
            else:
                return "'{}'".format(string)
        except TypeError:
            print("Invalid type: {}".format(string)) 

 
    def login(self, table='', user='', paswd=''):
        result = '' 
        data = (self.scrub(user),self.scrub(paswd))
        
        if table == '':
            table = self.dbtable

        try:
            self.connect()
            with self.con:
                cur = self.con.cursor()
                cur.execute(f"SELECT firstname,lastname FROM {table} WHERE usersname=? AND password=?",data)
                row = cur.fetchone() 
                if row == None: result = 'Invalid'
                else: result = row[0]+' '+row[1]
                cur.close()
        except lit.Error as e:
            print("Error occurred accessing database Error:{}".format(e))  
        self.disconnect() 
        return result 


    def Error(self):
        return lit.Error