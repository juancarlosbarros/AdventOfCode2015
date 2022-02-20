import hashlib

BASE = 'ckczppom'
n = 6  # number of '0' wanted at beginning of hash
TEST_START = '0' * n

for i in range(10 ** 7):
    key = (BASE + str(i)).encode('ASCII')
    hash = hashlib.md5(key).hexdigest()
    start = hash[:n]
    if start == TEST_START:
        print(key, hash)
        break
print(i)
