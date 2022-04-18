aria = str(input())
a = 0
b = 0
for i in range(len(aria)):
    if aria[i] == aria[i].lower():
        a += 1
    elif aria[i] == aria[i].upper():
        b += 1
if a >= b:
    print(aria.lower())
else:
    print(aria.upper())
