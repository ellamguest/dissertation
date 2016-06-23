# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:57:50 2016

@author: emg
"""

import pandas as pd

df1 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub1.csv')
df2 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub2.csv')
df3 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub3.csv')
df4 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub4.csv')
df5 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub5.csv')
df6 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub6.csv')
df7 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub7.csv')
df8 = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/data/BigQuery/full_comments/2016_04_subsets/sub8.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8])
