# we want to display the data a little differently right now
# we do our imports

import json 
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# changing limit will change number of results
response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=weezer+" + sys.argv[1])

# we are going to put the data into a variable called o
o = response.json()
# we make a for loop 
# for each result in that objects key
for result in o["results"]:
    # we print out the track name
    print(result['trackName'])