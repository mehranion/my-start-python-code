from audioop import add


adad = int(input())
c = adad // 100
b = (adad % 100) // 10
a = (adad % 100) % 10
print((a*200)+(b*20)+(c*2))