matriz = [[4, 7, 9], [7, 2, 3], [9, 3, 6]]

simetria = True

for i in range(len(matriz)): #len(matriz) = quantidade de linhas
    for j in range(len(matriz[0])): #len(matriz[0]) = quantidade de colunas
        while matriz[i][j] != matriz[j][i] and simetria:
            simetria = False

print(simetria)