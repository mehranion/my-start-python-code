sara = str(input())
hsara = int(sara.find('h'))
esara = int(sara.find('e'))
llsara = int(sara.find('ll'))
osara = int(sara.find('o'))
if hsara == -1 or esara == -1 or llsara == -1 or osara == -1:
    print("NO")
else:
    hello = sara[hsara] + sara[esara] + sara[llsara] + sara[llsara] + sara[osara]
    if hello == "hello":
        print("YES")
    else:
        print("NO")


