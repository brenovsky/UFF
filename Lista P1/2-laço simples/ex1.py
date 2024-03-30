n = 1
positivos = 0
negativos = 0
while n != 0:
    n = int(input('input n: '))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print(f'{positivos} números positivos e {negativos} números negativos')