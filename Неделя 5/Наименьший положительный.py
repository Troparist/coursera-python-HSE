a = list(map(int, input().split()))

n = 1000

for i in range(1, len(a)):
    if n > a[i] and a[i] > 0:
        n = a[i]

print(n)
