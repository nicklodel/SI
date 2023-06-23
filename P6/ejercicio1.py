from Crypto.Hash import MD5


hash_object = MD5.new(bytes('hola, buenas', encoding='utf-8'))

print(hash_object.hexdigest())
#comprobamos la longitud hexadecimal
print(len(hash_object.hexdigest()))