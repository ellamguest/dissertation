# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:33:04 2016

@author: emg
"""

import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.formula.api as smf
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']
df = df[df['author'] != 'AutoModerator']
df = df[df['author'] != 'AskScienceModerator']
df['count'] = 1

authors = df.drop_duplicates('author')[['author', 'mod', 'subreddit', 'distinguished']]
authors = authors.set_index('author')
authors['avg_score'] = df.groupby('author')['score'].mean()
authors['num_comments'] = df.groupby('author')['count'].sum()

# mod = num_comments
h1c = smf.logit(formula='mod ~ num_comments', data=authors).fit()
print(h1c.summary())

# num_comments = mod
h1c = smf.glm(formula='num_comments ~ mod + subreddit', data=authors).fit()
#print(h1c.summary())
x = h1c.summary()
x = x.as_csv()
f = open('h1c_results.csv', 'w')
f.write(x)
f.close()

len(authors[authors['mod'] 


mod_comments = df[df['mod'] == 1] # 30
mods = mod_comments.drop_duplicates('author')
mods = mods.sort_values('author')
mods = mods.set_index('author')
mods['author'] = mods.index
x = mod_comments.groupby('author')['count'].sum()
mods['num_comments'] = x
mods = mods.sort_values('num_comments')
mods.plot(x='author',y='num_comments', kind='bar')

nonmod_comments = df[df['mod'] == 0] # 30
nonmods = nonmod_comments.drop_duplicates('author')
nonmods = nonmods.sort_values('author')
nonmods = nonmods.set_index('author')
nonmods['author'] = nonmods.index
x = nonmod_comments.groupby('author')['count'].sum()
nonmods['num_comments'] = x
nonmods = nonmods.sort_values('num_comments')
nonmods.plot(x='author',y='num_comments', kind='scatter')

# x = mods.groupby(['author', 'subreddit'])['count'].sum()
# mods = mods.drop_duplicates(['author', 'subreddit'])[['author', 'subreddit', 'mod', 'count']]
# mods['count'] = x

mods = mods.sort('author')

multimods = mods[mods.duplicated('author') == True]