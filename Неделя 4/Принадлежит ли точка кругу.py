def IsPointInCircle(x, y, xc, yc, r):
    a = abs(x - xc) * abs(x - xc)
    b = abs(y - yc) * abs(y - yc)
    c = a + b
    return (c <= r ** 2)

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
rad = float(input())

if (IsPointInCircle(x, y, xc, yc, rad)):
    print("YES")
else:
    print("NO")
