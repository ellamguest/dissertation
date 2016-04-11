import praw
from login import *
from PRAW_OAuth2_Test import client_id, client_secret, redirect_uri

# CREATE R OBJECT W/ CLEAR USERAGENT
r = praw.Reddit('OAuth testing example by u/why_ask_reddit ver 0.1 see '
                 'https://praw.readthedocs.org/en/latest/'
                 'pages/oauth.html for source')

# SET APP INFO
r.set_oauth_app_info(client_id = client_id,
                    client_secret = client_secret,
                    redirect_uri = redirect_uri)

scope = 'history identity mysubreddits' 
# REQUEST AUTHORISATION FROM USER
# SCOPE DEFINES WHAT INFO WILL BE AUTHOIRSED TO ACCESS, DEFINE ABOVE
url = r.get_authorize_url('uniqueKey', scope, True)
import webbrowser
webbrowser.open(url)

# EXCHANGE CODE FOR ACCESS INFORMATION
access_information = r.get_access_information('KxgzosRSREHHD7TLZ3MDWVP_W-o')

# TO REFRESH TOKEN AFTER 60 MINUTES
# r.refresh_access_information(access_information['refresh_token'])

# CHECK ACCESS
authenticated_user = r.get_me()
print authenticated_user.name, authenticated_user.link_karma

from login import *



