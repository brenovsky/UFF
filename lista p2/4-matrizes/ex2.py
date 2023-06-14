matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

identidade = True

if len(matriz) == len(matriz[0]) and identidade:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j and matriz[i][j] != 1:
                identidade = False
                break
            elif i != j and matriz[i][j] != 0:
                identidade = False
                break
else:
    identidade = False

print(identidade)