# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:04:50 2016

@author: emg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', header=0)
stats_df = stats_df.sort('comments')

# sort subreddits by comment count
stats_df.sort('comments').plot(x='subreddit', y='comments', kind='barh', sort_columns=True, legend=False)
mods = stats_df[stats_df.mods > 0]
tops = stats_df[stats_df.tops > 0]


def save_barh_plot(data, column, Name):
    '''column and name are strings, Name is capitalised'''
    sub_nums = np.arange(len(data.subreddit))
    plt.barh(sub_nums, data[column])
    plt.yticks(sub_nums, data.subreddit)
    plt.xlabel('{} Count'.format(Name))
    plt.ylabel('Subreddit')
    plt.title('Monthly {} Count by Subreddit'.format(Name))
    plt.gcf().savefig('sub_{}_count.jpg'.format(column), bbox_inches='tight')

# write plots
comments_jpg = save_barh_plot(stats_df, 'comments', 'Comments')
authors_jpg = save_barh_plot(stats_df, 'authors', 'Authors')
mods_jpg = save_barh_plot(mods, 'mods', 'Commenting Moderator')
tops_jpg = save_barh_plot(tops, 'tops', 'Top Comments')

'''contingency tables'''

table = pd.pivot_table(df, values=['top', 'not_top'], index=['mod', 'not_mod'], aggfunc=np.sum)



