sen = int(input())
bozorg1= 10
bozorg2= 10
while sen <= 90 and sen >= 10 and sen!= -1:
    sen = int(input())
    if sen > bozorg2:
        bozorg2 = sen
        if bozorg2 > bozorg1:
            sen = bozorg1
            bozorg1 = bozorg2
            bozorg2 = sen
print(bozorg1,bozorg2)