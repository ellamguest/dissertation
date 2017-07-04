# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:45:44 2016

@author: emg
"""

import pandas as pd
from datetime import datetime
import os
os.chdir('/Users/emg/Programmming/GitHub/reddit_comments_may_2015')

df = pd.read_csv('ass_may_2015_comments_full.csv')

df['timestamp'] = pd.to_datetime(df['created_utc'], unit='s')

# df = df[df['author'] != '[deleted]'] # remove deleted comments

df = df.sort('created_utc') # sort chronologically

df.to_csv('ass_may_2015_comments_full.csv', encoding= 'utf-8', index=False)

df['parent_id'] = df.parent_id.apply(lambda x: x[3:])

test = df[['created_utc', 'id', 'author', 'parent_id']]






