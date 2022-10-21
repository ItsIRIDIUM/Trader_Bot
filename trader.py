import MetaTrader5 as mt
from calc import *
from catch import catch_exceptions
import datetime
import datetime


# connecting to MetaTrader 5
@catch_exceptions()
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
@catch_exceptions()
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
        print("Failed to send order :(", mt.last_error())
        open_position(pair, order_type, size)
    else:
        print("Order successfully placed!")


# get orders
@catch_exceptions()
def positions_get(symbol):
    res = mt.positions_get(symbol=symbol)

    return res


# close order
@catch_exceptions()
def close_position(deal_id, symbol):
    open_positions = positions_get(symbol)
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
    if result.retcode == mt.TRADE_RETCODE_REQUOTE:
        close_pos_by_symbol(symbol)
    else:
        print("Order successfully closed!")


@catch_exceptions()
def close_pos_by_symbol(symbol):
    print('try ot close')
    for _ in range(len(positions_get(symbol))):
        close_position(int(positions_get(symbol)[0][0]), symbol)


@catch_exceptions()
def msg(t, m, symbol):
    print(t, vertex[-1], vertex[-2], datetime.datetime.now().time(), m, symbol)


@catch_exceptions()
def trading(account, password, server, symbols):
    for symbol in symbols:
        num = 2
        pos = positions_get(symbol)
        try:
            if len(pos):
                if pos[0][5]:
                    num = 0
                else:
                    num = 1
        except:
            pass

        if datetime.datetime.today().weekday() != 5 and datetime.datetime.today().weekday() != 6:
            connect(account, password, server)
            account_info = mt.account_info()
            balance = account_info[10]
            vol = balance / 16 / 100
            vol = round(vol, 2)
            m = start(symbol)
            if vertex[-2] <= -10:
                msg('B', m, symbol)
                open_position(symbol, 'BUY', vol, 5000, 5000)
            elif vertex[-2] >= 10:
                msg('S', m, symbol)
                open_position(symbol, 'SELL', vol, 5000, 5000)
            else:
                if num == 1:
                    if vertex[-1] >= 0 or vertex[-2] >= 0:
                        msg('=', m, symbol)
                        close_pos_by_symbol(symbol)
                    else:
                        msg('-', m, symbol)
                elif num == 0:
                    if vertex[-1] <= 0 or vertex[-2] <= 0:
                        msg('=', m, symbol)
                        close_pos_by_symbol(symbol)
                    else:
                        msg('-', m, symbol)
                else:
                    msg('#', m, symbol)
        else:
            print('It is weekend')
