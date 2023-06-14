matriz = [[4, 3, 1], [0, 2, 5], [0, 0, 1]]

superior = True

if len(matriz) == len(matriz[0]) and superior:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i > j and matriz[i][j] != 0:
                superior = False
                break
else:
    superior = False

print(superior)