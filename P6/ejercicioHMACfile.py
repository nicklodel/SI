from Crypto.Hash import HMAC, SHA256
import argparse


parser = argparse.ArgumentParser(description = "HMAC cypher")


parser.add_argument("entrada", help= "Nombre del fichero",type=str)



args = parser.parse_args()

with open(args.entrada) as f:
    text =f.readline()

secret = b'Patata'
h = HMAC.new(secret, digestmod=SHA256)
h.update(bytes(text,encoding='utf-8'))

try:

    h.hexverify(h.hexdigest())

    print("The message '%s' is authentic" % text)

except ValueError:

  print("The message or the key is wrong")

secret= b'Batata'
hmacErroneo = HMAC.new(secret,digestmod=SHA256)
hmacErroneo.update(bytes(text,encoding='utf-8'))


try:

    h.hexverify(hmacErroneo.hexdigest())

    print("The message '%s' is authentic" % text)

except ValueError:

  print("Error de mensaje o clave")