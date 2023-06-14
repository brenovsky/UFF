def inverter(x):
    y = []
    for i in range(len(x) - 1, -1, -1):
        y.append(i)
    return y

lista = [0, 1, 2, 3, 4, 5]

print(inverter(lista))
