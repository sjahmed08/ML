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
from marketsim import compute_portvals
from util import get_data, plot_data
import matplotlib.pyplot as plt


def author(self):
    return 'sahmed99'

if __name__=="__main__":

    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    symbol = "JPM"
    dates = dates = pd.date_range(sd, ed)
    prices_all = ut.get_data([symbol], dates)

    prices = prices_all[symbol]

    learner = st.StrategyLearner(verbose=False, impact=0.0)
    learner.addEvidence(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    test = learner.testPolicy(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)

    trades_00 = np.count_nonzero(test)
    # print test
    st_port_val_00 = compute_portvals(test, start_val=100000, commission=0, impact=0)
    st_cumu_ret_00 = (st_port_val_00[-1] / st_port_val_00[0]) - 1

    learner = st.StrategyLearner(verbose=False, impact=0.10)
    learner.addEvidence(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    test = learner.testPolicy(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    # st_trades = trades_ST(test, 'JPM')
    # st_port_val = compute_portvals(st_trades, sd, ed, 100000, 0, 0)
    # print test
    trades_10 = np.count_nonzero(test)
    # print test
    st_port_val_10 = compute_portvals(test, start_val=100000, commission=0, impact=0.10)

    st_cumu_ret_10 = (st_port_val_10[-1] / st_port_val_10[0]) - 1

    learner = st.StrategyLearner(verbose=False, impact=0.20)
    learner.addEvidence(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    test = learner.testPolicy(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    # st_trades = trades_ST(test, 'JPM')
    # st_port_val = compute_portvals(st_trades, sd, ed, 100000, 0, 0)
    # print test
    trades_20 = np.count_nonzero(test)
    # print test
    st_port_val_20 = compute_portvals(test, start_val=100000, commission=0, impact=0.20)
    st_cumu_ret_20 = (st_port_val_20[-1] / st_port_val_20[0]) - 1

    learner = st.StrategyLearner(verbose=False, impact=0.30)
    learner.addEvidence(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    test = learner.testPolicy(symbol, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    # st_trades = trades_ST(test, 'JPM')
    # st_port_val = compute_portvals(st_trades, sd, ed, 100000, 0, 0)
    # print test
    trades_30 = np.count_nonzero(test)
    # print test
    st_port_val_30 = compute_portvals(test, start_val=100000, commission=0, impact=0.30)
    st_cumu_ret_30 = (st_port_val_30[-1] / st_port_val_30[0]) - 1


    print "Portfolio Cumulative return with impact 0:", st_cumu_ret_00
    print "Number of trades with impact 0:", trades_00
    print "Portfolio Cumulative return with impact .10:", st_cumu_ret_10
    print "Number of trades with impact .10:", trades_10
    print "Portfolio Cumulative return with impact .20:", st_cumu_ret_20
    print "Number of trades return with impact .20:", trades_20
    print "Portfolio Cumulative return with impact .30:", st_cumu_ret_30
    print "Number of trades with impact .30:", trades_30

    st_port_val_00 = st_port_val_00 / st_port_val_00[0]
    st_port_val_10 = st_port_val_10 / st_port_val_10[0]
    st_port_val_20 = st_port_val_20 / st_port_val_20[0]
    st_port_val_30 = st_port_val_30 / st_port_val_30[0]

    ax = st_port_val_00.plot(fontsize=12, color="black", label="Strategy Learner - impact = 0.0")
    st_port_val_10.plot(ax=ax, color="blue", label='Strategy Learner - impact = 0.10')
    st_port_val_20.plot(ax=ax, color="green", label='Strategy Learner - impact = 0.20')
    st_port_val_30.plot(ax=ax, color="red", label='Strategy Learner - impact = 0.30')
    plt.title("Experiment 2")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")
    plt.savefig('experiment2.png')
    plt.legend()
    plt.show()
