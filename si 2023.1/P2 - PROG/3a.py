def funcao(n):
    if n <= 0:
        raise ValueError("Fora do intervalo permitido")
    
    s = 0

    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    
    return s

try:
    n = int(-9)
    print(f"Resultado: {funcao(n)}")
except ValueError as e:
    print(f"{e}!")