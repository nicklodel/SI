from Crypto.Hash import MD5
import argparse

##Como yo entiendo el enunciado, se busca hacer el valor hash MD5 del nombre del fichero.

parser = argparse.ArgumentParser(description = "MD5 cypher")


parser.add_argument("entrada", help= "Nombre del fichero",type=str)



args = parser.parse_args()




hash_object = MD5.new(bytes(args.entrada, encoding='utf-8'))

print(hash_object.hexdigest())

