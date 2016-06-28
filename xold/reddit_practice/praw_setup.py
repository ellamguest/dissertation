# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:46:33 2016

@author: emg
"""

import praw

r = praw.Reddit(user_agent="test by /u/wednesdaysguest")
name = 'AskSocialScience'
sub = r.get_subreddit(name)

names = ['AskAcademia',
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
 'askscience']

mods = {}
for x in names:
    sub = r.get_subreddit(x)
    mods = sub.get_