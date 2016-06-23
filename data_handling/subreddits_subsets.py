# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:04:19 2016

@author: emg
"""
import pandas as pd

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/dummied_data.csv')

sub_list = ['AskAcademia', 'AskAnthropology', 'AskComputerScience',
       'AskElectronics', 'AskEngineers', 'AskHistorians',
       'AskLiteraryStudies', 'AskPhotography', 'AskSocialScience',
       'AskStatistics', 'askphilosophy', 'askscience']

 
ass = df[df.subreddit == 'AskSocialScience']

def name(n):


# create dictionary of subreddit data subset
d = {}
subnames = df.subreddit.unique()
for n in range(len(subnames)):
    d['{}'.format(subnames[n].lower())] = df[df.subreddit==subnames[n]]
    
''' d keys = ['askcomputerscience',
 'askacademia',
 'askhistorians',
 'askscience',
 'askphotography',
 'askphilosophy',
 'asksocialscience',
 'askelectronics',
 'askstatistics',
 'askanthropology',
 'askengineers',
 'askliterarystudies']'''