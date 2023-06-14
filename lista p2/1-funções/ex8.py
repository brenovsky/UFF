def primo(x):
    if x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    elif x < 2:
        return False
    elif x == 2:
        return True

n = int(input('input n: '))
s = 0
i = 2

while n > 0:
    if primo(i) == True:
        s += i
        n -= 1
    i += 1

print(s)