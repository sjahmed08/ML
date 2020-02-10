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


import datetime as dt
import pandas as pd
import util as ut
import random
import numpy as np
import StrategyLearner as st
from ManualStrategy import testPolicy
from marketsim import compute_portvals
from util import get_data, plot_data
import matplotlib.pyplot as plt




def author(self):
    return 'sahmed99'


if __name__=="__main__":

    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)

    out_sd = dt.datetime(2010, 1, 1)
    out_ed = dt.datetime(2011, 12, 31)
    symbol = "JPM"
    dates = dates = pd.date_range(sd, ed)
    prices_all = ut.get_data([symbol], dates)

    # Strategy Learner
    learner = st.StrategyLearner(verbose=False, impact=0.0)
    learner.addEvidence(symbol, sd=sd, ed=ed, sv=100000)
    test = learner.testPolicy(symbol, sd=sd, ed=ed, sv=100000)
    # st_trades = trades_ST(test, 'JPM')
    # st_port_val = compute_portvals(st_trades, sd, ed, 100000, 0, 0)
    # print test

    # print test
    st_port_val = compute_portvals(test, start_val=100000, commission=0, impact=0)
    # print "strategy port val", st_port_val

    #benchmark
    bench = st.benchMark(symbol, sd, ed, 100000)
    bm_port_val = compute_portvals(bench, 100000, 0, 0)
    # print "bench port val", bench_port_val

    # ManualStrategy
    trades = testPolicy(symbol, sd=sd, ed=ed, sv=100000)
    ms_port_val = compute_portvals(trades, 100000, 0, 0)

    # print ms_port_val

    ms_port_val = ms_port_val / ms_port_val[0]

    ms_cumu_ret = (ms_port_val[-1] / ms_port_val[0]) - 1

    daily_rets = ms_port_val.copy()
    daily_rets[1:] = (ms_port_val[1:] / ms_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    ms_avg_daily_ret = daily_rets.mean()
    ms_std_daily_ret = daily_rets.std()
    ms_sr = (np.sqrt(252.0) * ms_avg_daily_ret) / ms_std_daily_ret

    print "###Manual Strategy statistics### "
    print "Cumulative Returns: ", ms_cumu_ret
    print "Average Daily Return: ", ms_avg_daily_ret
    print "Average Standard Deviation Return: ", ms_std_daily_ret
    print "Sharpe Ratio ", ms_sr

    bm_port_val = bm_port_val / bm_port_val[0]

    bm_cumu_ret = (bm_port_val[-1] / bm_port_val[0]) - 1

    daily_rets = bm_port_val.copy()
    daily_rets[1:] = (bm_port_val[1:] / bm_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    bm_avg_daily_ret = daily_rets.mean()
    bm_std_daily_ret = daily_rets.std()
    bm_sr = (np.sqrt(252.0) * bm_avg_daily_ret) / bm_std_daily_ret

    print "###Benchmark statistics### "
    print "Cumulative Returns: ", bm_cumu_ret
    print "Average Daily Return: ", bm_avg_daily_ret
    print "Average Standard Deviation Return: ", bm_std_daily_ret
    print "Sharpe Ratio", bm_sr

    st_port_val = st_port_val / st_port_val[0]
    st_cumu_ret = (st_port_val[-1] / st_port_val[0]) - 1
    daily_rets = st_port_val.copy()
    daily_rets[1:] = (st_port_val[1:] / st_port_val[:-1].values) - 1
    daily_rets.ix[0] = 0
    st_avg_daily_ret = daily_rets.mean()
    st_std_daily_ret = daily_rets.std()
    st_sr = (np.sqrt(252.0) * st_avg_daily_ret) / st_std_daily_ret

    print "###Strategy Learner statistics### "
    print "Cumulative Returns: ", st_cumu_ret
    print "Average Daily Return: ", st_avg_daily_ret
    print "Average Standard Deviation Return: ", st_std_daily_ret
    print "Sharpe Ratio ", st_sr

    ax = ms_port_val.plot(fontsize=12, color="black", label="Manual Strategy")
    bm_port_val.plot(ax=ax, color="blue", label='Benchmark')
    st_port_val.plot(ax=ax, color="green", label='Strategy Learner')
    plt.title("Experiment 1")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")
    plt.savefig('experiment1.png')
    plt.legend()
    plt.show()