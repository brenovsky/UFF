l = [1, 4, 7, 3, 5, 8]
i = 3
o = 9

l2 = l[i:]
l[i] = o
l[i + 1:] = l2

print(l)