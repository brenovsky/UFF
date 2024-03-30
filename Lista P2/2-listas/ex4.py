def inverter(x):
    y = []
    for i in range(len(x) - 1, -1, -1):
        y.append(x[i])
    x = y
    return x

lista = [0, 2, 3, 5, 4]

print(inverter(lista))