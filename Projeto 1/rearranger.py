import os as os

wordlist = ["para", "de", "com", "por", "em", "a", "o", "as", "os", u"à", u"às",
    "aos", "e", u"é", u"está", "na", "nas", "no", "nos", "pelo", "pela",
    "mas", "da", "do", "das", "dos"]

local_dir = os.getcwd()
home = local_dir + "/Resultados/"
directory = os.fsencode(home)

for filename in os.listdir(directory):
    filenamestr = os.fsdecode(filename)

    filein = open(home + filenamestr, 'r')
    fileout = open(home + filenamestr + "_clean", "w+")
    for line in filein:
        out = line.split()
        if out[0] not in wordlist:
            fileout.write(out[-1] + " " + out[0] + "\n")

    filein.close()
    fileout.close()
