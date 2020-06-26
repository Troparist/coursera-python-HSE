a = list(map(int, input().split()))

n = a[0]
index = 0

for i in range(0, len(a)):
    if a[i] >= n:
        n = a[i]
        index = i

print(n, index)
