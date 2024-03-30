def fatorial(x):
    P = 1
    for i in range(2, x + 1):
        P *= i
    return P

print(fatorial(int(input())))