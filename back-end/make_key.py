import random
import generate_big_prime

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
	p_rand = random.randrange(100000000000000, 999999999999999)
	p = generate_big_prime.find_next_prime(p_rand)
	q_rand = random.randrange(100000000000000, 999999999999999)
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

	pub_key = {'e': e, 'n': n}
	private_key = {'d': d}

	#todo 将公私钥对存放到数据库中，便于调用

	print('pub_key: ' + str(pub_key))
	print('private_key: ' + str(private_key))


if __name__ == '__main__':
	generate_key()
