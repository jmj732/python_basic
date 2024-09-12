mymap = [[0 for _ in range(20)] for _ in range(20)]

for _ in range(1,20):
    row = list(map(int, input().split())) 
    mymap[_][1:20] = row

num = input()
num = int(num)

for k in range(num):
    x, y = map(int, input().split())
    
    for i in range(1, 20):
        mymap[i][y] = 1 - mymap[i][y]
    
    for j in range(1, 20):
        mymap[x][j] = 1 - mymap[x][j]
    

for i in range(1,20):
    for j in range(1,20):
        print(mymap[i][j],end=" ")
    print('')