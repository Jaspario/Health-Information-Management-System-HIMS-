from Importlib import*
from interface.UiStart import Ui_Start
from Login import Auth
from resources.database import SqLiteDB

class __Start__(PySide2.QtWidgets.QDialog,Ui_Start):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowFlags(PySide2.QtCore.Qt.WindowStaysOnTopHint|PySide2.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
        pixmap = getLogo(self.logo)
        self.logo.setPixmap(pixmap)
        self.show()
class   App(PySide2.QtWidgets.QApplication):
    def __init__(self, arg__1):
        super().__init__(arg__1)
        self.setStyleSheet(forest)
        self.setStyle("Fusion")    
        
        self.database = SqLiteDB(database="Sefa.db")
        self.login = Auth(parent=self,database=self.database)
        self.start = __Start__()
    
    def run(self):
        self.start.hide()
        self.login.show()
