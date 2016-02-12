# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:31:19 2016

@author: emg
"""

import praw

user_agent = "test by /u/wednesdaysguest"
r = praw.Reddit(user_agent=user_agent)

sr_comments = r.get_comments('poledancing')

comment_list = []
for x in sr_comments:
    comment_list .append(str(x.body).split()) #make list of list of words per comment

d = {}
for x in comment_list:
    for word in x:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

def make_reverse_dict(d):
    '''reverse any dict, accounting for possible multiple values'''
    results = {}
    for k, v in d.iteritems():
        if v in results:
            results[v].append(k)
            results[v] = list(set(results[v]))
        else:
            results[v] = [k]
    return results

rd = make_reverse_dict(d)
            
            
print r

    