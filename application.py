from flask import Flask, render_template
from textblob import TextBlob
import tweepy

app = Flask(__name__)

@app.route("/")
def fun():
	consumerKey = 'QBz9j6TvF7aEGWsLvVU2nxaGv'
	consumerSecret = '2jxrkIDox6DdktWloiUk9vQzv1Tty9dmz0BakivPgryB2fxUuI'
	accessToken = '379580689-xg4a9dT5PvVMqHgAjArs5N3s6WLLJnXS5IC2QjRB'
	accessTokenSecret = 'ZYYon4XxjE99gUnyx1xeVZ1NZIG5dhI8xc8y8I7Hr6GzR'

	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessTokenSecret)

	api = tweepy.API(auth)

	tweets = api.search("machine learning")
	
	t = dict()
	
	for item in tweets:
		tweet = TextBlob(item.text)
		t[tweet[:100]] = round(tweet.sentiment.polarity, 2)
		
	return render_template("sentiAnalyze.html", t_dict = t)
	
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)
