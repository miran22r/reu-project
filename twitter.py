from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import json

ckey = 'HpYbmOyVaDs222n8yMNJw9vBk' 
csecret = '74tKYGJA9xNeNAqxLQolZd5aojvdLQIVdTqoQsV9wUXZV4IE6P'
atoken = '2609717065-TYNaKhGlzO3tNTZ3Uqn2Mvfu1bFOv7l1InfVaVc'
asecret = 'MSJtXJKNsLS8xS00KIQ6JEE8dUrJUf7FUJnjsYczCqugs'
tweets = []

class StdOutListener(StreamListener):
	
	fileName = open("test.txt", "w")

	def on_data(self, data):
		global fileName
		decoded = json.loads(data)
		self.fileName.write("#")
		self.fileName.write(decoded[u'user'][u'screen_name'])
		self.fileName.write(decoded[u'user'][u'followers_count'])
		self.fileName.write(decoded[u'user'][u'created_at'])
		self.fileName.write(decoded[u'user'][u'location'])
		self.fileName.write(decoded[u'text'])
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	stream = Stream(auth,l)

	#topic filter
	stream.filter(track=['McDonalds, big mac'])

	#location filter
	stream.filter(locations= '-122.75, 36.8, -121.75, 37.8')
	
	#language filter
	stream.filter(language='en')
