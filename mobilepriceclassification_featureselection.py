# -*- coding: utf-8 -*-
"""MobilePriceClassification_FeatureSelection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LR3oWKbl5SRkbqlxJtiniHm18X9nQrU0
"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
data = pd.read_csv("/Users/gokulalex/Datasets/mobile-price-classification/train.csv")
X = data.iloc[:,0:20]
y = data.iloc[:,-1] 
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']
print(featureScores.nlargest(10,'Score'))