import ccxt
import time
import json
import pandas as pd

class Bot:

    def __init__(self):
        '''
        initialize setup, api auth, and exchange market
        '''
        with open("crypto.conf") as f:
            lines = f.readlines()
            key = lines[0].strip()
            secret = lines[1].strip()            

        self.exchange_id = 'binance'
        self.exchange_class = getattr(ccxt, self.exchange_id)
        self.exchange = self.exchange_class({
                'apiKey': key,
                'secret': secret,
                'verbose': True
            })

        self.exchange.fetch_balance()    
        self.exchange.fetch_trades('USDC/BTC')
        self.weekly_average('BTC/USDC')

    def purchase_price(self, price):
        '''
        hold variable for initial buy price
        '''
        return price 

    def weekly_average(self, coin):
        '''
        gathers market data, displays a dataframe including date, open, high, low, close, and volume.
        from this we gather the weekly price average (a filter for buying and selling)
        '''
        self.balance = self.exchange.fetch_balance()

        # iterate through tickers related to the coin and construct dataframe around data
        for ticker in self.exchange.fetch_tickers(coin):
            time.sleep(self.exchange.rateLimit / 1000)
            resp = self.exchange.fetch_ohlcv(ticker, '1m')
            df = pd.DataFrame(resp, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
            return df

    def get_current_data(self, data):
        '''
        gathers current data
        :type: coin --> string referencing specific crypto i.e. 'btc'
        :rtype: current_price --> int 
        :rtype: current_vol --> int
        :rtype: 
        '''
        try: 
            week_avg = data.tail(7)['close'].mean()
            current_price = float(str(data.tail(1)['close'])[7:15])
            current_vol = float(str(data.tail(1)['volume'])[7:14])
            return [current_price, current_vol, week_avg]
        except:
            return f'No data currently available' 

    def get_market_slope(self, data):
        '''
        gathers current market slope
        :type: data --> dataframe of most recent trades? (last 5 or so)
        :rtype: slope --> float (positive means U shape, negative means n shape)
        '''
        df = data[['close', 'date']]
        df = df.tail(360)
        print(df)

        # -60 iloc will result in an hour ago's price/date
        prev_price = df.iloc[-360]['close']
        prev_date = df.iloc[-360]['date']
        curr_price = df.iloc[-1]['close']
        curr_date = df.iloc[-1]['date']

        slope = ((curr_price-prev_price)/(curr_date-prev_date))

        return slope 


    def execute_purchase(self, coin, data, price):
        ''' checks all three filters, and makes a decision to hold or buy'''

        symbol = 'USDC/BTC'
        type = 'market'
        side = 'buy'
        amount = 0.001
        price = price 
        params = {
            'test': True
        }

        if self.get_market_slope(data) and (self.get_current_data(data) > self.weekly_average(coin)) and ((price + price*0.01) < self.purchase_price(price)):
            order = self.exchange.create_order(symbol, type, side, amount)
            print(order)    
        
        else:
            print(f'Filters failed, retry...') 