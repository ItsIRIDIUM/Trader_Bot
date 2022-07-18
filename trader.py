import MetaTrader5 as mt
import pandas as pd
from calc import *
import math
import datetime as g


# connecting to MetaTrader 5
def connect(account, password, server):
    account = int(account)
    mt.initialize()
    authorized = mt.login(account, password, server)

    if authorized:
        pass
        # print("Connected: Connecting to MT5 Client")
    else:
        print("Failed to connect at account #{}, error code: {}"
              .format(account, mt.last_error()))


# open order
def open_position(pair, order_type, size, tp_distance=None, stop_distance=None):
    symbol_info = mt.symbol_info(pair)
    if symbol_info is None:
        print(pair, "not found")
        return

    if not symbol_info.visible:
        print(pair, "is not visible, trying to switch on")
        if not mt.symbol_select(pair, True):
            print("symbol_select({}}) failed, exit", pair)
            return

    point = symbol_info.point

    if order_type == "BUY":
        order = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick(pair).ask
        if stop_distance:
            sl = price - (stop_distance * point)
        if tp_distance:
            tp = price + (tp_distance * point)

    elif order_type == "SELL":
        order = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick(pair).bid
        if stop_distance:
            sl = price + (stop_distance * point)
        if tp_distance:
            tp = price - (tp_distance * point)

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": pair,
        "volume": float(size),
        "type": order,
        "price": price,
        "sl": sl,
        "tp": tp,
        "magic": 234000,
        "comment": "",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    result = mt.order_send(request)
    print('result retcode: ', result.retcode)

    if result.retcode != mt.TRADE_RETCODE_DONE:
        print("Failed to send order :(")
    else:
        print("Order successfully placed!")


# get orders
def positions_get(symbol=None):
    if symbol is None:
        res = mt.positions_get()
    else:
        res = mt.positions_get(symbol=symbol)

    return res


# close order
def close_position(deal_id):
    open_positions = positions_get()
    order_type = open_positions[0][5]
    symbol = open_positions[0][16]
    volume = open_positions[0][9]

    if (order_type == mt.ORDER_TYPE_BUY):
        order_type = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick(symbol).bid
    else:
        order_type = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick(symbol).ask

    close_request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(volume),
        "type": order_type,
        "position": deal_id,
        "price": price,
        "magic": 234000,
        "comment": "Close trade",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    result = mt.order_send(close_request)

    if result.retcode != mt.TRADE_RETCODE_DONE:
        print("Failed to close order :(")
    else:
        print("Order successfully closed!")


def close_pos_by_symbol(symbol):
    close_position(int(positions_get()[0][0]))


def trading(account, password, server):
    mt.initialize()
    num = 2
    pos = positions_get('EURUSD')
    if not len(pos):
        num = 2
    elif len(pos):
        if pos[0][5]:
            num = 0
        else:
            num = 1

    if not len(pos):
        if g.datetime.today().weekday() != 5 and g.datetime.today().weekday() != 6:
            connect(account, password, server)
            account_info = mt.account_info()
            balance = account_info[10]
            vol = balance / 16 / 100
            if num == 2:
                m = start()
                if vertex[-2] <= -10:
                    print('B', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
                    open_position(symbol, 'BUY', vol, 5000, 5000)
                elif vertex[-2] >= 10:
                    print('S', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
                    open_position(symbol, 'SELL', vol, 5000, 5000)
                else:
                    print('#', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
        else:
            print('It is weekend')
    else:
        if g.datetime.today().weekday() != 5 and g.datetime.today().weekday() != 6:
            if num == 1:
                m = start()
                if vertex[-1] >= 0 or vertex[-2] >= 0:
                    print('-', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
                    close_pos_by_symbol(symbol)
                    num = 2
                else:
                    print('#', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
            elif num == 0:
                m = start()
                if vertex[-1] <= 0 or vertex[-2] <= 0:
                    print('=', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
                    close_pos_by_symbol(symbol)
                    num = 2
                else:
                    print('#', vertex[-1], vertex[-2], datetime.datetime.now().time(), m)
        else:
            print('It is weekend')

        return num
