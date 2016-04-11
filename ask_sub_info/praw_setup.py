import praw

r = praw.Reddit(user_agent="test by /u/why_ask_reddit")
n1 = 'AskSocialScience'
s1 = r.get_subreddit(n1)

