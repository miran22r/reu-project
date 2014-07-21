from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import json

ckey =  'rBXniNxKspuvBsvYnou6co2Ot'
csecret = '77hcyMa73lBDdi9y3bQhaIBQrSLuiB4U29WxCfFa3zw0bebska'
atoken = '2609717065-TYNaKhGlzO3tNTZ3Uqn2Mvfu1bFOv7l1InfVaVc'
asecret = 'MSJtXJKNsLS8xS00KIQ6JEE8dUrJUf7FUJnjsYczCqugs'
tweets = []

class StdOutListener(StreamListener):
	

	def on_data(self, data):
		self.fileName = open("test.txt", "a")
		decoded = json.loads(data)
		self.fileName.write("#")
		self.fileName.write(decoded[u'user'][u'screen_name'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.write(str(decoded[u'user'][u'followers_count']))
		self.fileName.write("\n")
		self.fileName.write(decoded[u'user'][u'created_at'])
		self.fileName.write("\n")
		self.fileName.write(decoded[u'user'][u'location'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		self.fileName.write(decoded[u'text'].encode('ascii', 'ignore'))
		self.fileName.write("\n")
		print decoded[u'user'][u'location']
		print decoded[u'text']
		print "\n"
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
	stream.filter(track=['$YHOO, yahoo!, Yahoo!, AdInterax, Flickr, Rivals.com, Yahoo! Advertising, Yahoo! Answers, Yahoo! Autos, Yahoo! Developer Network, Yahoo! Directory, Yahoo! Family Accounts, Yahoo! Finance, Yahoo! GeoPlanet, Yahoo! Green, Yahoo! Groups, Yahoo! Local, Yahoo! Mail, Yahoo! Maps, Yahoo! Messenger, Yahoo! Mobile, Yahoo! Movies, Yahoo! Music, Yahoo! News, Yahoo! OMG, Yahoo! Originals, Yahoo! Parental Controls, Yahoo! Pipes, Yahoo! Real Estate, Yahoo! Research, Yahoo! Search, Yahoo! Search Marketing, Yahoo! Security Center, Yahoo! Shopping, Yahoo! Small Business, Yahoo! Smush.it, Yahoo! Sports, Yahoo! Travel, Yahoo! TV, Yahoo! Screen, Yahoo! Voices'])

	#location filter
	stream.filter(locations=[-74.2591,40.496,-73.7003,40.9153, -118.6682,33.7037,-118.1553,34.3373, -87.9403,41.6443,-87.524,42.0231, -95.7881,29.5236,-95.0145,30.1107, -77.119759,38.791645,-76.909393,38.995548])


	#language filter
	stream.filter(language=en)
