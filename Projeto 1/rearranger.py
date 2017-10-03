import os as os

wordlist = ["para", "de", "com", "por", "em", "a", "o", "as", "os", u"à", u"às",
    "aos", "e", u"é", u"está", "na", "nas", "no", "nos", "pelo", "pela",
    "mas", "da", "do", "das", "dos","pra", "2x", "aqui", u"tá"]
wordlist += u"porém todavia contudo entretanto embargo obstante aliás ou ora quer que nem já logo senão logo portanto pois conseguinte então ademais porque desde qual conforme escopo proporção".split()
wordlist += u"se seu É foi faz vou isso ah lá oh são nessa pro aí lhe deu seja dá será fiz".split()
wordlist += u"tô te tão quis uma sua num ser era fui Ó essa esta este esse aquela aquele sobre há ".split()
wordlist += u"um uns uma umas me só quem assim sou vem ai como até mesmo estou fazer tanto nossa".split()
wordlist += u"vai sei".split()

local_dir = os.getcwd()
home = local_dir + "/Resultados/"
directory = os.fsencode(home)

for filename in os.listdir(directory):
    filenamestr = os.fsdecode(filename)

    filein = open(home + filenamestr, 'r')
    fileout = open(home + filenamestr + "_clean", "w+")
    for line in filein:
        out = line.split()
        if ((out[0] not in wordlist) and (int(out[-1]) >= 10)):
            fileout.write(out[-1] + " " + out[0] + "\n")

    filein.close()
    fileout.close()
