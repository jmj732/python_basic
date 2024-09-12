mymap = [[0 for _ in range(11)] for _ in range(11)]

for _ in range(1,11):
    row = list(map(int, input().split())) 
    mymap[_][1:11] = row
x = 2
y = 2
mymap[y][x] = 9
while True:
    if mymap[y][x + 1] != 1 and mymap[y][x + 1] != 2:
        mymap[y][x + 1] = 9
        x += 1
    elif mymap[y + 1][x] != 1 and mymap[y + 1][x] != 2:
        mymap[y + 1][x] = 9
        y += 1
    elif mymap[y][x + 1] == 2:
        mymap[y][x + 1] = 9
        break
    elif mymap[y + 1][x] == 2:
        mymap[y + 1][x] = 9
        break
    else:
        break
    
for i in range(1,11):
    for j in range(1,11):
        print(mymap[i][j],end=" ")
    print('')