n, m, h = map(int,input().split())
if n < m and n < h:
    print(n)
elif m < n and m < h:
    print(m)
else:
    print(h)
