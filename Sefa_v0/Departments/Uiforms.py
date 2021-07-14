# This Python file uses the following encoding: utf-8
import os, sys

class UI:
    def __init__(self, folder):
        self.folder = folder+"\\_ui"
        self.outPath = folder+"\\_py"

    def getModules(self):
        for files in os.listdir(self.folder): 
            if files.endswith('.ui'):
                # store input and output files
                inputFile  = os.path.join(self.folder,files)
                outputFile = self.outPath+"\\Ui_"+files.split('.')[0]+".py"
               
                self.remove(outputFile) #if it exists already
                  
                # create new output file, return false if failed
                CMD = "pyside2-uic " + inputFile +" -o " + outputFile
                if os.system(CMD)!=0:
                    print("Failed to get Modules, CMD: ",CMD)
                    return False

        # .ui modules successfully converted to .py
        return True
    
    def remove(self, file):
        if os.path.isdir(file):
            os.remove(file)
            print("Directory Cleared!")
    

