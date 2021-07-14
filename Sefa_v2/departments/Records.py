from importLib import *

class Records():
    def __init__(self,parent=None):
        super().__init__()
        self.table    = parent.table
        self.status   = "Unsigned"
        self.viewObj  = None
        self.items    = [] 
        self.index    = parent.rowCount
        self.button   = QPushButton("Create")
        self.addButton()

    def setTable(self):
        columns = self.table.columnCount()-1
        for i in range(0,columns): 
            item = QTableWidgetItem(self.items[i])
            self.table.setItem(self.index,i,item) 

    def viewObject(self,vobject):
        self.viewObj  =vobject

    def addButton(self):
        self.button.setFlat(True)
        self.button.setCursor(Qt.PointingHandCursor)
        i = self.table.columnCount()
        self.button.clicked.connect(self.OnClickButton)
        self.table.setCellWidget(self.index,i-1,self.button)

    def UpdateTable(self):
        text = self.GetButtonText()
        self.button.setText(text)
        self.setTable()

    def OnView(self):
        self.viewObj.show()

    def OnCreate(self):
        self.viewObj.show()  
        print("A new record for patient 0000000000 has been created!")

    def GetButtonText(self):
        res = "Create"
        if self.status == "Signed":
            res = "View" 
        return res 
    
    def OnClickButton(self):
        if self.button.text() == "Create":
            self.OnCreate()
        elif self.button.text() == "View":
            self.OnView()

    
