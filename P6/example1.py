from Crypto.Hash import SHA256

hash_object = SHA256.new(data = b'First')
hash_object.update(b'SecondThird')

print(hash_object.digest())
print(hash_object.hexdigest())

print(hash_object.digest_size)
print(hash_object.block_size)