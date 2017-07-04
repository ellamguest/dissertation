# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:02:20 2016

@author: emg
"""
import sqlite3
import pandas as pd

# Establish connection to SQL database
sql_conn = sqlite3.connect('/Volumes/PENDRIVE/Programming/reddit_may_2015_comments/database.sqlite')
c = sql_conn.cursor()

# Select target subreddits
sub = ('AskSocialScience',)

# Get * (all fields) from target subreddits
c.execute("SELECT * FROM May2015 WHERE subreddit=?", sub)

# Create list and pd database of fetched comments
comments = c.fetchall() # created_utc, author

columns = [ 'created_utc', 'ups', 'subreddit_id', 'link_id', 'name',
           'score_hidden', 'author_flair_css_class', 'author_flair_text',
           'subreddit', 'id', 'removal_reason', 'gilded', 'downs',
           'archived', 'author', 'score', 'retrieved_on', 'body', 
           'distinguished', 'edited',' controversiality', 'parent_id']
comment_df = pd.DataFrame(comments, columns=columns)
comment_df['timestamp'] = pd.to_datetime(comment_df['created_utc'], unit='s')


# Save database to csv
comment_df.to_csv('ass_may_2015_comments_full.csv', encoding= 'utf-8', index=False)

#c.close()