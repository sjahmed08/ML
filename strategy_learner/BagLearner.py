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
import RTLearner

class BagLearner(object):

    def __init__(self, learner, kwargs={"leaf_size":1},bags=10,boost=False, verbose = False):
        pass  # move along, these aren't the drones you're looking for
        self.verbose = verbose
        learners = []
        for i in range(0, bags):
            learners.append(learner(**kwargs))

        self.learners = learners
        self.bags = bags



    def author(self):
        return 'sahmed99'  # replace tb34 with your Georgia Tech username

    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """

        samp_index = dataX.shape[0]

        for learner in self.learners:
            idx = np.random.choice(samp_index, samp_index)
            databX = dataX[idx]
            databY = dataY[idx]
            learner.addEvidence(databX, databY)


        # build and save the model
        # self.model_coefs, residuals, rank, s = np.linalg.lstsq(newdataX, dataY)

    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        query_list=[]
        for learner in self.learners:
            query_list.append(learner.query(points))
        quary_array = np.array(query_list)
        ans = np.mean(quary_array, axis=0)
        return ans.tolist()


if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"
