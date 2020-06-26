n = int(input())
m = int(input())


def div(a, b):
    if a % b == 0:
        return b
    return div(b, a % b)


def ReduceFraction(n, m):
    p = n / div(n, m)
    q = m / div(n, m)
    return int(p), int(q)


print(*ReduceFraction(n, m))
