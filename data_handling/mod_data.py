# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:19:01 2016

@author: emg
"""
import pandas as pd
from subreddits_subsets import d

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/dummied_data.csv')

sub_list = ['AskAcademia', 'AskAnthropology', 'AskComputerScience',
       'AskElectronics', 'AskEngineers', 'AskHistorians',
       'AskLiteraryStudies', 'AskPhotography', 'AskSocialScience',
       'AskStatistics', 'askphilosophy', 'askscience']
       
all_mods = df[df.distinguished=='moderator']   

mod_subs = list(all_mods.subreddit.unique())

''' subreddits with mods are:
    ['AskAnthropology',
 'AskElectronics',
 'AskEngineers',
 'AskHistorians',
 'AskPhotography',
 'AskSocialScience',
 'askphilosophy',
 'askscience'] '''
 
''' subreddits WITHOUT mod comments:
['AskComputerScience', 'AskAcademia', 'AskLiteraryStudies', 'AskStatistics']'''


