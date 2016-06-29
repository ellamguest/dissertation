# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:04:34 2016

@author: emg
"""
'''fetching current moderators'''
import praw
import pandas as pd
stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', header=0, index_col=0)


r = praw.Reddit(user_agent="test by /u/wednesdaysguest")
name = 'AskSocialScience'

names = list(stats_df.subreddit.get_values())

'''getting all mods as of june 2016, not nec those during time point'''
mod_dict = {}
for x in names:
    sub = r.get_subreddit(x)
    mods = list(sub.get_moderators())
    n = []
    for y in mods:
        n.append(y.name)
    mod_dict[x] = n

mod_nums = {}
for x in mod_dict.keys():
    mod_nums[x] = len(mod_dict[x])



newdf = pd.DataFrame()
newdf['subreddit'] = mod_nums.keys()
newdf['mods'] = mod_nums.values()
newdf['names'] = mod_dict.values()
newdf = newdf.sort('subreddit')
newdf = newdf.reset_index(drop=True)
stats_df['mods'] = newdf['mods']
stats_df['mod_names'] = newdf['names']

cols = ['subreddit',
 'comments',
 'authors',
 'mods',
 'mod_comments',
 'tops',
 'del_rate',
 'avg_score',
 'mod_names']
 
stats_df = stats_df[cols]

stats_df.to_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv')

