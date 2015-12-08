import hashlib

hash = 'yzbqklnj'

int = 0

while not hashlib.md5("{}{}".format(hash, int).encode('utf-8')).hexdigest().startswith('000000'):
    print("Nope luck for {}{}".format(hash, int))
    int += 1

print("Key: {}{}".format(hash, int))
print("Number: {}").format(int)