from Crypto.Hash import HMAC, SHA256
secret = b'Patata'
h = HMAC.new(secret, digestmod=SHA256)
text = 'Buenas tardes'
h.update(b'Buenas tardes')

try:

    h.hexverify(h.hexdigest())

    print("The message '%s' is authentic" % text)

except ValueError:

  print("The message or the key is wrong")

secret= b'Batata'
hmacErroneo = HMAC.new(secret,digestmod=SHA256)
hmacErroneo.update(b'Buenas tardes')


try:

    h.hexverify(hmacErroneo.hexdigest())

    print("The message '%s' is authentic" % text)

except ValueError:

  print("Error de mensaje o clave")