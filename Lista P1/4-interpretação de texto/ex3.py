n = int(input("Insert n: "))
k = int(input("Insert the k position: "))
sequence = []
if k >= 1 and k <= n and n >= k and n <= 1000:
    for i in range(1, n + 1):
        if i % 2 != 0:
            sequence.append(i)
    for i in range(1, n + 1):
        if i % 2 == 0:
            sequence.append(i)
    print('Number in k position is', sequence[k - 1])
else:
    print("Interval error.")