# Website scrapper
import ast
import json
import requests
from bs4 import BeautifulSoup

class Scrape:
        def __init__(self):
            print "working"

        #  returns the location and follower count from a given a twitter page
        def pageData(self, url):
            raw = requests.get("http://"+url)
            data = raw.text
            soup = BeautifulSoup(data,["lxml", "xml"])

            for link in soup.find_all(class_="json-data", limit=1):
                strLink = str(link)
                init = strLink.index("value") + 7
                final = strLink.index("false}}'>") + 7
                json_data = "%s"% strLink[init:final]
                json_data = json_data.replace("false", "False")
                json_data = json_data.replace("true", "True")
                json_data = json_data.replace("null", "0")
                json = ast.literal_eval(json_data)
                print json.has_key('profile_user')
                portion = json['profile_user']
                location = portion['location']
                followers = portion['followers_count']
                print location
                print followers
                return location, followers

        # returns location and follower count given a Twitter username
        def twitter(self, user):
            return self.pageData("www.twitter.com/"+user)

# main
def main():
    p = Scrape()
    print "Working"
    url = raw_input("username: ")
    l,f = p.twitter(url)
    print "done"

if __name__=="__main__":
   main()
