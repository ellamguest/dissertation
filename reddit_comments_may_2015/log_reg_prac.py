# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:59:07 2016

@author: emg
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from variable_manipulation import df
from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
df = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/ass_reddit_comments_may_2015/practice_5_25.csv')

# make subreddits numeric
df['subreddit'] = pd.to_numeric(df['subreddit'], errors='coerce') # doesn't work
subnums = {"N/A":0.0 ,"AskSocialScience":1.0,"AskStatistics":2.0} 
df['sub_num'] = df['subreddit'].apply(subnums.get)

prac = df.loc[:,['mod','score', 'sub_num']]
prac = df.loc[:,['mod','score', 'subreddit']]

lreg1 = smf.logit(formula = 'mod ~ sub_num', data = df).fit()
print lreg1.summary()