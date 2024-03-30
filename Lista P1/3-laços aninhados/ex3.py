def intocavel(x):
    for i in range(2, x ** 2):
        j = 1
        divisores = []
        while j <= i // 2:
            if i % j == 0:
                divisores.append(j)
            j += 1
        if sum(divisores) == x:
            return False
    return True

k = int(input('input k: '))
i = 2
c = 1
while k > 0:
    if intocavel(i) == True:
        print(f'{c}: {i}')
        k -= 1
        c += 1
    i += 1