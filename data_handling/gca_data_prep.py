# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:29:05 2016

@author: emg
"""

import pandas as pd

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[['created_utc', 'id', 'author', 'subreddit', 'score']]
df = df.reset_index()
df['rank'] = df.groupby('author')['created_utc'].rank()
df = df.sort(['author', 'rank'])
df.to_csv('ranked_data.csv')

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/ranked_data.csv', index_col=0)
df = df[df['author'] != '[deleted]']
df = df[df['author'] != '#NAME?']

repeats = df[df.duplicated('author',keep=False)]
repeats.to_csv('ranked_repeats.csv')