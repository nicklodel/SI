import random
import string
import argparse

alpha = "abcdefghijklmnopqrstuvwxyz"
parser = argparse.ArgumentParser(description = "Mono cypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

parser.add_argument('-o', dest = "salida", type=str,	metavar='OFILE', 
                    help='specify output file')


args = parser.parse_args()
with open(args.entrada) as f:
        rawtext = f.readline()
        f.close()

l = list(alpha)
random.shuffle(l)
key = "".join(l)

rawtext = rawtext.strip('\n')
rawtext = rawtext.translate({ord(' '): None})
letterList = []
for letter in rawtext:
    letterList.append(key[alpha.index(letter)])
    print(letterList)

f=open(args.salida,"w")
f.write("".join(letterList))
f.write("\n")
f.write(key)
f.close