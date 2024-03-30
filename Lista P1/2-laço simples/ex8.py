n = int(input('input n: '))
k = int(input('input k: '))
p, d, i, j = 1, 1, 0, 0
while k - j > 0:
    p = p * (n - i)
    d = d * (k - j)
    i += 1
    j += 1
print(p // d)