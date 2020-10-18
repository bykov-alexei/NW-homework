from math import sqrt
from random import choices
import pickle as pkl


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    ds = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ds.add(i)
            ds.add(n // i)
    return set(ds)

def isCoprime(*arr):
    common = set([i for i in range(1, max(arr) + 1)])
    for n in arr:
        common = common.intersection(divisors(n))
    return len(common) == 1

def getE(phi_n):
    for i in range(2, phi_n):
        if isCoprime(i, phi_n):
            return i

def getD(e, phi_n):
    for i in range(1, phi_n):
        if (e * i) % phi_n == 1:
            return i

primes = [i for i in range(1000) if isPrime(i)]

p, q = choices(primes, k=2)
# p, q = 23, 37
print("p=%i, q=%i" % (p, q,))
n = p * q
print("n=%i" % n)
phi_n = (p - 1) * (q - 1)
print("phi(n)=%i" % phi_n)
e = getE(phi_n)
print('e=%i' % e)
d = getD(e, phi_n)
print('d=%i' % d)

with open('public.key', 'w') as f:
    f.write("%i %i" % (e, n))

with open('private.key', 'w') as f:
    f.write("%i %i" % (d, n))
 