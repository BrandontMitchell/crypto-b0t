from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd 
import matplotlib.pyplot as pt
import datetime as datetime
import json


class PricePlotter():
    """
    Get current price, and historical data for specified coin. This class will plot that data
    """

    def __init__(self, coin):
        self.baseURL = 'https://api.coindesk.com/v1/bpi/historical/close.json?'
        # self.params = {
        #     'start': '1',
        #     'limit': '5000',
        #     'convert': 'USD'
        # }
        # self.headers = {
        #     'Accepts': 'application/json',
        #     'X-CMC_PRO_API_KEY': '4d75989f-6de0-49e3-aef2-5f2a2464c7a9'
        # }

        # self.key = '4d75989f-6de0-49e3-aef2-5f2a2464c7a9'
        self.get_data('btc')


    def get_historical_data(self, coin, start, end):
        self.session = Session()
        self.session.headers.update(self.headers)

        try:
            resp = self.session.get(self.baseURL, params=self.params)
            data = json.loads(resp.text)
            print(data)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == '__main__':
    plotter = PricePlotter('BTC')
