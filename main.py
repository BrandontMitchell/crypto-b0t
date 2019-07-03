from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QRect
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


        self.createGraph()
        self.createMetrics()
        self.layout()
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()

    def layout(self):
        logo = QLabel("Crypto B0t")
        sign_in_btn = QPushButton("Sign In")
        sign_in_btn.setGeometry(QRect(0, 0, 50, 100))
        sign_up_btn = QPushButton("Sign Up")
        topLayout = QHBoxLayout()
        topLayout.addWidget(logo)
        topLayout.addWidget(sign_in_btn)
        topLayout.addWidget(sign_up_btn)

        main = QGridLayout()
        main.addLayout(topLayout, 0, 0, 1, 2)
        main.addWidget(self.graphBox, 1, 0)
        main.addWidget(self.metricsBox, 1, 1)
        self.setLayout(main)

    def createGraph(self):
        self.graphBox = QGroupBox("Graph")
        graph_label = QLabel("Graphs")
        graph_label.setGeometry(QRect(0, 0, 100, 700))
        middleLeft = QVBoxLayout()
        middleLeft.setContentsMargins(50, 50, 50, 50)
        middleLeft.addWidget(graph_label)
        middleLeft.addStretch(1)
        self.graphBox.setLayout(middleLeft)
        
    
    def createMetrics(self):
        self.metricsBox = QGroupBox("Metrics")

        transaction_log = QLabel("Transaction Log")
        transaction_log.setGeometry(QRect(0, 0, 400, 700))
        middleRight = QVBoxLayout()
        middleRight.addWidget(transaction_log)
        self.graphBox.setLayout(middleRight)

    def settings(self): 
        pass

    def footer(self):
        pass


    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bot = Main()
    sys.exit(app.exec_())