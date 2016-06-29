# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:47:58 2016

@author: emg
"""

import pandas as pd
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv')

''''count of subreddits by author '''
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

''' counts of comments by author ''''

counts = df[['subreddit', 'author']]
counts = counts[counts.author != '[deleted]']
counts['count'] = 1
counts = counts.groupby(['author']).count()
author_comment_counts = counts.groupby(['count']).count()

'''' D-Juice commented in 6 subs, TotesMessenger commented in 5''''

djuice = df.loc[df.author == 'D-Juice']
djuice_subs = list(djuice.subreddit.unique())

totes = df.loc[df.author == 'TotesMessenger']
totes_subs = list(totes.subreddit.unique())

