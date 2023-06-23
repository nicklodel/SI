import argparse
import string
parser = argparse.ArgumentParser(description = "Caesar decypher")


parser.add_argument("entrada", help= "Nombre del fichero",type=str)


parser.add_argument('-o', dest = "salida", type=str,	metavar='OFILE', 
                    help='specify output file')

letterList = []
args = parser.parse_args()
with open(args.entrada) as f:
        rawtext = f.readline()
        f.close()

result  = ""
for i in range(len(rawtext)):
      char = rawtext[i]
      # Encrypt uppercase characters in plain text
      if (char.isupper()):
         result += chr((ord(char) - 3 -65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) - 3 - 97) % 26 + 97)

f=open(args.salida,"w")
f.write(result)
f.close