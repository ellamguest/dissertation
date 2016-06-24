# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:19:26 2016

@author: emg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm

stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', header=0)

lreg1 = smf.logit(formula='mods ~ comments', data=stats_df).fit()

glm = sm.GLM(stats_df['tops'], stats_df['mods']).fit()
result = glm.summary()
result