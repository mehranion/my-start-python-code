emtiaz = 0
bord = 0
for i in range(30):
    sepid = int(input())
    if sepid == 1:
        emtiaz += 1
    if sepid == 3:
        emtiaz += 3
        bord += 1
print(emtiaz,bord)
