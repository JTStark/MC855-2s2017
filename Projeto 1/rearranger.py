filein = open("part-00000", "r")
fileout = open("out-00000", "w")

for line in filein:
    out = line.split()
    fileout.write(out[-1] + " " + out[0] + "\n")

filein.close()
fileout.close()
