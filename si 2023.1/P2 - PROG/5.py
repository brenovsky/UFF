def inferior(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] != 0 and i < j:
                return False
    return True

matriz = [[1, 0, 0], [1, 2, 0], [1, 2, 3]]

print(inferior(matriz))