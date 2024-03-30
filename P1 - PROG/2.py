lista = [3, 2, 1, 4]
N = len(lista)
u = sum(lista) / N
s = 0
for i in range(N):
    s += ((lista[i] - u) ** 2)
d = ((s / N) ** (1 / 2))
print(d)