# This Python file uses the following encoding: utf-8
import sys,time
from PySide2.QtWidgets import QApplication
from Authenticate import __Auth__, __Start__
from resources.Themes import *



class __App__(QApplication):
    def __init__(self, arg__1):
        super().__init__(arg__1)
        self.setStyleSheet(theme2)
        self.setStyle("Fusion")
        
        #...
        self.__initUI__()

    def __initUI__(self): 
        self.login = __Auth__()
        self.start = __Start__()
    
    def run(self):
        time.sleep(1)
        self.login.show()



if __name__ == "__main__":
    app = __App__(sys.argv)
    app.run()
    sys.exit(app.exec_())
