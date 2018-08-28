#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decision Tree is explainable, we need to understand how to explain it

# Example of Decision Tree
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

p = clf.predict([[2., 2.]])

print(p)