# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:42:22 2016

@author: emg
"""

import pandas as pd
from subreddits_subsets import d

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv')

test = d['askanthropology'] # 990
tops = test[test.p_level=='t1'] # 680
nontops = test[test.p_level=='t3'] # 310


link_ids = test.link_id.str.split('_', expand=True)[1].sort_values()
parent_ids = test.p_id.sort_values()

# check that parent comments in dataset

x = parent_ids.isin(link_ids)


test['p_in_list'] = test.parent_id.isin(test.link_id)
test.sum()['p_in_list'] # 310
# all parent comments started this month
# no need to check parents of tops against posts


test2 = d['askscience']
test2['p_in_list'] = test2.parent_id.isin(test2.link_id)
test2.sum()['p_in_list'] # 16882.0
len(test2[test2.p_level=='t3']) # 16882


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

all_tops = df[df.p_level=='t1']
all_tops['top_count'] = all_tops.groupby('subreddit')['subreddit'].transform('count')
sub_tops = all_tops.drop_duplicates(subset='subreddit')

df['top_count'] = all_tops.top_count

df.to_csv('practice_data.csv')
