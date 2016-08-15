# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:17:37 2016

@author: emg
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/have_parents.csv', index_col=0)
df = df[df['author'] != '#NAME?']
df = df[df['author'] != 'AutoModerator']
df = df[df['author'] != 'AskScienceModerator']
df['count'] = 1
df.to_csv('botfreedata.csv')

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfreedata.csv', index_col=0)
df = df[df['author'] != '[deleted]']
authors = df.drop_duplicates('author')
authors.to_csv('botfree_author_data.csv')


# author count hist
x = authors[authors['author_count'] < 11]
x = stats_df['del_rate']
plt.hist(mods['author_count'], bins=10)
plt.title("Histogram of Comment Counts of Moderators")
plt.xlabel("Number of Comments Made")
plt.ylabel("Frequency")
plt.show()

#comment score hist
# 64785 (deleted omitted)
# highest = 4267
x100 = df[df['score'] < 20] # 64211
x = x100[x100['score'] > -20] # 64042
#==============================================================================
# plt.hist(x['score'], bins=20)
# plt.title("Histogram of Comment Scores")
# plt.xlabel("Score")
# plt.ylabel("Frequency")
# plt.show()
#==============================================================================
