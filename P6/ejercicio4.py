from Crypto.Hash import MD5
import argparse

##Comparamos la cadena hexadecimal de un MD5 y la resultante de hacer el hash al nombre de un fichero

parser = argparse.ArgumentParser(description = "MD5 cypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

parser.add_argument("MD5", help = "Nombre del fichero a comparar", type=str)

args = parser.parse_args()


##Usaremos siempre la versión hexadecimal


hash_objectA = MD5.new(bytes(args.entrada, encoding='utf-8'))



if hash_objectA.hexdigest() == args.MD5 :
    print('Hashes iguales\n')
    print(hash_objectA.hexdigest())
    exit()

print('Hashes distintos')
print(hash_objectA.hexdigest())
