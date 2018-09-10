import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bnt = QPushButton("B1")
    bnt.clicked.connect(QCoreApplication.instance().quit)
    bnt.resize(400, 100)
    bnt.move(50, 50)
    bnt.show()
    sys.exit(app.exec_())
