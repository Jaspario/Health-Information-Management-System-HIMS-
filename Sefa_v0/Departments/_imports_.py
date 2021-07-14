import os, sys, random,datetime

from Departments.Uiforms import UI
from PySide2.QtWidgets import (QApplication,QWidget,QMainWindow,QDialog,QTableWidgetItem,QPushButton,QMessageBox,QLineEdit,QStyle)
from PySide2.QtCore import Qt, QSize, QTimer,QPoint
from PySide2.QtGui import QImage, QPixmap, QRegion,QPolygon


folder = sys.path[0]+"\\Departments\\resources\\interface"
logoPath = sys.path[0]+"\\Departments\\resources\\logos\\Sefa Logo3.png" 
ui = UI(folder)
if not ui.getModules():
    sys.exit()

def mssgBox(wnd,text):
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle(wnd.windowTitle())
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    btn = msg.exec_()
    if btn == QMessageBox.Yes:
        wnd.close()
        return True 
    else:
        msg.close()
    return False

def errorMsg(msg):
    msgBox = QMessageBox() 
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Database - Error!")
    retcode = msgBox.exec_()
    sys.exit(1) # exit with failure

def dbMsg(msg):
    msgBox = QMessageBox() 
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Database-Info")
    retcode = msgBox.exec_()
    return msg

def dbWarningMsg(msg): 
    msgBox = QMessageBox() 
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Database-Warning")
    msgBox.setStandardButtons(QMessageBox.Retry|QMessageBox.No)
    retcode = msgBox.exec_()
    if retcode == QMessageBox.No:
        sys.exit()
    else:
        msgBox.close()

def getLogo(object):
    pixmap = QPixmap(logoPath)
    pixmap = pixmap.scaled(object.size())
    return pixmap


style1 = """QDialog{background-color:rgb(170,170,170);color:rgb(0,0,0);}
            QFrame#picFrame,QFrame#picFrame QFrame,QFrame#loginFrame,QFrame#loginFrame QFrame,
            QPushButton
            {background-color:rgb(55,55,5);color:rgb(255,255,255);}  
            QPushButton#exitBtn{background-color:rgb(170,170,170);color:rgb(255,0,0);}
            QPushButton#minBtn{background-color:rgb(170,170,170);color:rgb(0,0,0)}"""

style2 = """QDialog{background-color:rgb(170,170,170);color:rgb(0,0,0);}
           QPushButton#exitBtn{background-color:rgb(170,170,170);color:rgb(255,0,0);}
           QPushButton#minBtn{background-color:rgb(170,170,170);color:rgb(0,0,0)}
           QFrame#bgLayer{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QFrame#rbgLayer{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QFrame#rbgLayer QWidget{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QFrame#bgLayer QFrame,QPushButton{background-color:rgb(55,55,5);color:rgb(255,255,255);}"""

style3 = """QDialog{background-color:rgb(170,170,170);color:rgb(0,0,0);}
           QPushButton#exitBtn{background-color:rgb(170,170,170);color:rgb(255,0,0);}
           QPushButton#minBtn{background-color:rgb(170,170,170);color:rgb(0,0,0)}
           QFrame#bgLayer{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QFrame#bgLayer QFrame,QPushButton{background-color:rgb(55,55,5);color:rgb(255,255,255);}"""


style4 = """QDialog{background-color:rgb(170,170,170);color:rgb(0,0,0);}
           QFrame#bgLayer{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QFrame#bgLayer QFrame,QPushButton{background-color:rgb(55,55,5);color:rgb(255,255,255);}
           QPushButton#exitBtn{color:rgb(255,0,0);}
           QPushButton#minBtn{color:rgb(0,0,0)}""" 