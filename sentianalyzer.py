from textblob import TextBlob
import tweepy

consumerKey = 'QBz9j6TvF7aEGWsLvVU2nxaGv'
consumerSecret = '2jxrkIDox6DdktWloiUk9vQzv1Tty9dmz0BakivPgryB2fxUuI'
accessToken = '379580689-xg4a9dT5PvVMqHgAjArs5N3s6WLLJnXS5IC2QjRB'
accessTokenSecret = 'ZYYon4XxjE99gUnyx1xeVZ1NZIG5dhI8xc8y8I7Hr6GzR'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

tweets = api.search("machine learning")

for item in tweets:
	tweet = TextBlob(item.text)
	if tweet.sentiment.polarity > 0:
		print("Positive Tweet")
	elif tweet.sentiment.polarity < 0:
		print("Negative Tweet")
	else:
		print("Neutral Tweet")
	print("\n"+str(tweet))
	print(" - - - - - - - - - - \n")