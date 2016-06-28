# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:04:34 2016

@author: emg
"""
'''fetching current moderators'''
import praw
import pandas as pd
stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', header=0)

r = praw.Reddit(user_agent="test by /u/wednesdaysguest")
name = 'AskSocialScience'
sub = r.get_subreddit(name)

names = ['AskAcademia',
 'AskAnthropology',
 'AskComputerScience',
 'AskElectronics',
 'AskEngineers',
 'AskHistorians',
 'AskLiteraryStudies',
 'AskPhotography',
 'AskSocialScience',
 'AskStatistics',
 'askphilosophy',
 'askscience']

'''getting all mods as of june 2016, not nec those during time point'''
mod_dict = {}
for x in names:
    sub = r.get_subreddit(x)
    mods = list(sub.get_moderators())
    n = []
    for y in mods:
        n.append(y.name)
    n.append(len(n))
    mod_dict[x] = n

mod_nums = {}
for x in mod_dict.keys():
    mod_nums[x] = mod_dict[x][-1]

stats_df['mod_comments'] = stats_df['mods']

newdf = pd.DataFrame()
newdf['subreddit'] = mod_nums.keys()
newdf['mods'] = mod_nums.values()
stats_df['mods'] = newdf['mods']

cols = ['subreddit',
 'comments',
 'authors',
 'mods',
 'mod_comments',
 'tops',
 'del_rate',
 'avg_score']
 
stats_df = stats_df[cols]

stats_df.to_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv')

