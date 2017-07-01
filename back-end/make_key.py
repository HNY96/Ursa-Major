import random
import generate_big_prime
import math

def quick_mod(a, b, c):
	ans = 1
	while b:
		if b % 2 == 1:
			ans = (ans * a) % c
		b //= 2
		a = (a * a) % c
	return ans

def gcd(a, b):
	while (b > 0):
		r = a % b
		a = b
		b = r
	return a

# 扩展欧几里得算法，可以快速计算逆

def exgcd(a, b):
	x0 = 1
	y0 = 0
	x1 = 0
	y1 = 1
	x = 0
	y = 1
	r = a % b
	q = (a - r) / b
	while (r):
		x = x0 - q * x1
		y = y0 - q * y1
		x0 = x1
		y0 = y1
		x1 = x
		y1 = y
		a = b
		b = r
		r = a % b
		q = (a - r) / b
	return int(x)


def generate_key():
	# 生成两个15位的大素数p和q
	p_rand = random.randrange(10, 99)
	p = generate_big_prime.find_next_prime(p_rand)
	q_rand = random.randrange(10, 99)
	q = generate_big_prime.find_next_prime(q_rand)

	# 生成n，phi_n，e，d

	n = p * q
	phi_n = (p - 1) * (q - 1)
	while (True):
		e_rand = random.randrange(2, phi_n)
		if 1 == gcd(phi_n, e_rand):
			e = e_rand
			break
		else:
			continue

	d = exgcd(e, phi_n)
	if d < 0:
		d = phi_n + d

	pub_key = {'e': e, 'n': n}
	private_key = {'d': d}

	file_object = open('e.txt', 'w')
	file_object.write(str(e))
	file_object = open('n.txt', 'w')
	file_object.write(str(n))
	file_object = open('d.txt', 'w')
	file_object.write(str(d))
	file_object.close()

	print(math.log(n, 2))
	print('pub_key: ' + str(pub_key))
	print('private_key: ' + str(private_key))


if __name__ == '__main__':
	generate_key()
