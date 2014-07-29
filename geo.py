from geopy import geocoders
from geopy import distance

class geo:

	states = {}
	def __init__(self):
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
		try:
			place, (lat, lng) = g.geocode(place)
			loc = place.split(",")
			if(" USA" == str(loc.pop())):
				stateZip = str(loc.pop())
				state = stateZip[1:3]
				if(self.states.has_key(state)):
					city = loc.pop()
					if len(city) > 1:
						print city, state
						return city, state
				else:
					print "state not found"
			else:
				city = "None"
				state = "None"
				print city, state
				return city, state
		except:
			city = "None"
			state = "None"
			print city, state
			return city, state
