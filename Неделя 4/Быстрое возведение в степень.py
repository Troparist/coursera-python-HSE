def r(a, n):
    if a % 2 == 0:
        return ((a ** 2) ** ((n / 2)))
    return a * (a ** (n - 1))

a, b = float(input()), float(input())

print(r(a, b))
