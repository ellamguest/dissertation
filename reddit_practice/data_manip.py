# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:47:31 2016

@author: emg
"""

######################
# MANIPULATING DATA

sr_comments = r.get_comments('AskSocialScience')

def word_list(lines):
    word_list = []
    for x in lines:
        word_list.append(str(x.body).split()) #make list of list of words per comment
    return word_list

def word_dict(word_list):
    d = {}
    for x in word_list:
        for word in x:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d

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
            
            
print rd