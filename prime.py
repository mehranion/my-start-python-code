adad = int(input())
k = 0
if (adad == 1) or (adad == 2):
    print('prime')
    k = 1
for i in range(2,adad):
    if (adad % i) == 0:
        print('not prime')
        k = 1
        break
if k == 0:
    print('prime')
