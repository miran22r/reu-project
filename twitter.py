from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import json

ckey = 'jNBDXt5xoNZPe0q9OTFnBp8QE' 
csecret = 'rdVfwFZ8TuJaSIXdwtUhgejsaiTYzWKmGfy2983ag3Q608IjQf'
atoken = '53131213-razXndX0qMOEW4ZGYcQqdqxM4yvf4TCAlSNIKwzmX'
asecret = 'RXUrmSxbNHaqg7o0hwWYIimsVnHI4cTpkEAJ2wbD6BK2L'
tweets = []

class StdOutListener(StreamListener):


	def on_data(self, data):
		self.fileName = open("test.txt", "a")

		decoded = json.loads(data)
		self.fileName.write("\n")
		self.fileName.write(decoded[u'user'][u'screen_name'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.write(str(decoded[u'user'][u'followers_count']))
		self.fileName.write("\n")		
		self.fileName.write(decoded[u'user'][u'created_at'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.write(decoded[u'user'][u'location'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.write(decoded[u'text'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.close()
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	stream = Stream(auth,l)

	#topic filter
	stream.filter(track=['$SBUX,Starbucks,Starbucks coffee,Latte,Vanilla Latte,Mocha,White Mocha,Caramel Machiatto,Camramel Frappuccino,Mocha Frappuccino,Frappuccino,Frap,Four bucks,starbuck'])

	#location filter
	stream.filter(locations= '-74.2591,40.496,-73.7003,40.9153, -118.6682,33.7037,-118.1553,34.3373,-87.9403,41.6443,-87.524,42.0231,-95.7881,29.5236,-95.0145,30.1107,-77.119759,38.791645,-76.909393,38.995548')

	#language filter
	stream.filter(language='en')
