# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:04:19 2016

@author: emg
"""
import pandas as pd
import numpy as np
from __future__ import division
from mod_data import sub_mods
from top_data import sub_tops

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv', index_col=0)

sub_list = ['AskAcademia', 'AskAnthropology', 'AskComputerScience',
       'AskElectronics', 'AskEngineers', 'AskHistorians',
       'AskLiteraryStudies', 'AskPhotography', 'AskSocialScience',
       'AskStatistics', 'askphilosophy', 'askscience']


# create dictionary of subreddit data subset
d = {}
subnames = df.subreddit.unique()
for n in range(len(subnames)):
    d['{}'.format(subnames[n].lower())] = df[df.subreddit==subnames[n]]


    
''' d keys = ['askcomputerscience',
 'askacademia',
 'askhistorians',
 'askscience',
 'askphotography',
 'askphilosophy',
 'asksocialscience',
 'askelectronics',
 'askstatistics',
 'askanthropology',
 'askengineers',
 'askliterarystudies']'''
 
 '''create subreddit dict of tuples:
 subreddit: (N comments, N authors, N mods, deletion rate, avg score)'''

d_stats = {}
for x in subnames:
    name = x
    data = df[df.subreddit==x]
    sums = data.sum()
    n_authors = len(data.drop_duplicates(subset='author'))
    n_mods = float(sums['mod'])
    n_tops = float(sums['top'])
    del_rate = len(data[data.author=='[deleted]'])/len(data)
    avg_score = data.mean()['score']
    d_stats[name] = [len(data), n_authors, n_mods, n_tops, del_rate, avg_score]

# 0=N comments, 1=N authors, 2=N mods, 3=N tops, 4=del rate, 5=avg score 

stats_df = pd.DataFrame.from_dict(d_stats) 
stats_df = stats_df.T
stats_df.index.name = 'subreddit'
stats_df.columns = ['comments', 'authors', 'mods', 'tops', 'del_rate', 'avg_score']            
stats_df.to_csv('sub_stats.csv')

d_stats = {}
for x in subnames:
    name = x
    data = d['{}'.format(name.lower())]
    n_authors = len(data.drop_duplicates(subset='author'))
    if x in sub_mods.subreddit:
        n_mods = int(sub_mods.mod_count[sub_mods.subreddit==x])
    else
    n_tops = int(sub_tops.top_count[sub_tops.subreddit==x])
    del_rate = len(data[data.author=='[deleted]'])/len(data)
    avg_score = data.mean()['score']
    d_stats[name] = [len(data), n_authors, n_mods, n_tops, del_rate, avg_score]

'''' getting top*mod ''''

df['top_mod'] = df['mod'] * df['top'] # 498

tops = df.top.sum() # 60522
mod_commentss = df['mod'].sum() # 5151
top_mod_comments = df.top_mod.sum() # 498