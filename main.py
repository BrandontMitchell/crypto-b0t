from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
import sys

class Main(QWidget):
    
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title = 'Crypto B0t'
        self.x = 200
        self.y = 200
        self.width = 2100
        self.height = 1400

        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()

    def layout(self):
        header = QHBoxLayout()
        name = QLabel("crypto b0t")
        header.addWidget(name)
        header.addStretch(2)

        main = QGridLayout()

        self.setLayout(main)



    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bot = Main()
    sys.exit(app.exec_())