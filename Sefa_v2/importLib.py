import os, sys, random, time, datetime, UiLib
from PySide2.QtWidgets import (QMainWindow,QWidget,QDialog,QTableWidgetItem,QPushButton,QMessageBox,QLineEdit,QStyle)
from PySide2.QtCore import Qt, QSize, QTimer,QPoint
from PySide2.QtGui import QImage, QPixmap, QIcon, QCursor, QScreen

imgdir  = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\Sefa_v2\\resources\\images"
icondir = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\Sefa_v2\\resources\\icons\\logo.ico"

def getLogo(object):
    pixmap = QPixmap(icondir)
    pixmap = pixmap.scaled(object.size())
    return pixmap
