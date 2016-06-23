# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:06:51 2016

@author: emg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/2016_04.csv')


df['mod'] = pd.get_dummies(df['distinguished']) # does this work

''''list(df.columns) = ['id',
 'author',
 'subreddit',
 'created_utc',
 'link_id',
 'parent_id',
 'score',
 'distinguished',
 'mod']''''
 
comments_by_mods = pd.crosstab(df.subreddit, df.distinguished)
 

# get comment counts by author and subreddit
df['author_count'] = df.groupby('author')['author'].transform('count')
df['subreddit_count'] = df.groupby('subreddit')['subreddit'].transform('count')


# create subsets
subreddits = df.drop_duplicates(subset='subreddit')
subreddits = subreddits.reset_index()
subreddits = subreddits.sort('subreddit_count')

authors = df.drop_duplicates(subset='author')
authors = authors.reset_index()

dels = df[df.author == '[deleted]']



# plot comment count by subreddit
ax = subreddits.plot(kind='bar', x='subreddit', y='subreddit_count', title='Comment Count by Subreddit', legend=False)
ax.set_xlabel('Subreddit')
ax.set_ylabel('Comment Count')
fig = ax.get_figure()
fig.set_figwidth(10)
fig.set_figheight(5)
fig.savefig('sub_comment_count.jpg', dpi=100) # cuts of x labels


authors = pd.DataFrame(pd.value_counts(df['author'].values, sort=True))
authors.reset_index(level=0, inplace=True)
authors.columns = ['author', 'count']
authors = authors[authors.author != '[deleted]'] # remove [deleted]

ax = s.hist()  # s is an instance of Series
fig = ax.get_figure()
fig.savefig('/path/to/figure.pdf')



# top level comment
# parent id t1 = top, t3 = not
# create varaible for t1 or t3
# then convert to binart
p = df.parent_id.str.split('_', expand=True)
df['p_level'] = p[0]
df['p_id'] = p[1]
x = pd.get_dummies(df['p_level'])
df['top'] = x['t1']

df['mod'] = pd.get_dummies(df['distinguished'])

df.to_



