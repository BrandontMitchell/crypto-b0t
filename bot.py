import ccxt
#
# hitbtc   = ccxt.hitbtc({'verbose': True})
# bitmex   = ccxt.bitmex()
# huobipro = ccxt.huobipro()
# binance     = ccxt.binance({
#     'apiKey': '7o6rbHZbD2uJcZC3XIGyZHUjxStCdByNUufe52r2gv2zgr3lr8fHeBibyD5Cr3UW',
#     'secret': 'ISqKlDLESnNbmdHT5nVpYjtdF3yHcN7LaXSbJQvma0FUD1bY5Yz12biR6LBQeD3M',
# })
# kraken = ccxt.kraken({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })

# exchange_id = 'binance'
# exchange_class = getattr(ccxt, exchange_id)
# exchange = exchange_class({
#     'apiKey': '7o6rbHZbD2uJcZC3XIGyZHUjxStCdByNUufe52r2gv2zgr3lr8fHeBibyD5Cr3UW',
#     'secret': 'ISqKlDLESnNbmdHT5nVpYjtdF3yHcN7LaXSbJQvma0FUD1bY5Yz12biR6LBQeD3M',
#     'timeout': 30000,
#     'enableRateLimit': True,
# })
MIN_AMOUNT ={}
MIN_ORDERS = {}

binance = ccxt.binance({
    'apiKey': '7o6rbHZbD2uJcZC3XIGyZHUjxStCdByNUufe52r2gv2zgr3lr8fHeBibyD5Cr3UW',
    'secret': 'ISqKlDLESnNbmdHT5nVpYjtdF3yHcN7LaXSbJQvma0FUD1bY5Yz12biR6LBQeD3M',
})

print(binance.fetch_balance())

# print(ccxt.exchanges)
#
# hitbtc_markets = hitbtc.load_markets()
#
# print(hitbtc.id, hitbtc_markets)
# print(bitmex.id, bitmex.load_markets())
# print(huobipro.id, huobipro.load_markets())
#
# print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
# print(bitmex.fetch_ticker('BTC/USD'))
# print(huobipro.fetch_trades('LTC/CNY'))
#
# print(exmo.fetch_balance())
#
# # sell one ฿ for market price and receive $ right now
# print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))
#
# # limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
# print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))
#
# # pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
# kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})
