import argparse
alpha = 'abcdefghijklmnopqrstuvwxyz'
parser = argparse.ArgumentParser(description = "Caesar decypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

args = parser.parse_args()
with open(args.entrada) as f:
        rawtext = f.readline()
        f.close()

frequency = [[letter for letter in alpha]  for y in range(2)]
i=0
for letter in alpha:
    frequency[1][i] = 0
    i= i+1


for letter in rawtext:
    if letter in alpha:
        print(letter)
        frequency[1][alpha.index(letter)] = frequency[1][alpha.index(letter)] +1

i=0
for letter in alpha:
    frequency[1][i] = frequency[1][i]/len(rawtext)
    i= i+1

print(frequency)

