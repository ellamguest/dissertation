# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:36:51 2016

@author: emg
"""

import numpy as np
import pandas as pd
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import (Exchangeable,
    Independence,Autoregressive)
from statsmodels.genmod.families import Poisson

fam = Poisson()
ind = Independence()
model1 = GEE.from_formula("author_count ~ top + mod", "author", authors, cov_struct=ind, family=fam)
result1 = model1.fit()
print(result1.summary())