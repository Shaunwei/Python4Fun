#!/usr/bin/env python3.3
# find the greatest common divisor of two nonnegative integer
# example: gcd(9,6)=3; gcd(49,21) =7; gcd(0,6) =6

def gcd(a,b):
	M = max(a,b)
	m = min(a,b)

	if m == 0:
		return M

	for i in range(m,0,-1):
		if a%i==0 and b%i == 0:
			return i

	return 1;

def euclid(a,b):
	while b!=0:
		temp,a = a,b
		b = temp %a

	return a;


if __name__ == '__main__':
	a, b = raw_input('Enter a,b: ').split(' ')

	print(euclid(int(a),int(b)))

