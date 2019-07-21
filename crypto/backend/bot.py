import ccxt
import time
import json
import pandas as pd

# TODO:
#   FILTERS THE DATA MUST PASS BEFORE BUYING:
#       1. There is a negative to positive slope at time of buy
#       2. Buying will be below the previous sold price
#       3. Price will be below weekly average       !!!! Nearly Done !!!!

#   FILTERS THE DATA MUST PASS BEFORE SELLING:
#       1. There is a positive to negative slope at time of sale
#       2. Price is above bought price (>1%)
#       3. Price will be above weekly average       !!!! Nearly Done !!!!

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

            week_avg = df.tail(7)['close'].mean()
            self.get_current_data(df)
            self.get_market_slope(df)

        # for trade in exchange.fetch_trades('USDC/BTC', since=):
        #     if trade['side'] == 'buy':
        #         print(trade['price'])
        #         print(trade['amount'])

    def get_current_data(self, data):
        '''
        gathers current data
        :type: coin --> string referencing specific crypto i.e. 'btc'
        :rtype: current_price --> int 
        :rtype: current_vol --> int
        :rtype: 
        '''
        try: 

            current_price = float(str(data.tail(1)['close'])[7:15])
            current_vol = float(str(data.tail(1)['volume'])[7:14])
            current_supp = ''
            print(data.tail(1)['close'])
            print(f'Current Price: {current_price}')
            print(f'Current Volumne: {current_vol}')
        except:
            pass 
    def get_market_slope(self, data):
        '''
        gathers current market slope
        :type: data --> dataframe of most recent trades? (last 5 or so)
        :rtype: slope --> float (positive means U shape, negative means n shape)
        '''
        df = data[['close', 'date']]
        df = df.tail(2)

        prev_price = df.iloc[-2][6:13]
        # curr_price = df.iloc[[-1],['close']][6:13]

        print(prev_price)

        print(df)



# EXAMPLE ON MARKET ORDER

# symbol = 'XRP/BTC'
# type = 'market'
# side = 'sell'
# amount = 50
# price = 0.40 
# params = {
#     'test': True
# }

# order = exchange.create_order(symbol, type, side, amount)
# print(order)



if __name__ == '__main__':
    bot = Bot()
    bot.weekly_average('BTC/USDC')