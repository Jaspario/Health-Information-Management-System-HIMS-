from importLib import *
from interface.UiLabRecord import Ui_LabRecord
from interface.UiLabReport import Ui_LabReport
from departments.Records import Records

class Lab(QDialog,Ui_LabRecord):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.Load()
        self.__initUI__()
        self.rowCount=0
        self.records=[]
        self.addLogo()
        self.signalSlot()
    
    def __initUI__(self,parent=None):
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(icondir))
    
    def signalSlot(self):
        self.exitBtn.clicked.connect(self.onClose)
        self.miniBtn.clicked.connect(self.mini)  
        self.closeBtn.clicked.connect(self.onClose)
        self.addNewBtn.clicked.connect(self.OnClickAddNew)

    def addLogo(self): 
        self.logo.setFixedSize(QSize(40,45)) 
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)

    def mini(self):
        self.showMinimized()
    
    def onClose(self):
        self.Save()
        self.hide()
        self.parent.show()

    def OnClickAddNew(self): 
        pass
        if self.rowCount>0: 
            d = self.rowCount-1  
            status = self.records[d].status
            print("Item gotten: ",status, " row = ",d)
            if status == "Unsigned":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Sefa (HIMS) - Warning!")
                msg.setText("An unsigned record was created! Sign record to continue.")
                msg.exec_()
                return 
            else:
                self.AddNew()
        else:
            self.AddNew()
    
    def AddNew(self):
        pass
        self.table.setRowCount(self.rowCount+1)
        record = Records(self)
        review = RequestNote(self,record)
        record.viewObject(review)
        self.records.append(record) 
        self.rowCount = self.rowCount+1
    
    def Load(self):
        pass

    def Save(self):
        pass


class RequestNote(QWidget):
    def __init__(self, parent=None, f=None):
        super().__init__(parent=None)
        pass
