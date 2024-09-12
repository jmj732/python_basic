n = input()
n = int(n)
ls = input().split()
myls = [0] * n
for i in range(n):
    myls[i] = ls[n - i - 1]
for i in range(n):
    print(myls[i], end=" ")


