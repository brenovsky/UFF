n = int(input('input a number: '))
triangular = False
for i in range(n):
    if i ** 2 + i == 2 * n:
        triangular = True
        break
if triangular == True:
    print(f'{n} é triangular')
else:
    print(f'{n} não é triangular')


#código antigo
#n = int(input('input n: '))
#triangular = False
#i = 1
#while n > i and triangular == False:
#    tri = (i * (i + 1))/2
#    if tri == n:
#        triangular = True
#    i += 1
#    if tri > n: # se tri > n, o código quebra
#        i = n + 1
#if triangular == False:
#    print(f'{n} não é triangular')
#else:
#    print(f'{n} é triangular')