import ccxt

binance = ccxt.binance({
    'apiKey': '7o6rbHZbD2uJcZC3XIGyZHUjxStCdByNUufe52r2gv2zgr3lr8fHeBibyD5Cr3UW',
    'secret': 'ISqKlDLESnNbmdHT5nVpYjtdF3yHcN7LaXSbJQvma0FUD1bY5Yz12biR6LBQeD3M',
})

print(binance.fetch_balance())

