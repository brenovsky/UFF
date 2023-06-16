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

a = int(input('input a: '))
n = int(input('input n: '))
for i in range(1, n + 1):
    if coprimo(a, i) == True:
        print(i)