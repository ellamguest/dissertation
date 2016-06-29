# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:40:59 2016

@author: emg
"""

import pandas as pd

'''' compiled post data:
df1 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_posts/reddit_posts_2016_04/results-20160627-123923.csv')
df2 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_posts/reddit_posts_2016_04/results-20160627-124040.csv')
posts = df1.append(df2).sort('created_utc')
posts.to_csv('2016_04_full_posts.csv')''''

posts = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/2016_04_full_posts.csv')
comments = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/practice_data.csv')

post_ids = posts.id.head() # 20945
parent_ids = comments.p_id
'4csu0y' in post_ids.get_values()

for x in post_ids:
    if x in posts.id.get_values():
        print x
        
parent_ids = comments.p_id # 98294

'''parent_ids start with 3,4,c,d - subset:'''
# get 'parent_ids' starting w/ 4
fours = [] 
for x in parent_ids:
    if x[0] == '4':
        fours.append(x)
        
len(fours) # 37718 = 0.38 of all p_ids
fours = list(set(fours)) # get unique values, 14656

cs = [] 
for x in parent_ids:
    if x[0] == 'c':
        cs.append(x)
        
cs = list(set(cs)) # 80

ds = [] 
for x in parent_ids:
    if x[0] == 'd':
        ds.append(x)

ds = list(set(ds))
len(ds) # 40055

threes = [] 
for x in parent_ids:
    if x[0] == '3':
        threes.append(x)

threes = list(set(threes)) # 80

len(threes) # 42




'''' if 4 parent id not is post_ids it if left censored, remove ''''
# find parent_ids (starting w/ 4) not in post_ids
missing = []
for x in fours:
    if x not in post_ids.get_values():
        missing.append(x)
        
# get comments with missing parent_ids
parented = df.loc[~df['p_id'].isin(missing)]
len(parentless) # 534
len(parented) # 97760

new_df = parented # only tracing comment parents which aren't censored

''''most parent_ids start with d, these are other comments''''
comments = comments.sort('id')
comment_ids = comments.id
comment_ids.head() # first = d1l5ad6
comment_ids.tail() # last = d2nvhxh

parent_ds = new_df.loc[new_df['id'].isin(ds)]

missing_ds = new_df.loc[~new_df['id'].isin(ds)] # 58321

missing1 = missing_ds.id

''' have to iterate over to go up tree '''

### TRYING TO CLEAN UP

all_comment_ids = comments.id
all_comment_parents = comments.p_id
all_post_ids = posts.id
parent_not_post = all_comment_parents.loc[~all_comment_parents.isin(all_post_ids)]
# len = 61110

''' redo following having removed left censored tops... '''
top_comments = comments[comments.p_level=='t3']
top_comment_parent_ids = top_comments.p_id
top_comment_parent_in_posts = top_comment_parent_ids.loc[top_comment_parent_ids.isin(all_post_ids)]
# len = 37184
parentless_top_comment = top_comment_parent_ids.loc[~top_comment_parent_ids.isin(all_post_ids)]
# 588 tops comments left censored

new_comments1 = comments.loc[~comments.p_id.isin(parentless_top_comment)]

parent_in_comments = parent_not_post.loc[parent_not_post.isin(new_comments1.id)]
# len = 59671 (160 less than inluding left censored tops)

parent_missing = parent_not_post.loc[~parent_not_post.isin(new_comments1.id)]
# len = 1439

def check_time(x_id):
    return comments.loc[comments['id' = x_id]].created_utc
    
parent_missing_comments = comments.loc[comments.p_id.isin(parent_missing)]
parent_missing_comments['date'] = pd.to_datetime(parent_missing_comments.created_utc, unit='s')


'''' attempting again, building new database with confirmed parentage ''''

tops_with_parents = comments.loc[comments['

cols = ['id', 'author', 'subreddit', 'created_utc', 'link_id', 'parent_id', 'p_level', 'p_id']
comments = comments[cols]

links = comments.link_id.str.split('_', expand=True)
comments['link_level'] = links[0]
comments['link_id'] = links[1]