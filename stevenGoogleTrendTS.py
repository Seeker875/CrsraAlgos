# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf


df = pd.read_csv('stevenTrend.csv',skiprows=1)
df.head()
df.columns = ['Month', 'StevCount']

df.index = pd.to_datetime(df.Month)

df = df.drop(['Month'], axis=1)

#dropping first row cuz of 100, last to make feb to feb 10yr comparison
df = df.drop(df.index[0])
df = df.drop(df.index[-1])

df.plot()
#seasonality



plot_acf(df,lags= 24,alpha=0.05)
##strong positive autocorrelation at 12and 6 month

autocorrelation= df.StevCount.autocorr(lag=12)
#0.77
autocorrelation

from math import sqrt

nobs = len(df)

# confidence interval
conf = 1.96/sqrt(nobs)
print("The approxmate confidence interval is +/- %4.2f" %(conf))

from collections import defaultdict

monthlyVisits = defaultdict(int)

  
for index, row in df.iterrows():
    
   # Counting monthly count
    monthlyVisits[index.month] += int(row[0])
    
print(monthlyVisits)

 

