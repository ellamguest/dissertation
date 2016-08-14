# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:20:25 2016

@author: emg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfree_notdel_comment_data.csv', index_col=0)

x = df[df['score'] <= 20]
x = x[x['score'] >= -20] # 64042
float(len(x))/float(len(df))

x['score'].hist()

x=x[x['mod']==1]


plt.hist(np.tanh(df['score']/10), bins=10)
plt.title("Histogram of Comment Scores (tanh transformed)")
plt.xlabel("tanh(Score/10)")
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