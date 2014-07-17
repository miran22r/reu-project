# Website scrapper
import json
import requests
import re
from bs4 import BeautifulSoup

#def expression():
    
def pageData(url):
    r = requests.get("http://"+url)
    data = r.text
    soup = BeautifulSoup(data,["lxml", "xml"])

    for link in soup.find_all(class_="json-data", limit=1):
	strLink = str(link)
	init = strLink.index("value") + 7
	final = strLink.index("false}}'>") + 7
	json_data = "[" +strLink[init:final] + "]"
#	json_data = strLink[init:final]	
	print json_data
        data = json.loads(json_data)
	print data
#	data['location']
	print json_data["u'location"]    


def main():
    print "Working"
    #url = raw_input("username")
    url = "yesitsressi"
    twitter(url)
    print "done"

def twitter(user):
    pageData("www.twitter.com/"+user)

if __name__=="__main__":
   main()


