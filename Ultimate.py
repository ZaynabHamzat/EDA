# -*- coding: utf-8 -*-
"""

@author: zaynab
"""


import pandas as pd
import matplotlib.pyplot as plt

Y = pd.read_json('logins.json')
Y.describe()
Y.set_index(pd.to_datetime(Y.login_time, unit = 'm'), inplace = True)
freqs = Y.groupby(pd.Grouper(freq = '15Min')).agg(['count'])['login_time']
freqs.plot(figsize = (10, 8))
plt.ylabel('login count')
plt.show
freqs.iloc[:96].plot(figsize = (10, 8))
plt.ylabel('login count')
plt.show
