def perfeitos(x):
    lista = []
    k = 1
    while k ** 2 <= x:
        lista.append(k ** 2)
        k += 1
    return lista

n = int(input('input n: '))
print(perfeitos(n))