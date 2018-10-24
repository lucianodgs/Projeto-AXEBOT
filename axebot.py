# Código de exemplo API Bitfinex.
# Author: Luciano Diniz Guerra Santiago
# Date: 17/10/2018

# symbols = client.symbols()
# print(symbols)
# ret = client.today(symbol)
# print(client.ticker(symbol))
# print(client.lendbook('btc', parameters))
# print(client.order_book(symbol, parameters))
# print(client.stats(symbol))
# parameters = {'limit_asks': 2, 'limit_bids': 2}
# ret['bid'] Ultima compra
# ret['ask'] Ultima venda


import time
from bitfinex.client import Client

period = 1
symbol = 'xrpusd'
client = Client()
tendencia = ['Alta', 'Baixa']
id_tendencia = 0
ultimas_compras = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
cont_compras = 0


while True:
    try:
        ret_day = client.today(symbol)
        ret = client.ticker(symbol)
    except Exception as inst:
        print("Erro: %s" % inst)
        continue

    if ultimas_compras[cont_compras] == 0:
        ultimas_compras[cont_compras] = ret['bid']
        id_tendencia = 0
    elif ultimas_compras[cont_compras] <= ret['bid']:
        ultimas_compras[cont_compras] = ret['bid']
        id_tendencia = 0
    elif ultimas_compras[cont_compras] > ret['bid']:
        ultimas_compras[cont_compras] = ret['bid']
        id_tendencia = 1

    if cont_compras == 5:
        cont_compras = 0
    else:
        cont_compras += 1

    print("%s | %s | %s"
          % (ultimas_compras[0],
             ultimas_compras[1],
             ultimas_compras[2]))
    print("Compra: %s ;Venda: %s ; Menor: %s ;Maior: %s; Data: %s | Tendencia: %s"
          % (ret['bid'],
             ret['ask'],
             ret_day['low'],
             ret_day['high'],
             time.ctime(ret['timestamp']),
             tendencia[id_tendencia]))

    time.sleep(int(period))
