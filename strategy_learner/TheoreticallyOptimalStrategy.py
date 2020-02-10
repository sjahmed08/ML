import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import os
from util import get_data, plot_data, get_orders_data_file
from marketsim import *


def benchMark(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000):
    dates = pd.date_range(sd, ed)
    df_prices = get_data([symbol], dates)
    symbolPrices = df_prices[symbol]
    # symbolPrices = symbolPrices / symbolPrices[0]
    bm_df = pd.DataFrame()
    bm_df[symbol] = symbolPrices
    start_date_of = bm_df.index[0]
    bm_df[symbol] = 0

    bm_df.ix[start_date_of, symbol] = 1000

    return bm_df

def testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000):
    # dates = pd.date_range(sd, ed)
    # df_prices = get_data([symbol], dates)
    # symbolPrices = df_prices[symbol]
    # # symbolPrices = symbolPrices / symbolPrices[0]
    #
    # tp_df = pd.DataFrame()
    # holding_df = pd.DataFrame()
    # #tp_df['prices'] = symbolPrices
    # tp_df[symbol] = symbolPrices < symbolPrices.shift(-1)
    # tp_df[symbol] *= 1000
    # tp_df[symbol].replace(0, -1000, inplace=True)
    # # print tp_df, symbolPrices
    # return tp_df

    symbolPrices = get_data([symbol], pd.date_range(sd, ed))
    symbolPrices = symbolPrices[symbol]

    tp_df = pd.DataFrame(data=np.zeros(len(symbolPrices.index)), index=symbolPrices.index, columns=[symbol])

    priceVals = symbolPrices.values

    tradeHolding = priceVals[1] > priceVals[0]

    if tradeHolding == True:
        tp_df[symbol].iloc[0] = 1000
    else:
        tp_df[symbol].iloc[0] = -1000

    for val in range(1, len(priceVals) - 1):
        if (priceVals[val] < priceVals[val+1] and not tradeHolding) or (priceVals[val] >= priceVals[val + 1] and tradeHolding):
            tradeHolding = not tradeHolding

            if tradeHolding == True:
                tp_df[symbol].iloc[val] = 2000
            else:
                tp_df[symbol].iloc[val] = -2000

    return tp_df

class TheoreticallyOptimalStrategy:

    def testPolicy(symbol = "JPM", sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 100000):
        dates = pd.date_range(sd, ed)
        df_prices = get_data([symbol], dates)
        symbolPrices = df_prices[symbol]
        symbolPrices = symbolPrices/symbolPrices[0]

        df1 = pd.DataFrame()
        df1[symbol] = symbolPrices < symbolPrices.shift(-1)

        df1[symbol].replace(True, '1000', inplace=True)
        df1[symbol].replace(False, '-1000', inplace=True)
        return df1


def testCode():
    dev_sd = dt.datetime(2008, 1, 1)
    dev_ed = dt.datetime(2009, 12, 31)
    test_sd = dt.datetime(2010, 1, 1)
    test_ed = dt.datetime(2011, 12, 31)
    tso = TheoreticallyOptimalStrategy()
    # df_tp = tso.testPolicy()
    df_tp = testPolicy(symbol="JPM", sd=dev_sd, ed=dev_ed)
    sv = 100000
    tso_port_val = compute_portvals(df_tp, sv, 0, 0)
    tso_port_val = tso_port_val / tso_port_val[0]

    tso_cumu_ret = (tso_port_val[-1] / tso_port_val[0]) - 1

    daily_rets = tso_port_val.copy()
    daily_rets[1:] = (tso_port_val[1:] / tso_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    tso_avg_daily_ret = daily_rets.mean()
    tso_std_daily_ret = daily_rets.std()

    print "###Total Optimal Strategy statistics### "
    print "Cumulative Returns: ", tso_cumu_ret
    print "Average Daily Return: ", tso_avg_daily_ret
    print "Average Standard Deviation Return: ", tso_std_daily_ret

    #print tso_port_val

    bm_df = benchMark(symbol="JPM", sd=dev_sd, ed=dev_ed)
    bm_port_val = compute_portvals(bm_df, sv, 0, 0)
    bm_port_val = bm_port_val / bm_port_val[0]

    bm_cumu_ret = (bm_port_val[-1] / bm_port_val[0]) - 1

    daily_rets = bm_port_val.copy()
    daily_rets[1:] = (bm_port_val[1:] / bm_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    bm_avg_daily_ret = daily_rets.mean()
    bm_std_daily_ret = daily_rets.std()
    print ""
    print "###Benchmark statistics### "
    print "Cumulative Returns: ", bm_cumu_ret
    print "Average Daily Return: ", bm_avg_daily_ret
    print "Average Standard Deviation Return: ", bm_std_daily_ret


    #print bm_port_val
    plt.figure(figsize=(20, 7))
    plt.gca().set_color_cycle(['black', 'blue'])
    port, = plt.plot(tso_port_val)
    bench, = plt.plot(bm_port_val)
    plt.legend([port, bench], ['Optimal', 'Benchmark'])
    plt.title("Manual vs Benchmark")
    plt.savefig('Optimal Vs Bench.png')
    plt.show()


if __name__ == "__main__":
    testCode()
    # dev_sd = dt.datetime(2008, 1, 1)
    # dev_ed = dt.datetime(2009, 12, 31)
    # test_sd = dt.datetime(2010, 1, 1)
    # test_ed = dt.datetime(2011, 12, 31)
    # tso = TheoreticallyOptimalStrategy()
    # # df_tp = tso.testPolicy()
    # df_tp = testPolicy(symbol="JPM", sd=dev_sd, ed=dev_ed)

    # print df_tp
