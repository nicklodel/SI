from Crypto.Hash import SHA256
import argparse

##Como yo entiendo el enunciado, se busca hacer el valor hash MD5 del nombre del fichero.

parser = argparse.ArgumentParser(description = "SHA cypher")


parser.add_argument("entrada", help= "Nombre del fichero",type=str)



args = parser.parse_args()




hash_object = SHA256.new(bytes(args.entrada, encoding='utf-8'))

print(hash_object.hexdigest())