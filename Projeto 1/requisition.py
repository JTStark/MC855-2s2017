import requests
import json

artist = "u2"
#song = "one"
key = "c5bfa4102ecd1bb4b62f0f80b88630da"
search_url = "https://api.vagalume.com.br/search.php"
artist_url = "https://www.vagalume.com.br/" + artist + "/index.js"

#r = requests.get(search_url + "?art=" + artist + "&mus=" + song + "&apikey=" + key)
#ans = json.loads(r.text)

#print(ans['mus'][0]['text'])

r = requests.get(artist_url)
ans = json.loads(r.text)
song_id = ans['artist']['toplyrics']['item'][0]['id']

r = requests.get(search_url + "?art=" + artist + "&musid=" + song_id + "&apikey=" + key)
ans = json.loads(r.text)
print(ans['mus'][0]['text'])
