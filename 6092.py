n = input()
ls = []
myls = [0] * 23
ls = input().split()
for i in ls:
    myls[int(i) - 1] += 1
for i in range(23):
    print(myls[i],end=" ")