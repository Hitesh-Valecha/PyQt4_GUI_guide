import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Self declared Window not widget")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
"""init method is the initial method that runs whenever we make Window object
    The init method is permanent and is always there, other functions may remain
    for a particular window/frame"""
sys.exit(app.exec_())