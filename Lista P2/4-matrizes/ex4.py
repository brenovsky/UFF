#para 2ª ordem
#A = [[5, 3], [2, 4]]

#diagonal_1 = A[0][0] * A[1][1]
#diagonal_2 = A[0][1] * A[1][0]

#determinante = diagonal_1 - diagonal_2

#print(determinante)

#para 3ª ordem
A = [[2, 1, 1], [3, 1, 2], [1, -1, 0]]

x = A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1]
y = A[0][2] * A[1][1] * A[2][0] + A[0][0] * A[1][2] * A[2][1] + A[0][1] * A[1][0] * A[2][2]

determinante = x - y

print(determinante)