import random
import string
import argparse

alpha = "abcdefghijklmnopqrstuvwxyz"
parser = argparse.ArgumentParser(description = "Mono decypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

parser.add_argument('-o', dest = "salida", type=str,	metavar='OFILE', 
                    help='specify output file')


args = parser.parse_args()
with open(args.entrada) as f:
        rawtext = f.readline()
        key = f.readline()
        f.close()

rawtext = rawtext.strip('\n')
key = key.strip('\n')
letterList = []
for letter in rawtext:
    letterList.append(alpha[key.index(letter)])
    print(letterList)

f=open(args.salida,"w")
f.write("".join(letterList))
f.close
