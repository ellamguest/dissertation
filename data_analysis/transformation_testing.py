# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:20:25 2016

@author: emg
"""

import pandas as pd
import numpy as np
df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfreedata.csv', index_col=0)

x = df['score']
x = x[x < 101] # 64211
x = x[x > -10] # 64042

sqrt = np.sqrt(x)
plt.hist(sqrt)
plt.title("Histogram of Comment Count by Authors")
plt.xlabel("Comment Count")
plt.ylabel("Frequency")
plt.show()


log = np.log(x +11)    
log.hist()