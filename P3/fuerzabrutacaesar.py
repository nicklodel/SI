import argparse
import string

parser = argparse.ArgumentParser(description = "Caesar decypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

letterList = []
args = parser.parse_args()
with open(args.entrada) as f:
        rawtext = f.readline()
        f.close()

result  = ""
for j in string.ascii_lowercase:
    
   for i in range(len(rawtext)):
      char = rawtext[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) - ord(j) -65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) - ord(j)- 97) % 26 + 97)
   print(result)
   result+=""
   result+="\n"
