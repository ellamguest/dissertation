# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:12:50 2016

@author: emg
"""

import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.formula.api as smf
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']
df['count'] = 1


deleted = df[df['author'] == '[deleted]']
notdel =  df[df['author'] != '[deleted]']

subdels = deleted.groupby(['subreddit'])['count'].sum()
subnotdels = notdel.groupby(['subreddit'])['count'].sum()

mods = df[df['mod'] == 1] # 30
mods = mods.sort(['author','subreddit'])
submods = mods.groupby(['subreddit', 'author'])['mod'].sum()


///////
# H2A: Subreddits with more moderators will have higher rates of deletion
# del_rate = mods

stats_df = pd.read_csv('sub_stats.csv', index_col=0)
stats_df.plot(x = 'del_rate', y='mods', kind='scatter')

h2a = smf.glm(formula='del_rate ~ mods', data=stats_df).fit()
print(h2a.summary())

///////
# H2B: Moderators will make more non-top level comments in subreddits with higher deletion rates
# num non-tops = mod + del_rate, moderator level

stats_df = pd.read_csv('sub_stats.csv', index_col=0)
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']
df['count'] = 1
df = df.set_index('subreddit')
df['subreddit'] = df.index
df['del_rate'] = stats_df.del_rate
#df = df.sort(['del_rate', 'author'])
df = df.set_index('author')
df['author'] = df.index
x = df.groupby(['author'])['count'].sum()
df['num_counts'] = x
# df['num_tops'] = df.groupby(['author', 'del_rate'])['top'].sum()
df['top_count'] = df.groupby('author')['top'].sum()
df['nontop'] = (df['top'] - 1) * -1
df['nontop_count'] = df.groupby('author')['nontop'].sum()
mods = df[df['mod'] == 1] # 30
#df['nontops_counts'] = (df.num_counts.T - df.top_count).T


#authors = df.drop_duplicates(['author', 'del_rate'])
#authors['num_comments'] = df.groupby(['author', 'del_rate'])['count'].sum()

mods = mods.drop_duplicates(['author', 'subreddit'])
mods['del_rate100'] = mods['del_rate'] * 100
mods['comment_count'] = mods['top_count'] + mods['nontop_count']
#his = mods[mods['subreddit']=='AskHistorians']

h2b = smf.glm(formula='nontop_count ~ del_rate100', data=mods).fit()
print(h2b.summary())
# x = h2b.summary()
x = x.as_csv()
f = open('h2b_results.csv', 'w')
f.write(x)
f.close()


###### h2b new = chi-square for each subreddit
x = pd.crosstab(index=[df['subreddit'],df['mod']], columns=df['top'])
