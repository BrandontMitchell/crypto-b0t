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

    def boughtPrice(self):
        '''
        hold variable for initial buy price
        '''
        pass

    def pullPrice(self, symbol):
        '''
        gathers BTC price for last _____ (interval of time)
        '''
        self.balance = self.exchange.fetch_balance()

        for ticker in self.exchange.fetch_tickers(symbol):
            time.sleep(self.exchange.rateLimit / 1000)
            resp = self.exchange.fetch_ohlcv(ticker, '1d')
            # print(resp)
            
            df = pd.DataFrame(resp, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
            print(df)

        # for trade in exchange.fetch_trades('USDC/BTC', since=):
        #     if trade['side'] == 'buy':
        #         print(trade['price'])
        #         print(trade['amount'])

if __name__ == '__main__':
    bot = Bot()
    bot.pullPrice('BTC/USDC')
    print('done')