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

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)

d_stats = {}
for x in list(df.subreddit.unique()):
    data = df[df.subreddit==x]
    n_authors = len(data.drop_duplicates(subset='author'))
    n_mods = data.drop_duplicates('author')['mod'].sum()
    n_mod_comments = data['mod'].sum()
    n_tops = data['top'].sum()
    del_rate = float(len(data[data['author']=='[deleted]']))/float(len(data))
    avg_score = data['score'].mean()
    d_stats[x] = [len(data), n_authors, n_mods, n_mod_comments, n_tops, del_rate, avg_score]

stats_df = pd.DataFrame.from_dict(d_stats) 
stats_df = stats_df.T
stats_df.index.name = 'subreddit'
stats_df.columns = ['comments', 'authors', 'mods', 'mod_comments', 'tops', 'del_rate', 'avg_score']            
stats_df = stats_df.reindex(sorted(stats_df.index, key=lambda x: x.lower()))
stats_df.to_csv('sub_stats.csv')