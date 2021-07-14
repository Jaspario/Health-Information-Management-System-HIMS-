import os, sys, time, random, PySide2, datetime#,uilib

imgdir  = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v3\\resources\\images"
icondir = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v3\\resources\\icons\\logo.ico"

def getLogo(object):
    pixmap = PySide2.QtGui.QPixmap(icondir)
    pixmap = pixmap.scaled(object.size())
    return pixmap

# style
forest = """           
            #bgLayer{
            background-color:rgb(170,170,170);
            color:rgb(0,0,0);
            border-radius: 7px;
            border: 2px solid #e2e2e2;}

            #bgframe {
            background-color:rgb(55,55,5);
            color:rgb(255,255,255);
            border-radius: 10px;
            border: 2px solid;}

            #bgfFrame{
            background-color:#929292;
            color:rgb(0,0,0);
            border-radius: 7px;
            border: 1px solid #e2e2e2;}

            #bgflbl{
            color: rgb(255,255,255);}

            #searchBtn{
            background-color: rgb(53, 0, 159);
            color:white;}

            #sendBtn{
            background-color: rgb(103, 103, 12);
            color: black;}

            #exitBtn{
            min-width: 80px;
            min-height: 20px;
            background-color:rgb(170,170,170);
            color: red;
            border-radius: 7px;
            border: 1px solid;}
            
            #exitBtn:hover {
            color: #ccc;
            background: red;}

            #miniBtn{
            min-width: 80px;
            min-height: 20px;
            background-color: rgb(170,170,170);
            color: rgb(0,0,0);
            border-radius: 7px;
            border: 1px solid;}

            #miniBtn:hover {
            color: white;
            background: #555555;}
            
            #bgframe QFrame, QPushButton{
            background-color:rgb(55,55,5);
            color:rgb(255,255,255);}

            #bgframe QPushButton:hover{
            color: white;
            background: #616109;}

            #table {
            color: rgb(0,0,0);
            background-color: rgb(255, 255, 255);}
        """

widget = """QPushButton{background:rgb(55,55,10);color:rgb(0,0,0);}
            QPushButton:hover{color: white;background: #616109;}"""


