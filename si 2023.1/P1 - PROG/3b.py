mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        mysum += 10
        print(mysum)
    mysum += 1
print(mysum)