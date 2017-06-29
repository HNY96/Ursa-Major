# 计算 a**b mod c
def quick_mod(a, b, c):
    ans = 1
    while b:
        if b % 2 == 1:
            ans = (ans * a) % c
        b //= 2
        a = (a * a) % c
    return ans


def decrypt(c):
    #todo 去数据库中找到服务器的公私钥 private_key[d], pub_key[n]

    m = quick_mod(c, private_key[d], pub_key[n])
