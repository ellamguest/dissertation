# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:52:56 2016

@author: emg
"""
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfree_notdel_comment_data.csv', index_col=0)
stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', index_col=0)

df = df.reset_index()
df['rank'] = df.groupby('author')['created_utc'].rank()
df = df.sort(['author', 'rank'])

subs = list(stats_df.index)
del_rates = list(stats_df['del_rate'])
df['del_rates'] = df['subreddit']
df['del_rates'] = df.del_rates.replace(subs, del_rates)
df['log_del_rate'] = np.log(df['del_rates'])

df['nontop'] = (df['top'] - 1) * -1
mods = df[df['mod'] == 1]

h1b2 = smf.logit(formula='nontop ~ author_count + rank', data=mods).fit()
print(h1b2.summary())

variables = ['author', 'subreddit', 'score', 'mod', 'top', 'author_count', 'rank', 'del_rates']
data = df[variables]

#test = x['score'].head(n=20).to_frame()
#data['score_level'] = 0
data['score_level'] = data['score'].apply(lambda x: 'neg' if x < 0 else 'low' if x >= 0 and x <= 4 else 'high')
data['neg_score'] = data['score'].apply(lambda x: 1 if x < 0 else 0)
data['low_score'] = data['score'].apply(lambda x: 1 if x >= 0 and x <= 4 else 0)
data['high_score'] = data['score'].apply(lambda x: 1 if x > 4 else 0)

data.to_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/analysis/ordinal_logistic_regression/data_15th.csv')

repeats = data[data['author_count'] > 2]
data.to_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/analysis/ordinal_logistic_regression/repeats_data_15th.csv')

small_data = data[['score'] < 12]
x100 = repeats[repeats['rank'] < 30] # 64211
x = x100[x100['rank'] > -30] # 
plt.hist(x['rank'], bins=9)
plt.title("Histogram of Comment Ranks")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.show()