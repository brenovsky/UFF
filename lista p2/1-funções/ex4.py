def divisores(x):
    lista = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            lista.append(i)
    return lista

def perfeito(x):
    if sum(divisores(x)) == x:
        return True
    return False

n = int(input('input n: '))
print(perfeito(n))