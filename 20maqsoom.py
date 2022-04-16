acount1 = 0
acount2 = 0
b = 0
def maq(a):
    countmaq = 1
    for i in range(1,a):
        if a % i == 0:
            countmaq+=1
    return(countmaq)
for i in range(0,20):
    a =int(input())
    acount1= maq(a)
    if acount2 < acount1:
        b = a 
        acount2 = acount1
print(b,acount2)    
  
    



