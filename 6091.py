n,m,k = map(int,input().split())
day = 1
while True:
    if day % n == 0 and day % m == 0 and day % k == 0:
        break
    day += 1
print(day)