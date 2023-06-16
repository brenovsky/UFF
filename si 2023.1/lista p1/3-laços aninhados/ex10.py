n = int(input('input n: '))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
soma = 0
for i in range(n):
    soma += (a[i] - b[i]) ** 2
print(soma ** (1 / 2))
