from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import argparse
#El archivo se llamará entrada
##Esta función lee de fichero y encripta dicho texto
data = b""
parser = argparse.ArgumentParser(description = "EAX cypher")


parser.add_argument("entrada", help= "Nombre del fichero",type=str)
args = parser.parse_args()
with open(args.entrada) as f:
    
    data+= f.readline().encode("utf-8")
f.close()
key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
print(key.hex())