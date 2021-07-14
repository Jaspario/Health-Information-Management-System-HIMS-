# This Python file uses the following encoding: utf-8 
from Departments._imports_ import*
from Authenticate import __Auth__,__Start__



class __Sefa__(QApplication):

    def __init__(self):
        super().__init__() 
        self.setStyleSheet(style2)
        self.setStyle("Fusion")
        #...
        self.__initUI__()


    def __initUI__(self): 
        self.login = __Auth__()
        self.start = __Start__(self.login)


    def run(self):  
        pass











if __name__ == "__main__":
    sefa = __Sefa__()
    sefa.run()
    sys.exit(sefa.exec_())