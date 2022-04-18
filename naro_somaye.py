def tartib(jam):
    jam = jam.replace("+","")
    coun1=0
    coun2=0
    coun3=0
    for i in range(len(jam)):
        if jam[i] == "1":
            coun1+=1
        elif jam[i] == "2":
            coun2+=1
        elif jam[i] == "3":
            coun3+=1
    jam= coun1*"1" + coun2*"2" + coun3*"3"
    jam = jam.replace("","+")
    jam = jam[1:-1]
    return jam
jam = str(input())
jam = tartib(jam)
print(jam)