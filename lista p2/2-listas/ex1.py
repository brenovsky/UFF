def inserir(x, y):
    if y not in x:
        x.append(y)
    return x

lista = [1, 2, 3, 4]
valor = 3

print(inserir(lista, valor))