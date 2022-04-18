asami = str(input())
for i in range(0,9):
    asami = asami + " " +  str(input())
asami = asami.lower().title().split()
for i in range(0,10):
    print(asami[i])