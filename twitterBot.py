import tweepy

# authentification to twitter
auth = tweepy.OAuthHandler("55dyMWbOG6SFCm0Kc4i3Z0a4I",
                           "YSuRnkT9rGzTmUmPLdh3kV4AZC3tyPzvfi5pOKMomMDOdq3Bol")
auth.set_access_token("1449717937590444038-TZ3jDileLZP1oLQ9bxeKEl1JDOS9cU",
                      "1UHmtDetn0lgL31qh6J0mem7CUrDgo3FN3dUm73Lk3w3C")

# api object
api = tweepy.API(auth)

# test authentification
try:
    api.verify_credentials()
    print("auth test successful")

except:
    print("error during auth")

# print recent tweets
# my permit is read only why cant i read?
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# test tweet, also doesnt work (i guess permit denied)
api.update_status("Test tweet from Tweepy Python")