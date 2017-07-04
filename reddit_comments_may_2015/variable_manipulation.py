import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_csv('/Users/emg/Google Drive/MSc SRMS/MSc Disseration/ass_reddit_comments_may_2015/practice_5_25.csv')
df.head()

# ADD AUTHOR COMMENT COUNT VARIABLE  
df['count'] = df.groupby('author')['author'].transform('count')
df.to_csv('count_data.csv')

# SUBSET REPEATS AND ONE-OFF COMMENTERS
repeats = df[df['count'] > 1]
singles = df[df['count'] == 1]
singles.shape # = 428 rows, correct number of one-off commenters

# SUBSET BY SUBREDDIT
ass = df.query('subreddit == "AskSocialScience"')
stats = df.query('subreddit == "AskStatistics"')

# GET HISTOGRAM OF DAILY COMMENT COUNTS OF SUBREDDIT, how to add titles?
ass_hist = ass.hist(column='days', bins=31)
stats_hist = stats.hist(column='days', bins=31)


# GET SUMMARY DATASET FOR UNIQUE AUTHORS, 785
df['count'] = df.groupby('author')['author'].transform('count') # where function issuses starts
sumscore = df.groupby('author')['score'].transform('sum') # also function issue
grouped = df.groupby('author')
sumscore = grouped.score.sum()
df['cum_score'] = sumscoredf.
uniques = df.drop_duplicates(subset='author')
test = uniques[['author', 'count', 'cum_score', 'mod']]
uniques.merge(test, sumscore, on='author') # not working

# andy's work
counts = df.author.value_counts() 
sums = df.groupby('author').score.sum() 
result = pd.concat([counts, sums], 1)
result.columns = ['count', 'sum']

result.plot(kind='scatter', x='sum',y='count')

