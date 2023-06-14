def divisores(x):
    lista = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            lista.append(i)
    lista.append(x)
    return lista

def aritmetico(x):
    if sum(divisores(x)) % len(divisores(x)) == 0:
        return True
    return False

n = int(input('input k: '))
print(aritmetico(n))