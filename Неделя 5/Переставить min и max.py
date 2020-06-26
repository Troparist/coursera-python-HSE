a = list(map(int, input().split()))
minIndex = a.index(min(a))
maxIndex = a.index(max(a))
a[minIndex], a[maxIndex] = a[maxIndex], a[minIndex]

print(*a, sep=' ')
