w, h, rgb = map(int, input().split())
result = w*h*rgb/8
result /= 1024
result /= 1024

print("%.2lf MB" % result)