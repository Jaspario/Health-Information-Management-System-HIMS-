from Lib.importlib import *
from Include.Sefa import App



if __name__ == "__main__": 
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = App(sys.argv)
    timer = QtCore.QTimer()
    timer.singleShot(2*2000,app.run)
    sys.exit(app.exec_()) 