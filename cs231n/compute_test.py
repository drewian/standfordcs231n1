import numpy as np
from collections import Counter

def compute_dist_two_loops(X_train, X):
    num_test = X.shape[0]
    num_train = X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in xrange(num_test):
        for j in xrange(num_train):
            print X_train[j]
            print X[i]
            dists[i, j] = np.sqrt(np.sum((X_train[j] - X[i])**2))
            print dists[i, j]
    return dists
