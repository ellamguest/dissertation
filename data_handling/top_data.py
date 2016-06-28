# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:42:22 2016

@author: emg
"""

import pandas as pd

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv')

link_ids = test.link_id.str.split('_', expand=True)[1].sort_values()
parent_ids = test.p_id.sort_values()

# check that parent comments in dataset

x = parent_ids.isin(link_ids)


df['p_in_list'] = df.parent_id.isin(df.link_id)
df.sum()['p_in_list'] # 310


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
