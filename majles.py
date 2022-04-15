sen = int(input())
bozorg = sen
while sen <= 90 and sen >= 10 and sen != -1 :
    sen = int(input())
    if sen > bozorg:
        bozorg = sen
if bozorg <= 90 and bozorg >= 10 and bozorg != -1:
    print(bozorg)

