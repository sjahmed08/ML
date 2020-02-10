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
import BagLearner as bl
import RTLearner as rt
import numpy as np
from indicators import *


class StrategyLearner(object):

    def author(self):
        return 'sahmed99'
  		   	  			    		  		  		    	 		 		   		 		  
    # constructor  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, verbose = False, impact=0.0):  		   	  			    		  		  		    	 		 		   		 		  
        self.verbose = verbose  		   	  			    		  		  		    	 		 		   		 		  
        self.impact = impact
        self.window_size = 20
        self.feature_size = 5
        self.N = 10
        bags = 20
        leaf_size = 5
        self.learner = bl.BagLearner(learner = rt.RTLearner, bags = bags, kwargs={"leaf_size":leaf_size})
  		   	  			    		  		  		    	 		 		   		 		  
    # this method should create a QLearner, and train it for trading  		   	  			    		  		  		    	 		 		   		 		  
    def addEvidence(self, symbol = "IBM", \
        sd=dt.datetime(2008,1,1), \
        ed=dt.datetime(2009,1,1), \
        sv = 10000):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
        # add your code to do learning here

        prices = ut.get_data([symbol], pd.date_range(sd, ed))
        prices = prices[symbol]

        lookback = self.N
        lookahead = 5
        # indicators_df = SMA
        indicators_df = get_indicators(symbol, sd, ed, plot1=False, lookback1 = lookback)
        indicators_df.fillna(0, inplace=True)
        indicators_df = indicators_df[:-lookahead]
        trainX = indicators_df.values

        # print prices
        # print indicators_df

        trainY = []

        for i in range (0, lookback):
            trainY.append(0)


        for i in range(lookback, prices.shape[0] - 5):

            ret = (prices.ix[i + lookahead, symbol] - prices.ix[i, symbol]) / prices.ix[i, symbol]
            # print prices.ix[i+5, symbol]
            # print prices.ix[i, symbol]
            # print ret
            # print i
            if ret > (0.02 + self.impact):
                trainY.append(1)
            elif ret < (-0.02 - self.impact):
                trainY.append(-1)
            else:
                trainY.append(0)
        trainY = np.array(trainY)

        self.learner.addEvidence(trainX[lookback:], trainY[lookback:])

  		   	  			    		  		  		    	 		 		   		 		  
    # this method should use the existing policy and test it against new data  		   	  			    		  		  		    	 		 		   		 		  
    def testPolicy(self, symbol = "IBM", \
        sd=dt.datetime(2010,1,1), \
        ed=dt.datetime(2011,12,31), \
        sv = 10000):

        # here we build a fake set of trades
        # your code should return the same sort of data
        prices = ut.get_data([symbol], pd.date_range(sd, ed))

        lookback = 10

        indicators_df = get_indicators(symbol, sd, ed, plot1=False, lookback1=lookback)
        indicators_df.fillna(0, inplace=True)
        indicators_df = indicators_df[:-5]

        testX = indicators_df.values
        trades = prices[[symbol,]].copy(deep=True)
        trades.values[:, :] = 0


        resultY = self.learner.query(testX)
        curr = 0
        for i, r in enumerate(resultY):
            if r > 0:
                trades.values[i, :] = 1000 - curr
                curr = 1000
            elif r < 0:
                trades.values[i, :] = -1000 - curr
                curr = -1000

        return trades

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
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "One does not simply think up a strategy"

    SObject = StrategyLearner()
    SObject.addEvidence()
    SObject.testPolicy()




