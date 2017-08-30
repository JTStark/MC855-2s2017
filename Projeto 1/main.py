import requests
import json

artists = ["u2"]
key = "c5bfa4102ecd1bb4b62f0f80b88630da"
search_url = "https://api.vagalume.com.br/search.php"

for artist in artists:
    artist_url = "https://www.vagalume.com.br/" + artist + "/index.js"
    r = requests.get(artist_url)
    ans = json.loads(r.text)

    for item in ans['artist']['toplyrics']['item']:
        song_id = item['id']
        r = requests.get(search_url + "?art=" + artist + "&musid=" + song_id + "&apikey=" + key)
        ans = json.loads(r.text)

        print(ans['mus'][0]['text'])
