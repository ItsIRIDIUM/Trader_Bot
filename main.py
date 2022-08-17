import schedule
import time
import logging
from trader import *


# bot data
account = int(5002657555)
password = 'ucln0cwy'
server = 'MetaQuotes-Demo'
symbols = ['EURUSD', 'GBPUSD', 'GBPJPY', 'XAUUSD']
# symbols = 'EURUSD', 'GBPUSD', 'USDCHF', 'USDJPY', 'USDCNH', 'USDRUB', 'AUDUSD', 'NZDUSD', 'USDCAD', 'USDSEK', \
#           'USDHKD', 'USDSGD', 'USDNOK', 'USDDKK', 'USDTRY', 'USDZAR', 'USDCZK', 'USDHUF', 'USDPLN', 'USDRUR', \
#           'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF', \
#           'EURCZK', 'EURDKK', 'EURGBP', 'EURHKD', 'EURHUF', 'EURJPY', 'EURNOK', 'EURNZD', 'EURPLN', 'EURRUR', \
#           'EURRUB', 'EURSEK', 'EURTRY', 'EURZAR', 'GBPAUD', 'GBPCHF', 'GBPJPY', 'XAUUSD', 'XAGUSD', 'GBPCAD', \
#           'GBPNOK', 'GBPNZD', 'GBPPLN', 'GBPPLN', 'GBPSEK', 'GBPSGD', 'GBPZAR', 'NZDCAD', 'NZDCHF', 'NZDJPY', \
#           'NZDSGD', 'SGDJPY', 'XPDUSD', 'XPTUSD'

if __name__ == '__main__':
    schedule.every().hour.at(":04").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":09").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":14").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":19").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":24").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":29").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":34").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":39").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":44").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":49").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":54").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at(":59").do(trading, account=account, password=password, server=server, symbols=symbols)

    while True:
        schedule.run_pending()
        time.sleep(1)
