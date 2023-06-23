from Crypto.Hash import SHA256
import argparse

##Función que escribe en el fichero contraseñas el usuario y la contraseña cifrada
parser = argparse.ArgumentParser(description = "SHA cypher password")

parser.add_argument("usuario", help= "Nombre del fichero",type=str)

parser.add_argument("contraseña", help = "Nombre del fichero a comparar", type=str)

args = parser.parse_args()


##Usaremos siempre la versión hexadecimal


hash_objectA = SHA256.new(bytes(args.contraseña, encoding='utf-8'))


f=open('contraseñas','w')
f.write(args.usuario + '\n')
f.write(hash_objectA.hexdigest() + '\n')
f.close()

f=open('shadow','w')
f.write(args.usuario + '\n')
f.write(args.contraseña)
f.close()