h,b,c,s = map(int,input().split())

result = h/8*b*c*s
result /= 1024
result /= 1024

print("%.1lf MB" % result)