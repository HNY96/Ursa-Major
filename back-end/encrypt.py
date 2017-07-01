def quick_mod(a, b, c):
	ans = 1
	while b:
		if b % 2 == 1:
			ans = (ans * a) % c
		b //= 2
		a = (a * a) % c
	return ans

def encrypt(m):
    file_object = open('e.txt', 'r')
    e = int(file_object.read())
    file_object = open('n.txt', 'r')
    n = int(file_object.read())
    file_object.close()

    result = []
    for i in range(len(m)):
        result.append(ord(m[i]))
    for i in range(len(result)):
        result[i] = quick_mod(result[i], e, n)
        # print(result[i])

# test function
if __name__ == "__main__":
    encrypt('hello')
