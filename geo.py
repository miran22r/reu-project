from geopy import geocoders 
from geopy import distance

class Geo:

	states = {}
	def __init__(self):
    	    print "work"
    	    self.states = {
        	'AK': 'Alaska',
        	'AL': 'Alabama',
        	'AR': 'Arkansas',
        	'AS': 'American Samoa',
        	'AZ': 'Arizona',
        	'CA': 'California',
        	'CO': 'Colorado',
       		'CT': 'Connecticut',
        	'DC': 'District of Columbia',
        	'DE': 'Delaware',
        	'FL': 'Florida',
        	'GA': 'Georgia',
        	'GU': 'Guam',
        	'HI': 'Hawaii',
        	'IA': 'Iowa',
        	'ID': 'Idaho',
        	'IL': 'Illinois',
        	'IN': 'Indiana',
        	'KS': 'Kansas',
        	'KY': 'Kentucky',
        	'LA': 'Louisiana',
        	'MA': 'Massachusetts',
        	'MD': 'Maryland',
        	'ME': 'Maine',
        	'MI': 'Michigan',
        	'MN': 'Minnesota',
        	'MO': 'Missouri',
        	'MP': 'Northern Mariana Islands',
        	'MS': 'Mississippi',
        	'MT': 'Montana',
        	'NA': 'National',
        	'NC': 'North Carolina',
        	'ND': 'North Dakota',
        	'NE': 'Nebraska',
        	'NH': 'New Hampshire',
        	'NJ': 'New Jersey',
        	'NM': 'New Mexico',
        	'NV': 'Nevada',
        	'NY': 'New York',
        	'OH': 'Ohio',
        	'OK': 'Oklahoma',
        	'OR': 'Oregon',
        	'PA': 'Pennsylvania',
        	'PR': 'Puerto Rico',
        	'RI': 'Rhode Island',
        	'SC': 'South Carolina',
       		'SD': 'South Dakota',
        	'TN': 'Tennessee',
        	'TX': 'Texas',
        	'UT': 'Utah',
        	'VA': 'Virginia',
        	'VI': 'Virgin Islands',
        	'VT': 'Vermont',
        	'WA': 'Washington',
        	'WI': 'Wisconsin',
        	'WV': 'West Virginia',
        	'WY': 'Wyoming'
	}

	def coordinates(self,place):
    	    g = geocoders.GoogleV3()
            place, (lat, lng) = g.geocode(place)
            print "%s:, %.5f:, %.5f" % (place, lat, lng)
	    print place
            loc = place.split(",") 
	    print loc
	    if(" USA" == str(loc.pop())):
		print "in the us"
	        stateZip = str(loc.pop())
                state = stateZip[1:3]
                print stateZip
                if(self.states.has_key(state)):
            	    print "state found"
                else:
                    print "state not found"
                city = loc.pop()
                print city[0:len(city)]
                return city, state
    	    else:
		print "not in the us"
       	        return "None", "None"

def main():
   g = Geo()
   read = raw_input("Put in a location")
   something  = g.coordinates(read)
  

if __name__=="__main__": 
   main()
