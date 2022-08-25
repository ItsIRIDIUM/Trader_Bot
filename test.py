import MetaTrader5 as mt
from trader import *

account = int(61804102)
password = 'jz2mxdlp'
server = 'MetaQuotes-Demo'
symbols = ['EURUSD']

connect(account, password, server)
print(positions_get(symbols[0]))