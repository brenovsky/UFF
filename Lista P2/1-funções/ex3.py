def divisores(x):
    lista = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            lista.append(i)
    lista.append(x)
    return lista

n = int(input('input n: '))

print(divisores(n))