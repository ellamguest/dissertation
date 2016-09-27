# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:29:05 2016

@author: emg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/analysis/ordinal_logistic_regression/pred_rs.csv')

df = df[df['cons.(<=neg)']==1]

sample = df.author_long.sample(100)
sample = df[df.author_long.isin(sample)]

sample2 = df.author_long.sample(100)
sample2 = df[df.author_long.isin(sample2)]

sample3 = df.author_long.sample(100)
sample3 = df[df.author_long.isin(sample3)]

sample4 = df.author_long.sample(100)
sample4 = df[df.author_long.isin(sample4)]

s = sample.author_long
sample.plot(x='rank.12',y='pred_rs', kind='scatter', color=s)


df.plot(x='rank.12',y='pred_rs', kind='scatter')

plt.hist(x['rank'], bins=range(3,21,1))
plt.title("Histogram of Author Comment Count")
plt.xlabel("Comment Count")
plt.ylabel("Frequency")
plt.show()

plt.scatter(x=df['rank.12'], y=df['pred_rs'])
plt.scatter(x=df['rank.12'], y=df['pred_rs'], marker='o')
plt.scatter(x=df['rank.12'], y=df['pred_rs'], marker='.')

q = sample
plt.scatter(x=q['rank.12'], y=q['pred_rs'], marker='.',c=q['top.12'])
plt.title("Plot of Predicted Log-Odds of Comment Having a 'Negative' Score by Comment Rank")
plt.xlabel("Comment Rank")
plt.ylabel("Predicted Log-Odds of 'Negative' Score")
plt.figure(figsize=(10,30))

def plot(sample):
    plt.scatter(x=sample['rank.12'], y=sample['pred_rs'], marker='.',c='c')
    plt.xlabel("Comment Rank")
    plt.ylabel("Predicted Log-Odds of 'Negative' Score")
    plt.show()