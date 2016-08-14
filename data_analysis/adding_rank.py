# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:52:56 2016

@author: emg
"""
import statsmodels.formula.api as smf

df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/botfree_notdel_comment_data.csv', index_col=0)
stats_df = pd.read_csv('/Users/emg/Programmming/GitHub/dissertation/data_handling/sub_stats.csv', index_col=0)

df = df.reset_index()
df['rank'] = df.groupby('author')['created_utc'].rank()
df = df.sort(['author', 'rank'])

subs = list(stats_df.index)
del_rates = list(stats_df['del_rate'])
df['del_rates'] = df['subreddit']
df['del_rates'] = df.del_rates.replace(subs, del_rates)
df['log_del_rate'] = np.log(df['del_rates'])

df['nontop'] = (df['top'] - 1) * -1
mods = df[df['mod'] == 1]

h1b2 = smf.logit(formula='nontop ~ author_count + rank', data=mods).fit()
print(h1b2.summary())