## Código de exemplo API Bitfinex.
##Author: Luciano Diniz Guerra Santiago
##Date: 17/10/2018

#symbols = client.symbols()
#print(symbols)
#print(client.ticker(symbol))
#print(client.lendbook('btc', parameters))
#print(client.order_book(symbol, parameters))
#print(client.stats(symbol))
##


import json
import time
from bitfinex.client import Client

client = Client()

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))



symbol = 'btgusd'


ret = client.today(symbol)
ret['low']
ret['high']
ret['volume']



#print(client.today(symbol))

print(client.ticker(symbol))

parameters = {'limit_asks': 2, 'limit_bids': 2}

