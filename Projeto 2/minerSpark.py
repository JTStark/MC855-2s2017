#newspaper from: https://github.com/codelucas/newspaper

import newspaper
from newspaper import Article
import requests
import json
import os
import sys
from pyspark.sql import SparkSession

links = {"Independent": "http://www.independent.co.uk/news/world",
         "Guardian": "https://www.theguardian.com/world",
         "Reuters": "http://www.reuters.com/news/world"}

def get_article(article):
    try:
        article.download()
        flag = True
    except:
        print("Erro no download")
        j += 1
        flag = False

    if flag:
        try:
            article.parse()
        except:
            print("Erro no parse")
            j += 1
            flag = False

    if flag:
        return article.title + "\n\n" + article.text


try:
    os.mkdir("Noticias")
except:
    pass

spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

try:
    ind = newspaper.build(links["Independent"])
    guard = newspaper.build(links["Guardian"])
    reut = newspaper.build(links["Reuters"])
except:
    print("Erro ao criar jornais")
    sys.exit(0)

articles_list = ind.articles + guard.articles + reut.articles

rdd = spark.sparkContext.parallelize(articles_list)
rdd.flatMap(get_article)
articles_list = rdd.collect()

for i in range(len(articles_list)):
    f = open("Noticias/" + "art" + str(i) + ".txt", "w+")
    f.write(articles_list[i])
    f.close()

