n =int(input())
l = input().split()
l2 = l[0:n]
coun = 0
for i in range(len(l2)):
    l2[i]=int(l2[i])
    if l2[i] <= 2:
        coun += 1
print(coun // 3)


