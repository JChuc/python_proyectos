import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window=QtGui.QWidget()
window.setWindowTitle("Hola Mundo")
window.show()
sys.exit(app.exec_())
