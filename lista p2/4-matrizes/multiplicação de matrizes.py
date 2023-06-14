A = [[2, 0, 1], [5, 3, 2]]
B = [[4, 3], [1, 2], [0, 6]]

nova_matriz = []

for i in range(len(A)): #percorre pelas linhas de A
    resultado_soma = []
    for j in range(len(B[0])): #percorre pelas colunas de B
        soma = 0
        for k in range(len(A[0])): #itera coluna/linha de A com linha/coluna de B
            soma += A[i][k] * B[k][j]
        resultado_soma.append(soma)
    nova_matriz.append(resultado_soma)

for i in range(len(nova_matriz)):
    print(nova_matriz[i])