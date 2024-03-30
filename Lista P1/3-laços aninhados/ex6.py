def coprimo(x, y):
    X = []
    Y = []
    for i in range(1, x + 1):
        if x % i == 0:
            X.append(i)
    for i in range(1, y + 1):
        if y % i == 0:
            Y.append(i)
    for i in range(1, len(Y)):
        if Y[i] in X:
            return False
    return True

n = int(input('input n: '))

phi = 0

for i in range(1, n):
    if coprimo(n, i) == True:
        phi += 1
print(phi)