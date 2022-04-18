l = input().split()
for i in range(len(l)):
    l[i]=int(l[i])
l.sort()
l0 = (l[1]-l[0])+(l[2]-l[0])
l1 = (l[1]-l[0])+(l[2]-l[1])
l2 = (l[2]-l[0])+(l[2]-l[1])
l = [l0,l1,l2]
l.sort()
print(l[0])