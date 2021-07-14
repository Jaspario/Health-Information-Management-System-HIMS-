import os,sys, PySide2, Sefa



if __name__ == "__main__": 
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    if hasattr(PySide2.QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PySide2.QtWidgets.QApplication.setAttribute(PySide2.QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = Sefa.App(sys.argv)
    timer = PySide2.QtCore.QTimer()
    timer.singleShot(2*2000,app.run)
    sys.exit(app.exec_())
    app.quit()
    del app

#PySide2.QtWidgets.QStyle.alignedRect(PySide2.QtCore.Qt.LayoutDirection, PySide2.QtCore.Qt.Alignment, PySide2.QtCore.QSize, PySide2.QtCore.QRect)  
#QWindowsWindow::setGeometry: Unable to set geometry 1104x720+399+110 (frame: 1104x720+399+110) on QWidgetWindow/"RegisterWindow" on "\\.\DISPLAY1". Resulting geometry: 1104x810+399+110 (frame: 1104x810+399+110) margins: 0, 0, 0, 0 minimum size: 1104x720 maximum size: 1104x720 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1104,720 maxtrack=1104,720)

