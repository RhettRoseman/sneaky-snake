# we want to import requests and sys first 
# we also now need to import json
import json
import requests
import sys

# if the length of sysargv is not equal to 2
if len(sys.argv) != 2:
    # exit the program
    sys.exit()
# we make a variable called response
# This code looks up one Weezer song on iTunes, adding a word from the command line to the search. Authors note: if you dont have the + at the end of this link it will not work properly
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer+" + sys.argv[1])

# we want to parse the JSON response, using our variable we just created the ability to parse JSON
# we dont want the giant block of JSON we want to dump a string here
print(json.dumps(response.json(), indent=2))

# expected input: 
# python3 itunes.py weezer
# expected response:
# {
#   "resultCount": 1,
#   "results": [
#     {
#       "wrapperType": "track",
#       "kind": "song",
#       "artistId": 115234,
#       "collectionId": 1481414042,
#       "trackId": 1481414192,
#       "artistName": "Weezer",
#       "collectionName": "Frozen 2 (Original Motion Picture Soundtrack)",
#       "trackName": "Lost in the Woods",
#       "collectionCensoredName": "Frozen 2 (Original Motion Picture Soundtrack)",
#       "trackCensoredName": "Lost in the Woods (Weezer Version)",
#       "collectionArtistId": 36270,
#       "collectionArtistName": "Various Artists",
#       "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
#       "collectionViewUrl": "https://music.apple.com/us/album/lost-in-the-woods-weezer-version/1481414042?i=1481414192&uo=4",
#       "trackViewUrl": "https://music.apple.com/us/album/lost-in-the-woods-weezer-version/1481414042?i=1481414192&uo=4",
#       "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview126/v4/07/a6/a0/07a6a03f-0c12-a39b-8839-9805595022ee/mzaf_8190126004987717841.plus.aac.p.m4a",
#       "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/31/7d/73/317d7343-9844-1dbc-dd0d-d63d990e7938/19UMGIM88564.rgb.jpg/30x30bb.jpg",
#       "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/31/7d/73/317d7343-9844-1dbc-dd0d-d63d990e7938/19UMGIM88564.rgb.jpg/60x60bb.jpg",
#       "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/31/7d/73/317d7343-9844-1dbc-dd0d-d63d990e7938/19UMGIM88564.rgb.jpg/100x100bb.jpg",
#       "collectionPrice": 9.99,
#       "trackPrice": 1.29,
#       "releaseDate": "2014-10-13T12:00:00Z",
#       "collectionExplicitness": "notExplicit",
#       "trackExplicitness": "notExplicit",
#       "discCount": 1,
#       "discNumber": 1,
#       "trackCount": 11,
#       "trackNumber": 11,
#       "trackTimeMillis": 185240,
#       "country": "USA",
#       "currency": "USD",
#       "primaryGenreName": "Soundtrack",
#       "isStreamable": true
#     }
#   ]
# }
