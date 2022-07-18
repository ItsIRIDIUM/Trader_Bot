import schedule
import time
from trader import *


# bot data
account = int(5002657555)
password = 'ucln0cwy'
server = 'MetaQuotes-Demo'
symbol = 'EURUSD'


if __name__ == '__main__':
    schedule.every().hour.at(":04").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":09").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":14").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":19").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":24").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":29").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":34").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":39").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":44").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":49").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":54").do(trading, account=account, password=password, server=server)
    schedule.every().hour.at(":59").do(trading, account=account, password=password, server=server)

    while True:
        schedule.run_pending()
        time.sleep(1)

