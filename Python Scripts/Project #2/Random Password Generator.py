# Generate a random password 15 characters long with symbols included as well as capitals and lowercase.
import os
import random
import string

length = 15
chars = string.ascii_letters + string.digits + ')(*&^%$#@!'
random.seed = (os.urandom(1024))

print(''.join(random.choice(chars) for i in range(length)))
