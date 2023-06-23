from Crypto.Hash import SHA256


hash_object = SHA256.new(bytes('hola, buenas', encoding='utf-8'))

print(hash_object.hexdigest())
#comprobamos la longitud hexadecimal
print(len(hash_object.hexdigest()))