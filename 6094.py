n = input()
ls = []
min = 1000
ls = input().split()
for i in ls:
    if min > int(i):
        min = int(i)
print(min)