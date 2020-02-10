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

import numpy as np
from random import randint

class RTLearner(object):

    def __init__(self, leaf_size, verbose=False):
        pass  # move along, these aren't the drones you're looking for
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None

    def author(self):
        return 'sahmed99'  # replace tb34 with your Georgia Tech username

    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """

        dataY = np.array([dataY])

        xyData = np.append(dataX,dataY.T,axis=1)
 
        self.tree = self.buildTree(xyData)

        # build and save the model
        # self.model_coefs, residuals, rank, s = np.linalg.lstsq(newdataX, dataY)

    def buildTree(self, data):
        # print data
        if data.shape[0] <= self.leaf_size:
            return np.array([["Leaf", np.mean(data[:,-1]), np.nan, np.nan]])

        if np.all(data[0,-1]==data[:,-1],axis=0):
            return np.array([["Leaf",data[0,-1],np.nan, np.nan]])

        else:

            best_corr = randint(0,data.shape[1]-2)

            Split_Val = np.median(data[:,best_corr])

            Max = max(data[:, best_corr])
            if Max == Split_Val:
                return np.array([['Leaf', np.mean(data[:, -1]), np.nan, np.nan]])

            Left_Tree = self.buildTree(data[data[:, best_corr] <= Split_Val])
            Right_Tree = self.buildTree(data[data[:, best_corr] > Split_Val])

            root = np.array([[best_corr,Split_Val,1,Left_Tree.shape[0]+1]])
            combined = np.vstack((root, Left_Tree, Right_Tree))

            # print "Combined tree", combined
            return combined

    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        result=[]
        row_num=points.shape[0]
        for row in range(0,row_num):
            value=self.searchTree(points[row,:])

            result.append(float(value))

        return result

    def searchTree(self, val):
        rowVal = 0

        # if not a leaf node
        while (self.tree[rowVal, 0] != 'Leaf'):
            splitVal = self.tree[rowVal, 1]
            ft = self.tree[rowVal, 0]


            if val[int(float(ft))] <= float(splitVal):
                rowVal = rowVal + int(float(self.tree[rowVal, 2]))
            else:
                rowVal = rowVal + int(float(self.tree[rowVal, 3]))
        return self.tree[rowVal, 1]

if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"
