k = int(input('input a number: '))
n = 6
while k > 0:
    s = 0
    i = 1
    while i <= n // 2:
        if n % i == 0:
            s += i
        i += 1
    if s == n:
        print(n)
        k -= 1
    n += 1