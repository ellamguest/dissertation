# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:03:50 2016

@author: emg
"""

import pandas
from scipy.stats import ttest_ind
import statsmodels.formula.api as smf
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']
df['count'] = 1

# H1B1 Top level comments will be more common

tops = df[df['top'] == 1]
nontops = df[df['top'] == 0]

sub_top_counts = tops.groupby('subreddit')['count'].sum().to_frame()
sub_top_counts['nontops'] = nontops.groupby('subreddit')['count'].sum().to_frame()
sub_top_counts['diff'] = sub_top_counts['count'] - sub_top_counts['nontops']

ttest_ind(sub_top_counts['count'], sub_top_counts['nontops'])
# = (0.97051307083494409, 0.3423407952851889)

# H1B2  Top level comments will score more highly than non-top level comments

# top = score (+ mod)
h1b2 = smf.logit(formula='top ~ score + mod', data=df).fit()
print(h1b2.summary())

# or should it be score = top (+ mod)?

h1b2lin = smf.glm(formula='score ~ top*mod', data=df).fit()
print(h1b2lin.summary())

