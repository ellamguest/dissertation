import praw
import numpy as np
import pandas as pd
from datetime import datetime

#### RUN OAUTH_TEST TO AUTHORISE FIRST

# import list from file (see sub_names_list)
names = [l.strip() for l in
open("sub_names_list.txt")]

'''' LIST OF INTERESTING SUBREDDIT OBJECT ATTRIBUTES:
[created, created_utc, description, display_name, name, over18, 
public_description, public_traffic, subreddit_type]
''''

# dump sub_info into pandas dataframe + export to csv
df = pd.DataFrame(columns=['created', 'subscribers', 'public_description'], index=names)
for name in names:
    print 'getting' + name
    sub = r.get_subreddit(name)
    df.loc[name] = [datetime.date(datetime.fromtimestamp(sub.created_utc)),
                        sub.subscribers,
                        sub.public_description]
df.to_csv('sub_info.csv')

test = r.get_subreddit('AskSocialScience')
time = test.created_utc

x = datetime.fromtimestamp(time)
datetime.date(x)
time
itime = int(time)
ix = datetime.fromtimestamp(time)
datetime.date(ix)
######################################### OLD SCRIPT ########################################
# dump sub_info into empty numpy stacked array
num_rows = len(names) # set number of rows needed
sub_info = np.empty(shape=(num_rows,4), dtype='S20') # create empty np.array
for i in range(0,num_rows):
    print names[i]
    sub = r.get_subreddit(names[i])
    sub_info[i] = np.array([sub.display_name, sub.created_utc, sub.subreddit_type, sub.subscribers])

# convert into pandas dataframe and export to csv ***TRY PD INSTEAD OF NP FROM START***
header = ['NAME', 'CREATED_UTC', 'SUBSCRIBERS', 'PUBLIC_DESCRIPTION']
df = pd.DataFrame(sub_info, columns=header)
df.to_csv('sub_info.csv')
