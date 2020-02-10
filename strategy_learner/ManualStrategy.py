"""
Template for implementing StrategyLearner  (c) 2016 Tucker Balch

Copyright 2018, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 4646/7646

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CS 7646 is prohibited and subject to being investigated as a
GT honor code violation.

-----do not edit anything above this line---

Student Name: Syed Ahmed (replace with your name)
GT User ID: sahmed99 (replace with your User ID)
GT ID: 903388682 (replace with your GT ID)
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import os
import sys
from util import get_data, plot_data, get_orders_data_file
from indicators import *
from TheoreticallyOptimalStrategy import *

def author():
    return 'sahmed99'


def testPolicy(symbol = "AAPL", sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 100000):
    lookback = 10

    dates = pd.date_range(sd, ed)
    df_prices = get_data([symbol], dates)
    symbolPrices = df_prices[symbol]

    df_order = pd.DataFrame(data=np.zeros(len(symbolPrices.index)), index=symbolPrices.index, columns=[symbol])

    # symbolPrices = symbolPrices / symbolPrices[0]

    indicators_df = get_indicators(symbol, sd = sd, ed = ed, plot1 = False)

    sma_df = indicators_df['sma']
    bb_df = indicators_df['bb']

    previous = 0


    for i in range(lookback + 1, len(symbolPrices.index)):
        if ((sma_df[i] < -.10) and (bb_df[i] < -.5)):
            # print "signal buy"
            df_order[symbol].iloc[i] = 1000 - previous
            previous = 1000
            # print sma_df[i]
        elif ((sma_df[i] > .05 ) and (bb_df[i] > .5)):
            # print "signal sell"
            df_order[symbol].iloc[i] = -1000 - previous
            previous = -1000
            # print sma_df[i]

    # for index in range(lookback + 1, indicators_df.shape[0]):
    #     if ((sma_df.ix[index] < -.10) and (bb_df.ix[index] < -.5)):
    #         print "signal buy"
    #         order.ix[index, symbol] = 1000
    #     elif ((sma_df.ix[index] > .05 ) and (bb_df.ix[index] > .5)):
    #         print "signal sell"
    #         order.ix[index, symbol] = -1000
    #     else:
    #         print "signal hold"
    #         order.ix[index] = 0

    # for index in range(0, lookback + 1):
    #     order.ix[index, symbol] = 0
    #
    # for index in range(indicators_df.shape[0], indicators_df.shape[0] + lookback - 1):
    #     order.ix[index, symbol] = 0


    return df_order


def testCode():
    dev_sd = dt.datetime(2008, 1, 1)
    dev_ed = dt.datetime(2009, 12, 31)
    test_sd = dt.datetime(2010, 1, 1)
    test_ed = dt.datetime(2011, 12, 31)
    if sys.argv[1:] == ['1']:
        print sys.argv[1:]
        print "Out sample dates selected"
        dev_sd = test_sd
        dev_ed = test_ed
    df_ms = testPolicy(symbol="JPM", sd=dev_sd, ed=dev_ed)

    dates = pd.date_range(dev_sd, dev_ed)
    # print df_ms
    df_prices = get_data(["JPM"], dates)

    df_prices = df_prices['JPM']
    df_prices = df_prices / df_prices[0]

    sv = 100000
    ms_port_val = compute_portvals(df_ms, sv, commission=9.95, impact=.005)
    ms_port_val = ms_port_val / ms_port_val[0]

    ms_cumu_ret = (ms_port_val[-1] / ms_port_val[0]) - 1

    daily_rets = ms_port_val.copy()
    daily_rets[1:] = (ms_port_val[1:] / ms_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    ms_avg_daily_ret = daily_rets.mean()
    ms_std_daily_ret = daily_rets.std()

    print "###Manual Strategy statistics### "
    print "Cumulative Returns: ", ms_cumu_ret
    print "Average Daily Return: ", ms_avg_daily_ret
    print "Average Standard Deviation Return: ", ms_std_daily_ret

    # print tso_port_val

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

    plt.figure(figsize=(20, 7))
    plt.gca().set_color_cycle(['black', 'blue'])
    port, = plt.plot(ms_port_val)
    bench, = plt.plot(bm_port_val)

    for pr in range(len(df_prices.index)):
        if df_ms['JPM'].iloc[pr] > 0:
            print "green"
            print df_prices[pr]
            plt.axvline(x=df_prices[pr], color = 'g')
        elif df_ms['JPM'].iloc[pr] < 0:
            # print "red"
            plt.axvline(x=df_prices[pr], color = 'r')
            print "red"
            print df_prices[pr]

    plt.legend([port, bench], ['Manual', 'Benchmark'])
    plt.title("Manual vs Benchmark")
    #plt.savefig('Manual Vs Bench.png')
    plt.show()


if __name__ == "__main__":
    testCode()