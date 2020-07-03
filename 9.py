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

        # ToolBar
        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'This is exit', self)
        extractAction.triggered.connect(self.close_application)
        # extractAction.triggered.connect(self.close_application()) 
        # the paranthesis would load the method in the memory and runs it immediately, thus the application closes itself again and again
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        # checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)
        
        self.show()

    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
    
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit!!', "Do you want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Exiting now")
            sys.exit()
        else:
            pass

def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()