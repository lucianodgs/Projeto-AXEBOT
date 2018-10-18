## Código de exemplo API Bitfinex.
##Author: Luciano Diniz Guerra Santiago
##Date: 17/10/2018

#symbols = client.symbols()
#print(symbols)
#ret = client.today(symbol)
#print(client.ticker(symbol))
#print(client.lendbook('btc', parameters))
#print(client.order_book(symbol, parameters))
#print(client.stats(symbol))
#parameters = {'limit_asks': 2, 'limit_bids': 2}
# ret['bid'] --Ultima compra
# ret['ask'] --Ultima venda
#

import json
import time
from bitfinex.client import Client

period = 10
symbol = 'xrpusd'
client = Client()

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))


while True:
    ret_day = client.today(symbol)
    ret = client.ticker(symbol)

    print("Compra: %s ;Venda: %s ; Menor: %s ;Maior: %s; Data: %s" %(ret['bid'],ret['ask'],  ret_day['low'], ret_day['high'], time.ctime(ret['timestamp'])))
    time.sleep(int(period))
