# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:28:13 2016

@author: emg
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/ranked_data.csv', index_col=0)

sample = df[df['subreddit']=='AskAnthropology']

md = smf.mixedlm('score ~ rank', df, groups=df['author'], re_formula='~rank')

mdf = md.fit()

print(mdf.summary())