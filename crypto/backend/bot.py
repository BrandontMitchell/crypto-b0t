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
            print(key)
            print(secret)
            

        self.exchange_id = 'binance'
        self.exchange_class = getattr(ccxt, self.exchange_id)
        self.exchange = self.exchange_class({
                'apiKey': key,
                'secret': secret,
                'verbose': True
            })

        self.exchange.fetch_balance()    
        self.exchange.fetch_trades('USDC/BTC')

# print(exchange.load_markets)
# print(exchange.symbols)
# orders = exchange.fetch_order_book(exchange.symbols[0])
# print(f' orders -- {orders}')
# print(orders['bids'][0][0])
# print(binance.has['fetchTicker'])
# print(binance.fetch_ticker('BTC/USDC'))
# # print(binance.fetch_ticker('BTC/USDC')['weightedAvgPrice'])



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


#   FILTERS THE DATA MUST PASS BEFORE BUYING:
#       1. There is a negative to positive slope at time of buy
#       2. Buying will be below the previous sold price
#       3. Price will be below weekly average

#   FILTERS THE DATA MUST PASS BEFORE SELLING:
#       1. There is a positive to negative slope at time of sale
#       2. Price is above bought price (>1%)
#       3. Price will be above weekly average


    def boughtPrice(self):
        '''
        hold variable for initial buy price
        '''
        pass

    def weeklyAvg(self, coin):
        '''
        gathers market data, displays a dataframe including date, open, high, low, close, and volume.
        from this we gather the weekly price average (a filter for buying and selling)
        '''
        self.balance = self.exchange.fetch_balance()

        # iterate through tickers related to the coin and construct dataframe around data
        for ticker in self.exchange.fetch_tickers(coin):
            time.sleep(self.exchange.rateLimit / 1000)
            resp = self.exchange.fetch_ohlcv(ticker, '1d')
            df = pd.DataFrame(resp, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
            print(df)

            week_avg = df.tail(7)['close'].mean()
            print(week_avg)

        # for trade in exchange.fetch_trades('USDC/BTC', since=):
        #     if trade['side'] == 'buy':
        #         print(trade['price'])
        #         print(trade['amount'])

    def get_current_data(self, coin):
        '''
        gathers current data
        :type: coin --> string referencing specific crypto i.e. 'btc'
        :rtype: current_price --> int 
        :rtype: current_vol --> int
        :rtype: 
        '''

        # current_price = resp['USD']['rate']
        current_mcap = ''
        current_supp = ''

if __name__ == '__main__':
    bot = Bot()
    bot.weeklyAvg('BTC/USDC')
    print('done')