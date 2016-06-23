# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:04:19 2016

@author: emg
"""

df = df.sort('subreddit')
'''list(df.subreddit.unique()) =
 'AskAnthropology',
 'AskComputerScience',
 'AskElectronics',
 'AskEngineers',
 'AskHistorians',
 'AskLiteraryStudies',
 'AskPhotography',
 'AskSocialScience',
 'AskStatistics',
 'askphilosophy',
 'askscience']'''
 
ass = df[df.subreddit == 'AskSocialScience']