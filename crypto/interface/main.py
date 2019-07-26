from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)

# from matplotlib.backends.qt_compat import QtCore, QtWidets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import sys, os
import requests
import matplotlib
import datetime
import time
import qtmodern.styles 
import qtmodern.windows
from crypto.interface.graph import PlotCanvas   # import from top level
from crypto.backend.bot import Bot                  # import from top level

# received top level package relative import error, to fix we must run from top level... i.e. ~/Desktop/cbot/crypto-b0t 
# and type: python3 -m crypto.interface.main

class Main(QWidget):
    '''
        This is the main class for the crypto bot. cd into the top level package, i.e. crypto-b0t, then run the rest as a python
        module: `python3 -m crypto.interface.main` for this module to run. 

        Upon initializing the main module, the ccxt api will be used with the binance exchange market. We used binance because it
        is most common in the U.S., and we already had an account there. The exchange can be changed, however data may load differently
        because of which data is selected and where. 

        The main application is running on PyQt5, with matplotlib for graphing, requests for the graphing api call, and ccxt for the 
        exchange data.

        Customizability includes how many days to graph, risk factor (how willing are you to take a risk that omits one of our three
        filters: 1. current price > 1% + weekly average 2. slope is positive, price buying at is lower than previous buy price)

        TODO:
            * Add an executing buying feature, should be done in the backend class
            * Clean up UI, make it prettier
            
    '''
    
    def __init__(self, parent=None):
        super().__init__()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.bot = Bot()
        self.initUI()


    def initUI(self):
        self.title = 'Crypto B0t'
        self.x = 200
        self.y = 200
        self.width = 2100
        self.height = 1400

        self.graph = PlotCanvas(self)
        self.layout()
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        
        
        self.show()

    def layout(self):
        
        self.createGraph()
        self.createMetrics(self.createData())
        self.createSettings()
        self.createFooter()

        logo = QLabel("Crypto B0t")
        sign_in_btn = QPushButton("Show graph") # press to graph bitcoin
        sign_in_btn.setGeometry(QRect(0, 0, 50, 50))
        sign_up_btn = QPushButton("Sign Up")
        topLayout = QHBoxLayout()
        topLayout.addWidget(logo)
        topLayout.addWidget(sign_in_btn)
        topLayout.addWidget(sign_up_btn)

        main = QGridLayout()
        main.addLayout(topLayout, 0, 0, 1, 2)
        main.addWidget(self.graphBox, 1, 0)
        main.addWidget(self.metricsBox, 1, 1)
        main.addWidget(self.settingsBox, 2, 0)
        main.addWidget(self.footerBox, 2, 1)
        main.setColumnStretch(0, 6)
        main.setColumnStretch(1, 4)
        main.setRowStretch(1, 8)
        main.setRowStretch(2, 2)
        self.setLayout(main)

    def createGraph(self):
        self.graphBox = QGroupBox("Graph")
        middleLeft = QVBoxLayout()
        middleLeft.addWidget(self.graph)
        self.graphBox.setLayout(middleLeft)
        
    
    def createMetrics(self, data):
        self.metricsBox = QGroupBox("Metrics")
        middleRight = QVBoxLayout()

        # gather current market data
        self.coin_lb = QLabel("Coin Chosen: BTC/USDC")
        self.current_price = QLabel("Current Price: " + str(self.data_arr[0]))
        self.current_vol = QLabel("Current Volume: " + str(self.data_arr[1]))
        self.last_trade = QLabel("Weekly Average: " + str(self.data_arr[2]))
        self.last_trade_share = QLabel("Current Slope: " + str(data[3]))

        # gather user values (some won't be necessary)
        self.time_label = QLabel("Enter # of days to graph: ")
        self.time_box = QLineEdit(self)
        self.coin_selling_lb = QLabel("Enter the coin to sell: ")
        self.coin_selling = QLineEdit(self)
        self.coin_buying_lb = QLabel("Enter the coin to buy: ")
        self.coin_buying = QLineEdit(self)
        self.lowest_price_lb = QLabel("Enter lowest price to sell at: ")
        self.lowest_price = QLineEdit(self)
        self.highest_price_lb = QLabel("Enter highest price to sell at: ")
        self.highest_price = QLineEdit(self)
        self.risk = QSlider(Qt.Horizontal)
        # self.risk.setValue(self.risk.value())
        self.risk_lb = QLabel("Enter risk factor: ")
        self.risk.setFocusPolicy(Qt.StrongFocus)
        self.risk.setTickPosition(QSlider.TicksBothSides)
        self.risk.setTickInterval(10)
        self.risk.setSingleStep(1)
        self.submit = QPushButton("Submit Values")

        # self.time_val = self.time_box.text()
        # self.coin_selling_val = self.coin_selling.text()
        # self.coin_buying_val = self.coin_buying.text()
        # self.lowest_price_val = self.lowest_price.text()
        # self.highest_price_val = self.highest_price.text()
        # self.risk_val = self.risk.valueChanged()

        # data = [self.time_val, self.coin_selling_val, self.coin_buying_val, self.lowest_price_val, \
        #         self.highest_price_val] # self.risk_val

        

        self.submit.clicked.connect(self.updateSettings)

        # add labels and buttons to right middle box
        middleRight.addWidget(self.current_price)
        middleRight.addWidget(self.current_vol)
        middleRight.addWidget(self.last_trade)
        middleRight.addWidget(self.last_trade_share)
        middleRight.addWidget(self.time_label)
        middleRight.addWidget(self.time_box)
        middleRight.addWidget(self.coin_selling_lb)
        middleRight.addWidget(self.coin_selling)
        middleRight.addWidget(self.coin_buying_lb)
        middleRight.addWidget(self.coin_buying)
        middleRight.addWidget(self.lowest_price_lb)
        middleRight.addWidget(self.lowest_price)
        middleRight.addWidget(self.highest_price_lb)
        middleRight.addWidget(self.highest_price)
        middleRight.addWidget(self.risk_lb)
        middleRight.addWidget(self.risk)
        middleRight.addWidget(self.submit)

        # set layout to add the middle right box and stylesheet
        self.metricStyleSheet()
        self.metricsBox.setLayout(middleRight)

    def createSettings(self): 
        self.settingsBox = QGroupBox("Settings")
        lowerMiddle = QHBoxLayout()

        # initiate setting labels
        self.time_set = QLabel("# of days graphed: ")
        self.coin_sell_set = QLabel("Coin selling: ")
        self.coin_buy_set = QLabel("Coin buying: ")
        self.lowest_set = QLabel("Lowest price to sell: ")
        self.highest_set = QLabel("Highest price to sell: ")

        # try:
        #     self.risk_set = QLabel("Risk factor: " + str(data[5]))
        #     lowerMiddle.addWidget(self.risk_set)
        # except:
        #     pass
        
        # add to horizontal box layout
        lowerMiddle.addWidget(self.time_set)
        lowerMiddle.addWidget(self.coin_sell_set)
        lowerMiddle.addWidget(self.coin_buy_set)
        lowerMiddle.addWidget(self.lowest_set)
        lowerMiddle.addWidget(self.highest_set)
        
        self.settingsBox.setLayout(lowerMiddle)

    def updateSettings(self):

        # grab text after input and update those setting labels
        data = [self.time_box.text(), self.coin_selling.text(), self.coin_buying.text(), self.lowest_price.text(), self.highest_price.text()]
        self.time_set.setText("# of days graphed: " + str(data[0]))
        self.coin_sell_set.setText("Coin selling: " + str(data[1]))
        self.coin_buy_set.setText("Coin buying: " + str(data[2]))
        self.lowest_set.setText("Lowest price to sell: " + str(data[3]))
        self.highest_set.setText("Highest price to sell: " + str(data[4]))


    def createFooter(self):
        self.footerBox = QGroupBox("Footer")
        lower = QVBoxLayout()
        
        # create some lower right labels and buttons to initiate buying/selling
        footer_label = QLabel("@htb 2019")
        buy_label = QLabel("Press to initiate buying")
        buy_btn = QPushButton("Buy")
        sell_label = QLabel("Press to initiate selling")
        sell_btn = QPushButton("Sell")

        # add to layout
        lower.addWidget(footer_label)
        lower.addWidget(buy_label)
        lower.addWidget(buy_btn)
        lower.addWidget(sell_label)
        lower.addWidget(sell_btn)
        self.footerBox.setLayout(lower)


    def createData(self):
        
        data = self.bot.weekly_average('BTC/USDC')
        self.price = self.bot.get_current_data(data)[0]
        self.vol = self.bot.get_current_data(data)[1]
        self.week_avg = self.bot.get_current_data(data)[2]
        self.slope = self.bot.get_market_slope(data)

        self.data_arr = [self.price, self.vol, self.week_avg, self.slope]
        return self.data_arr


    def metricStyleSheet(self):
        try:
                
            if self.data_arr[3] > 0:
                self.last_trade_share.setStyleSheet('color: green')
            else:
                self.last_trade_share.setStyleSheet('color: red')
            
            if self.data_arr[0] > (self.data_arr[2] + self.data_arr[2] * 0.01):
                self.current_price.setStyleSheet('color: green')
            else:
                self.current_price.setStyleSheet('color: red')
        except TypeError as e:
            print(e)
            pass


    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # bot = Main()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(Main())
    mw.show()
    sys.exit(app.exec_())