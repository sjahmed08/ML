"""MC2-P1: Technical indicators.

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

Student Name: Tucker Balch (replace with your name)
GT User ID: sahmed99 (replace with your User ID)
GT ID: 903388682 (replace with your GT ID)
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import os
from util import get_data, plot_data, get_orders_data_file

def author():
    return 'sahmed99'

def get_rolling_mean(values, window):
    return pd.rolling_mean(values, window=window)

def get_rolling_std(values, window):
    return pd.rolling_std(values, window=window)

def get_bollinger_bands(rm, rstd):
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band

def get_bollinger_band(dfPrices, stockSymbol, plot = False, lookback = 10):

    #1 computer rolling mean
    rm_JPM = get_rolling_mean(dfPrices, window=lookback)

    #2 compute rolling standard deviation
    rstd_JPM = get_rolling_std(dfPrices, window=lookback)

    #3 compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_JPM, rstd_JPM)




    bollinger_band = (dfPrices - rm_JPM) / (2* rstd_JPM)

    if plot == True:
        ax = dfPrices.plot(title="JPM Bollinger Bands", label=stockSymbol)
        rm_JPM.plot(label='Rolling mean', ax=ax)
        upper_band.plot(label='upper band', ax=ax)
        lower_band.plot(label='lower band', ax=ax)
        bollinger_band.plot(label='bollinger band', ax=ax)

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')
        # plt.figure(figsize=(20, 7))
        plt.savefig('BB_Indicator.png')
        plt.show()
        plt.clf()


    return bollinger_band

def get_sma(dfPrices, stockSymbol, plot = False, lookback = 10):


    rm_JPM = get_rolling_mean(dfPrices, window=lookback)


    sma_df = rm_JPM - 1


    if plot == True:
        ax = dfPrices.plot(title="JPM SMA to price", label=stockSymbol)
        rm_JPM.plot(label='Rolling mean', ax=ax)
        sma_df.plot(label='SMA', ax=ax)

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')
        # plt.figure(figsize=(20, 7))
        plt.savefig('SMA_Indicator.png')
        plt.show()
        plt.clf()


    return sma_df

def get_commodity_channel_index(dfPrices, stockSymbol, plot = False, lookback = 10):


    cci_rm = get_rolling_mean(dfPrices, window = lookback)
    cci = (dfPrices-cci_rm)/(2.5 * dfPrices.std())


    if plot == True:
        ax = dfPrices.plot(title="Commodity Channel Index", label=stockSymbol)
        cci.plot(label="CCI", ax=ax)

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')
        # plt.figure(figsize=(20, 7))
        plt.savefig('CCI_Indicator.png')
        plt.show()
        plt.clf()



    return cci


def get_indicators(stockSymbol, sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), plot1 = False, lookback1 = 10):
    start_date = sd
    end_date = ed
    dates = pd.date_range(start_date, end_date)

    dfPrices = get_data([stockSymbol], dates)
    dfPrices = dfPrices.drop('SPY', axis=1)

    prices = dfPrices[stockSymbol]
    prices = prices/prices[0]

    # Generate plots
    indicators_df = pd.DataFrame()
    indicators_df['bb'] = get_bollinger_band(prices, stockSymbol, plot = plot1, lookback = lookback1)
    indicators_df['sma'] = get_sma(prices, stockSymbol, plot = plot1, lookback = lookback1)
    # indicators_df['cci'] = get_commodity_channel_index(prices, stockSymbol, plot = plot1, lookback = lookback1)

    # indicators_df.dropna()
    return indicators_df


if __name__ == "__main__":
    stockSymbol = 'JPM'
    # get_indicators(stockSymbol)
    # get_bollinger_band()
    indicators_df = get_indicators(stockSymbol, plot1 = True)
