# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:42:36 2016

@author: emg
"""

import pandas as pd

df = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/analysis/ordinal_logistic_regression/data_17.csv')
df['score_level_num'] = df.score_level.replace(['high','low','neg'],[1,2,3])
df['score_level_num_rev'] = df.score_level.replace(['high','low','neg'],[3,2,1])
df.to_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/analysis/ordinal_logistic_regression/data_18.csv',index=None)

df = df.sort_values('rank')