n = input()
ls = []
mymap = [[0 for _ in range(21)] for _ in range(21)]
for i in range(int(n)):
    x, y = map(int, input().split())
    ls.append([x,y])

for i in range(int(n)):
    mymap[ls[i][0]][ls[i][1]] = 1

for i in range(1,20):
    for j in range(1,20):
        print(mymap[i][j],end=' ')
    print('')