from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from itertools import chain
import requests
import datetime
import json

# https://www.coindesk.com/api
# https://github.com/L1Cafe/Coindesk-Python-API-client/blob/master/coindesk/client.py

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,\
                                   QSizePolicy.Expanding,\
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.bitcoinTrack('btc', 50)

    def bitcoinTrack(self, coin, time):
        '''
            live bitcoin tracking
        '''
        self.baseURL = 'https://api.coindesk.com/v1/bpi/'
        self.today = datetime.date.today()
        self.historical_date = datetime.date.today()-datetime.timedelta(days=time)
        self.coin = 'btc'
        self.get_historical_data(self.coin, self.historical_date, self.today) 
    
    def get_historical_data(self, coin, start, end):
        '''
        gathers historical data with given currency, start, end
        '''
        start = f'{start.year:#02d}-{start.month:#02}-{start.day:#02}'
        end = f'{end.year:#02}-{end.month:#02d}-{end.day:#02d}'
        url = f'{self.baseURL}historical/close.json?currency={coin}&start={start}&end={end}'
        r = requests.get(url).json()['bpi']

        dates = [x for x in chain(r) if x]
        print(dates)
        prices = [x for x in chain(r.values()) if x]
        print(prices)

        price_max = max(prices)
        date_pos = prices.index(price_max)
        date_max = dates[date_pos]

        price_min = min(prices)
        date_min = prices.index(price_min)

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        lists = sorted(r.items())
        x, y = zip(*lists)

        line, = ax.plot(x, y)
        ax.plot(x,y, 'tab:blue')
        ax.set_title('BTC Tracker')
        ax.annotate(f'local high of {price_max} on {date_max}', xy=(date_max, price_max), xytext=(date_max, price_max+5000),
                    arrowprops=dict(facecolor='green', shrink=0.05),
                    )
        ax.set_ylim(0, 20_000)
        self.draw()