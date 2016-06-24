# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:58:17 2016

@author: emg
"""

import praw
from praw_setup import *

subreddit = r.get_subreddit(name)
controv = subreddit.get_controversial_from_all()