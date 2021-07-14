import sqlite3 as lit, re, pandas as pd


class   SqLiteDB(object):
    def __init__(self, database='',table='',columns=''):
        self.dbname = database
        self.dbtable = table
        self.con = None

        if database!= '' and table != '' and columns != '':
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
            return True
        except self.error as e:
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
                cur.close()
                return True
            except self.error as e:
                print("Table Error: {}".format(e.args[0]))
        self.disconnect()
        return False


    def tableInsert(self, table='', data=None):
        if self.dbname=='':
            print("Insert Error: No database found!")
            return False
        
        if table == '':
            print('Insert Error: No table inputed!')

        if self.con == None:
            self.connect()
        # check data    
        data  = ",".join(self.validate(w) for w in data) 
    
        with self.con:
            try:
                cur = self.con.cursor()
                cur.execute("INSERT INTO {} VALUES ({})".format(table,data))
                #print('Successfully inserted ({}) into {} table'.format(data,table))
                cur.close() 
                return True
            except self.error as e:
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
                #print("Collected Table: \n{}".format(data))
                cur.close() 
                return data
            except self.error as e:
                print("Print Error: {}".format(e.args[0]))
        self.disconnect()


    def scrub(self, string=None,char1='',char2=''):
        s = "".join(w for w in string if w.isalnum() or w =='_' or w==' ' or w =='-' or w==',' or w==':'or w ==char1 or w ==char2)
        return s


    def format(self, string=None):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' 

        s = string.split('@',1)
        if len(s)==2:
            try:
                s1 = self.scrub(s[0])
                s2 = self.scrub(s[1],'.')
                string = s1+'@'+s2
            except IndexError:
                return string,False

        if(re.search(regex, string)):
            return string,True  
        
        regex = re.compile('[@_!#$%=^&*()<>?\'\"/\|}{~:]') 
        
        if(regex.search(string) == None):
            return string,True
        else:
            return self.scrub(string),True

        return string,False


    def validate(self, string=None):
        result = ''
        if type(string) == int:
            string = str(string)
        try: 
            string,re = self.format(string)
            if string.isnumeric() and string != str(string):
                result = str(string)
            elif string == "'{}'".format(string.strip('\'')):
                result = string
            else:
                result = "'{}'".format(string)
        except TypeError:
            print("Invalid type: {}".format(string)) 
        return result

 
    def login(self, table='', user='', paswd=''):
        result = None 
        msg =''
        data = (self.scrub(user),self.scrub(paswd))
        
        if table == '':
            print('Insert Error: No table inputed!')

        try:
            self.connect()
            with self.con:
                cur = self.con.cursor()
                cur.execute(f"SELECT firstname,lastname,jobtitle,department,rank,employeeID FROM {table} WHERE usersname=? AND password=?",data)
                result = cur.fetchone() 
                if result == None: msg = 'Invalid'
                else: msg = result[0]+' '+result[1]
                cur.close()
        except self.error as e:
            print("Error occurred accessing database Error:{}".format(e))  
        self.disconnect() 
        return result,msg 


    def error(self):
        return self.error


    def getRow(self,table='',field='',key=''):
        data = None 
        if table=='' or field=='' or key == '':
            print('getRow Error: No table or parameters!')
            return 
        print("'table='{}', field='{}', key='{}'".format(table,field,key))
        #...
        try:
            self.connect()
            with self.con:
                cur = self.con.cursor()
                cur.execute(f"SELECT {self.scrub(field,char1=',')} FROM {table} WHERE {self.scrub(key,char1='=')}")
                data = cur.fetchone()  
                cur.close()
            self.disconnect()
        except self.error() as e:
            print("Error occurred accessing database Error:{}".format(e))   
        return data

    
    def getRows(self,table='',field='',keys=''):
        data = None
        if table=='' or field=='' or keys == '':
            print('getRows Error: No table or parameters!')
            return data,''
        msg  = '' 
        #...
        try:
            self.connect()
            with self.con:
                cur = self.con.cursor()
                if type(keys) == tuple:
                    cur.execute(f"SELECT * FROM {table} WHERE {field}",(self.scrub(keys[0]),self.scrub(keys[1])))
                elif type(keys) == str:
                     cur.execute(f"SELECT * FROM {table} WHERE {field}={self.scrub(keys)}") 
                data = cur.fetchall() 
                if data == None:
                    msg = "FALSE"
                if len(data)>0: 
                    msg = 'TRUE'
                cur.close()
            self.disconnect()
        except self.error() as e:
            print("Error occurred accessing database Error:{}".format(e))   
        return data,msg