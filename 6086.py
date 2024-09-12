max = input()
sum = 0
i = 1
while True:
    sum += i
    i += 1
    if(sum >= int(max)):
        break
print(sum)