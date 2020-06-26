from math import floor
from math import ceil
n = float(input())
mod = int(round(n % 1, 5) * 10)
if mod >= 5:
    n = ceil(n)
else:
    n = floor(n)
print(n)
