import math
"""
Euclids Algorithm. Returns the greatest common denominator of m and n.
"""
def euclids_algorithm(m, n):
	if n > m:
		return euclids_algorithm(n, m)
	r = m % n
	if r == 0:
		return n
	return euclids_algorithm(n, r)

"""
Extended Euclids Algorithm. Returns the greatest common denominator of m and n as well as two integers a,b such that ma + bn = d.
"""
def extended_euclids_algorithm(m,n, a=0, b=1, a_prime=1, b_prime=0):
	c = m
	d = n
	r = m % n
	q = math.floor(m/n)
	if r == 0:
		return (d, a, b)
	t = a_prime
	a_prime = a
	a = t - (q*a)
	t = b_prime
	b_prime = b
	b = t - (q*b)
	return extended_euclids_algorithm(d, r, a, b, a_prime, b_prime)