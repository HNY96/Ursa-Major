from os import urandom
import hashlib

def hash_password(password):
    salt = urandom(32)
    m = hashlib.sha256()
    m.update(bytes(password, encoding='utf-8'))
    m.update(salt)
    print(m.hexdigest())

    #todo 需要把salt和最后的hash分开两项存到表中


if __name__ == '__main__':
    hash_password('123456')