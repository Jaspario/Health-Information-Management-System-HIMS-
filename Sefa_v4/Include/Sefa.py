from Lib.importlib import *
from Include.database import SqLiteDB
from Include.Authenticate import Login
from Include.interface.UiStart import Ui_Start

class _Start_(QtWidgets.QDialog,Ui_Start):
    def __init__(self, parent = None):
        super().__init__(parent = None)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        
        self.logo.setScaledContents(True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self.show()




class App(QtWidgets.QApplication):
    def __init__(self, arg__1):
        super().__init__(arg__1)
        self.setStyleSheet(forest)
        self.setStyle("Fusion")    
        
        self.database = SqLiteDB(database="Sefa.db")
        self.login = Login(parent=self,database=self.database)
        self.start = _Start_()
    
    def run(self):
        self.start.hide()
        self.login.show()
