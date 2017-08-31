import requests
import json
import os
import time
import sys

artists = {"sertanejo" :
                ["henrique-e-juliano", "jorge-e-mateus", "marilia-mendonca",
                "matheus-e-kauan", "luan-santana", "zeze-di-camargo-e-luciano",
                "bruno-e-marrone", "paula-fernandes", "naiara-azevedo",
                "victor-leo", "chitaozinho-e-xororo", "leonardo"],
            "forro" :
                ["wesley-safadao", "luiz-gonzaga", "falamansa",
                "calcinha-preta", "elba-ramalho", "avioes-do-forro",
                "banda-magnificos", "limao-com-mel", "dorgival-dantas",
                "dominguinhos", "flavio-jose", "luiz-gonzaga"],
            "mpb" :
                ["roberto-carlos", "nando-reis", "caetano-veloso",
                "chico-buarque", "marisa-monte", "raul-seixas",
                "djavan", "ana-carolina", "tim-maia", "tribalistas",
                "roupa-nova", "ze-ramalho", "maria-gadu"]}

key = "c5bfa4102ecd1bb4b62f0f80b88630da"
search_url = "https://api.vagalume.com.br/search.php"
fail = 0
success = 0

t1 = time.time()
try:
    os.mkdir("Letras")
except:
    pass

for style in artists:
    try:
        os.mkdir("Letras/" + style)
    except:
        pass

    for artist in artists[style]:
        try:
            os.mkdir("Letras/" + style + "/" + artist)
        except:
            pass

        artist_url = "https://www.vagalume.com.br/" + artist + "/index.js"
        r = requests.get(artist_url)
        artAns = json.loads(r.text)

        for item in artAns['artist']['toplyrics']['item']:
            song_id = item['id']
            r = requests.get(search_url + "?art=" + artist + "&musid=" + song_id + "&apikey=" + key)
            successful = False
            infail = 0

            #while not successful:
            try:
                ans = json.loads(r.text)
                f = open("Letras/" + style + "/" + artist + "/" + item['desc'] + ".txt", "w+")
                f.write(ans['mus'][0]['text'])
                f.close()
                success = success + 1
                print("Sucesso " + str(success) + ": " + style + "/" + artist + "/" + item['desc'])
                successful = True

            except:
                if infail == 0:
                    fail = fail + 1
                infail = infail + 1
                print("Falha: " + str(fail) + "." + str(infail))
                time.sleep(60)
                    #print(artAns)
                    #print()
                    #print(r.text)
                    #print()
                    #print(search_url + "?art=" + artist + "&musid=" + song_id + "&apikey=" + key)
                    #sys.exit()

            #print(ans['mus'][0]['text'])

        t2 = time.time()
        print("Tempo ateh agr: " + str(t2 - t1) + " segundos")

print(str(success) + " sucessos e " + str(fail) + " falhas.")
t2 = time.time()
print("Tempo total: " + str(t2 - t1) + " segundos")

#1793 sucessos e 26 falhas.
#Tempo total: 3668.4725477695465 segundos
#Total: 96201 requisições
