n = int(input())
lap = []
price = []
q = []
for i in range(n):
    lap = lap + input().split()

for i in range(2*n):
    if i % 2 == 0:
        price = price + (lap[i].split())
    else:
        q = q + lap[i].split()
for i in range(len(price)):
    price[i]=int(price[i])
for i in range(len(q)):
    q[i]=int(q[i])
coun = 0
for i in range(n-1):
    if ((price[i] < price[i+1]) and (q[i] > q[i+1])) or ((price[i] > price[i+1]) and (q[i] < q[i+1])) :
        print("happy irsa")
        coun =1
        break
    elif ((price[i] > price[i+1]) and (q[i] < q[i+1])) or ((price[i] < price[i+1]) and (q[i] > q[i+1])) :
        print("happy irsa")
        coun = 1
        break
if coun == 0:
    print("poor irsa")
