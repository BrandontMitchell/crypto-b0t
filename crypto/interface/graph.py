from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd 
import requests
import collections
import matplotlib.pyplot as pt
import datetime
import json


class PricePlotter():
    """
    Get current price, and historical data for specified coin. This class will plot that data
    """

    def __init__(self, coin):
        self.baseURL = 'https://api.coindesk.com/v1/bpi/'
        self.today = datetime.date.today()
        self.historical_date = datetime.date.today()-datetime.timedelta(days=200)
        self.coin = 'btc'
        self.get_historical_data(self.coin, self.historical_date, self.today)


    def get_historical_data(self, coin, start, end):
        '''
        gathers historical data with given currency, start, end
        '''
        start = f'{start.year:#02d}-{start.month:#02}-{start.day:#02}'
        end = f'{end.year:#02}-{end.month:#02d}-{end.day:#02d}'
        url = f'{self.baseURL}historical/close.json?currency={coin}&start={start}&end={end}'
        print(url)
        r = requests.get(url).json()['bpi']


        print(r)
        prices = r.values()
        dates = r.keys()
        print(prices)
        print(dates)
        # print(data_dict)
        


if __name__ == '__main__':
    plotter = PricePlotter('BTC')
