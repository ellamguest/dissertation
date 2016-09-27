# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:20:25 2016

@author: emg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df2 = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfree_notdel_comment_data.csv', index_col=0)

x = df[df['score'] <= 20]
x = x[x['score'] >= -20] # 64042
float(len(x))/float(len(df))

x['score'].hist()

x=x[x['mod']==1]

x = df[df['rank'] < 31]
x = x[x['rank'] > 2]
#plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth))
#plt.hist(x['rank'], bins=15)
plt.hist(x['rank'], bins=range(3,21,1))
plt.title("Histogram of Author Comment Count")
plt.xlabel("Comment Count")
plt.ylabel("Frequency")
plt.show()


log = np.log(x+11)    
log.hist()

tanh = np.tanh(df['score']/30)
tanh.hist()

trans_data = df
trans_data['score_sqrt'] = np.sqrt(trans_data['score'])
trans_data['score_tanh'] = np.tanh(trans_data['score']/10)
trans_data.to_csv('trans_data.csv')

tops = df[df['top']==1]

qrt = np.sqrt(x['score'])