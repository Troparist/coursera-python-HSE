from math import sqrt


def isPrime(n):
    i, k = 2, sqrt(n)
    while i <= k:
        if n % i != 0:
            i += 1
        else:
            return 'NO'
    return 'YES'


x = int(input())
print(isPrime(x))
