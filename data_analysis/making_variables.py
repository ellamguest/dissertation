# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:55:36 2016

@author: emg
"""

df['mod'] = df.distinguished.apply(lambda x: (1 if x == 'moderator' else 0))
# OR
df['mod'] = pd.get_dummies(df['distinguished'])