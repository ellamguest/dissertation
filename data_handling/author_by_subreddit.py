# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:47:58 2016

@author: emg
"""

import pandas as pd
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv')

names = df[['subreddit', 'author']]
names = names[names.author != '[deleted]']
names['count'] = 1
names = names.groupby(['author', 'subreddit']).count()

count_order = names.sort('count', ascending=False)

name_order = names.sort()

author_subs = df.groupby('author').subreddit.nunique()
author_subs.sort(ascending=False)

author_subs.value_counts()
''' 1     20535
2       962
3        90
4        12
12        1
6         1
5         1'''

multi_subs = author_subs[author_subs > 1]
# 1067 of 21602 authors post in more than 1 subreddit

