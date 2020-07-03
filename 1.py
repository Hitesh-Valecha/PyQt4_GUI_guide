import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(10, 10, 500, 300)
window.setWindowTitle("First GUI")

window.show()