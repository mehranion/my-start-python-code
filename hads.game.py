import random
x = 1
y = 99
personaction = 'start'
while personaction != "d":
    bot_hads = random.randint(x,y)
    print (bot_hads)
    personaction = input()
    if personaction == "d":
        break
    elif personaction == "k":
        y = bot_hads -1
    
    elif personaction == "b":
        x = bot_hads + 1
