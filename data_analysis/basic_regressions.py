# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:19:26 2016

@author: emg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm

stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', header=0)
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']
sample = df[df['subreddit']=='AskAnthropology']



lreg1 = smf.logit(formula='top ~ score * mod + C(subreddit)', data=sample).fit()
print(lreg1.summary())

glm = sm.GLM(stats_df['tops'], stats_df['mods']).fit()
result = glm.summary()
result

lin = smf.glm(formula='score ~ top + mod', data=df).fit()
s = lin.summary()
open('test.csv', 'w+').write(s.as_csv())

# H1A: Redditors who post more will have higher average scores.
# num comments = average score


authors = df.drop_duplicates('author')[['author']]
authors = authors.set_index('author')
authors['avg_score'] = df.groupby('author')['score'].mean()
authors['num_comments'] = df.groupby('author')['count'].sum()

# looking at only repeat authors
singles = authors[authors['num_comments'] == 1]
two = authors[authors['num_comments'] == 2]
more = authors[authors['num_comments'] > 2]
limit = more[more['num_comments'] < 300]
limit.plot(x='num_comments', y='avg_score', kind='scatter')
upto20 = author[authors['num_comments'] < 21]
limitscore = upto20[upto20['avg_score'] < 2000]
limitscore.plot(x='num_comments', y='avg_score', kind='scatter')

h1a = smf.glm(formula='num_comments ~ avg_score', data=upto20).fit()
print(h1a.summary())

h1a = smf.glm(formula='avg_score ~ num_comments', data=upto20).fit()
x = h1a.summary()
x = x.as_csv()
f = open('h1a_results.csv', 'w')
f.write(x)
f.close()


# H1C2 Moderators will post more highly

authors = df.drop_duplicates('author')[['author', 'mod']]
authors = authors.set_index('author')
authors['avg_score'] = df.groupby('author')['score'].mean()
authors = authors.ix[1:]  # remove '#NAME?'

h1c2 = smf.logit(formula='mod ~ avg_score', data=authors).fit()
print(h1c2.summary())