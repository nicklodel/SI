import random
import string
l = list(string.ascii_lowercase)
random.shuffle(l)
result = ''.join(l)
print(result)