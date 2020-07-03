import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Window")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        # MenuBar
        extractAction  = QtGui.QAction("&You can Close", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())      # more preferable auto adjusting
        # btn.resize(btn.minimumSizeHint())
        btn.move(0,100)   #position
        
        self.show()
    
    def close_application(self):
        print("Customized")
        sys.exit()

def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()