import pandas as pd 
import requests
import matplotlib.pyplot as plt
import datetime
import json

# https://www.coindesk.com/api
# https://github.com/L1Cafe/Coindesk-Python-API-client/blob/master/coindesk/client.py

class PricePlotter():
    """
    Get current price, and historical data for specified coin. This class will plot that data
    """

    def __init__(self, coin, time):
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

        prices = r.values()
        dates = r.keys()
        print(prices)
        print(dates)

        

        lists = sorted(r.items())
        x, y = zip(*lists)

        plt.ylabel('Price (USD)')
        plt.xlabel('Time')
        plt.title(f'{coin} price timeline')
        plt.show() 
        


if __name__ == '__main__':
    plotter = PricePlotter('BTC', 50)
