import MetaTrader5 as mt
import numpy as np
# from rich.console import Console
# from rich.table import Table
# import matplotlib.pyplot as plt
import datetime

# H1 = 300 H4 = 200


timeframe = mt.TIMEFRAME_M5
rates_total = 50
period = 5  # 4 hours in minutes

length = rates_total

control_period = 14

level_b = 10
level_s = -10

vertex = []


def start(symbol):
    try:
        mt.initialize()
        rates = mt.copy_rates_from_pos(symbol, timeframe, 0, rates_total)

        opn = np.zeros(rates_total)
        low = np.zeros(rates_total)
        hig = np.zeros(rates_total)
        cls = np.zeros(rates_total)

        for p in range(rates_total):
            opn[p] = rates[p][1]
            low[p] = rates[p][3]
            hig[p] = rates[p][2]
            cls[p] = rates[p][4]

        # ####

        for i in range(rates_total):
            complex_up = 0
            complex_dn = 0
            trigger_high = -999999
            trigger_low = 999999
            for n in range(control_period):
                sum_up = 0
                sum_dn = 0
                bar_shift = i - n
                bar_count = bar_shift + period

                if bar_count > length - 1:
                    bar_count = length - 1

                for j in range(bar_count + 1):
                    if 0 <= j + bar_shift < rates_total:
                        if hig[j + bar_shift] > trigger_high:
                            trigger_high = hig[j + bar_shift]
                            sum_up += cls[j + bar_shift]
                        if low[j + bar_shift] < trigger_low:
                            trigger_low = low[j + bar_shift]
                            sum_dn += cls[j + bar_shift]

                complex_up += sum_up
                complex_dn += sum_dn

            if complex_up != 0 and complex_dn != 0:
                v = complex_dn / complex_up - complex_up / complex_dn
                vertex.append(v)
        return opn[-1], opn[-2]
    except:
        print("error in calc")
