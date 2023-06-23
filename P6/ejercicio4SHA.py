from Crypto.Hash import SHA256
import argparse

##Comparamos la cadena hexadecimal de un SHA256 y la resultante de hacer el hash al nombre de un fichero

parser = argparse.ArgumentParser(description = "SHA cypher")

parser.add_argument("entrada", help= "Nombre del fichero",type=str)

parser.add_argument("SHA", help = "Nombre del fichero a comparar", type=str)

args = parser.parse_args()


##Usaremos siempre la versión hexadecimal


hash_objectA = SHA256.new(bytes(args.entrada, encoding='utf-8'))



if hash_objectA.hexdigest() == args.SHA :
    print('Hashes iguales\n')
    print(hash_objectA.hexdigest())
    exit()

print('Hashes distintos')
print(hash_objectA.hexdigest())
