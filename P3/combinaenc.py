import argparse
import string
import zipfile
parser = argparse.ArgumentParser(description = "Caesar cypher")

parser.add_argument("k",help = "Añade un desplazamiento",type=int)
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
         result += chr((ord(char) + args.k -65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + args.k - 97) % 26 + 97)


with zipfile.ZipFile(args.salida + '.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
    myzip.write('./' + args.salida)
    f=open(args.salida,"w")
    f.write(result)
    f.close
