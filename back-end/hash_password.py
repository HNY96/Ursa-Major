# -*- coding: utf-8 -*-

from os import urandom
import hashlib

def hash_password(password):
    m = hashlib.sha256()
    m.update(bytes(password, encoding='utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    print(hash_password('123456'))