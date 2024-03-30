def concatenado(x):
    if len(x) % 2 != 0:
        return False
    pulo = len(x) // 2
    for i in range(pulo):
        if x[i] != x[i + pulo]:
            return False
    return True
  
string = input()
print(concatenado(string))