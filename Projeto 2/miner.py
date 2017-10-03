#newspaper from: https://github.com/codelucas/newspaper

import newspaper
from newspaper import Article
import requests
import json
import os
import time
import sys

links = {"Independent": "http://www.independent.co.uk/news/world",
         "Guardian": "https://www.theguardian.com/world",
         "Reuters": "http://www.reuters.com/news/world"}


t1 = time.time()

try:
    os.mkdir("Noticias")
except:
    pass

for paper in links:
    try:
        os.mkdir("Noticias/" + paper)
        print("Pasta geral " + paper + " criada com sucesso")
    except:
        print("Erro pasta geral " + paper)
        t2 = time.time()
        print("Tempo total: " + str(t2 - t1) + " segundos")
        sys.exit(0)


    folder_head = "Noticias/" + paper + "/Headlines"
    try:
        os.mkdir(folder_head)
        print("Pasta de manchetes " + paper + " criada com sucesso")
    except:
        print("Erro pasta de manchetes " + paper)
        t2 = time.time()
        print("Tempo total: " + str(t2 - t1) + " segundos")
        sys.exit(0)


    folder_text = "Noticias/" + paper + "/Artigos"
    try:
        os.mkdir(folder_text)
        print("Pasta de artigos " + paper + " criada com sucesso")
    except:
        print("Erro pasta de artigos " + paper)
        t2 = time.time()
        print("Tempo total: " + str(t2 - t1) + " segundos")
        sys.exit(0)


    try:
        news_paper = newspaper.build(links[paper])
    except:
        print("Erro ao criar " + paper)
        t2 = time.time()
        print("Tempo total: " + str(t2 - t1) + " segundos")
        sys.exit(0)

    print("Tudo pronto para " + paper)
    print(paper + ": " + str(len(news_paper.articles)) + " artigos")


    i = 0
    for article in news_paper.articles[:129]:
        article.download()
        article.parse()

        f = open(folder_head + "/headline" + '{:03d}'.format(i) + ".txt", "w+")
        f.write(article.title)
        f.close()

        f = open(folder_text + "/artigo" + '{:03d}'.format(i) + ".txt", "w+")
        f.write(article.title)
        f.close()

        i += 1
        print('{:05.2f}'.format(i/130.0) + "% concluidos de " + paper)
        time.sleep(5)

    t2 = time.time()
    print("Tempo ateh agr: " + str(t2 - t1) + " segundos")

t2 = time.time()
print("Tempo total: " + str(t2 - t1) + " segundos")
