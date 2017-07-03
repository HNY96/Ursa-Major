# -*- coding: utf-8 -*-

import time
import hashlib
import encrypt

def make_credit(username, e, n):
    credit ='''<credit>
    <pub_key_e>%s</pub_key_e>
    <pub_key_n>%s</pub_key_n>
    <username>%s</username>
    <date_of_issue>%s</date_of_issue>
</credit>''' % (e, n, username, time.strftime('%Y-%m-%d',time.localtime(time.time())))
    # print(credit)

    # 将证书的hash值得到
    m = hashlib.sha256()
    m.update(bytes(credit, encoding='utf-8'))
    print(m.hexdigest())

    # 将hash值用自己的私钥进行加密
    file_object = open('d.txt', 'r')
    d = int(file_object.read())
    file_object = open('n.txt', 'r')
    n = int(file_object.read())
    file_object.close()

    m = m.hexdigest()
    result = []
    for i in range(len(m)):
        result.append(ord(m[i]))
    for i in range(len(result)):
        result[i] = encrypt.quick_mod(result[i], d, n)
        # print(result[i])

    return credit + ' ursa-major ' + str(result)

if __name__ == '__main__':
    print(make_credit('he', '25387', '31877'))
