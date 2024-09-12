w, h = map(int,input().split())
n = input()
mymap = [[0 for _ in range(100)] for _ in range(100)]

for i in range(int(n)):
   l, d, y, x = map(int,input().split())
   
   for j in range(l):
      if d == 0: 
          mymap[y][x] = 1
          x += 1
      else:
          mymap[y][x] = 1
          y += 1

for i in range(w):
    for j in range(h):
        print(mymap[i + 1][j + 1],end=" ")
    print('')