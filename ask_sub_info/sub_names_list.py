import numpy as np

# force Rodeo to change cwd
os.chdir('/Users/emg/Programmming/GitHub/dissertation/ask_sub_info')

# RUN OAUTH_TEST TO AUTHORISE FIRST

# get subscribed subreddit list object
subreddits = r.get_my_subreddits()
subs = list(r.get_my_subreddits())


# make list of subscribed subreddit names
sub_names = list()
for i in range(len(subs)):
    sub_names.append(subs[i].display_name + '\n')


# quickly check list
len(subs), len(sub_names)

# export list to file
file = open("sub_names_list.txt", "w")
file.writelines(sub_names)
file.close()

# import list from file
file = open("sub_names_list.txt", "r")
test = file.readlines()

