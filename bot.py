import ccxt
import time
import json

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': '7o6rbHZbD2uJcZC3XIGyZHUjxStCdByNUufe52r2gv2zgr3lr8fHeBibyD5Cr3UW',
    'secret': 'ISqKlDLESnNbmdHT5nVpYjtdF3yHcN7LaXSbJQvma0FUD1bY5Yz12biR6LBQeD3M',
    'verbose': True
})

print("23452345;l234jk5;l234j5;lkj345;lk")
print(exchange.fetch_balance())
print("23452345;l234jk5;l234j5;lkj345;lk")
print(exchange.load_markets)
print(exchange.symbols)
orders = exchange.fetch_order_book(exchange.symbols[0])
# print(f' orders -- {orders}')
# print(orders['bids'][0][0])
# print(binance.has['fetchTicker'])
# print(binance.fetch_ticker('BTC/USDC'))
# # print(binance.fetch_ticker('BTC/USDC')['weightedAvgPrice'])


# high = binance.fetch_ticker('BTC/USDC')['high']
# print((int(high) + int(low))/2)

# print(binance.fetch_ticker('BTC/USDC')['info']['weightAvgPrice'])
# for symbol in binance.symbols:
#     if symbol == 'BTC/BNB':
#         print("found")


symbol = 'XRP/BTC'
type = 'market'
side = 'sell'
amount = 50
price = 0.40 
params = {
    'test': True
}

order = exchange.create_order(symbol, type, side, amount)
print(order)

def boughtPrice():
    '''
    hold variable for initial buy price
    '''
    pass