from Crypto.Hash import MD5
import argparse



parser = argparse.ArgumentParser(description = "MD5 cypher")

##En este caso cogemos dos ficheros y comparamos el hash de su interior para ver si tiene el mismo hash value
parser.add_argument("entrada", help= "Nombre del fichero",type=str)

parser.add_argument("compara", help = "Nombre del fichero a comparar", type=str)

args = parser.parse_args()

with open(args.entrada) as f:
    text = f.readline()

with open(args.compara) as f:
    textB = f.readline()


hash_objectA = MD5.new(bytes(text, encoding='utf-8'))
hash_objectB = MD5.new(bytes(textB,encoding = 'utf-8'))


if hash_objectA.hexdigest() == hash_objectB.hexdigest() :
    print('Hashes iguales\n')
    print(hash_objectA.hexdigest())
    exit()

print('Hashes distintos')
print(hash_objectA.hexdigest())
print(hash_objectB.hexdigest())

