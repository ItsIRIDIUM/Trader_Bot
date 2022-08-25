import schedule
import time
from trader import *


# bot data
account = int(61804102)
password = 'jz2mxdlp'
server = 'MetaQuotes-Demo'
symbols = ['EURUSD']


if __name__ == '__main__':
    schedule.every().hour.at("04:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("09:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("14:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("19:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("24:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("29:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("34:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("39:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("44:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("49:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("54:30").do(trading, account=account, password=password, server=server, symbols=symbols)
    schedule.every().hour.at("59:30").do(trading, account=account, password=password, server=server, symbols=symbols)

    while True:
        schedule.run_pending()
        time.sleep(1)
