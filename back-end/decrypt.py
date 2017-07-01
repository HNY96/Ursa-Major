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
    # read key after making that
    file_object = open("d.txt", 'r')
    private_key = file_object.read()
    file_object = open('n.txt', 'r')
    n = file_object.read()
    file_object.close()

    result = []
    for i in range(len(c)):
        result.append(quick_mod(c[i], int(private_key), int(n)))
    for i in range(len(result)):
        result[i] = chr(result[i])
        # print(result[i])


# test function
if __name__ == '__main__':
    decrypt([1362, 138, 1292, 1292, 444])