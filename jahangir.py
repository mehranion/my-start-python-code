horoof = str(input())
horoof = horoof.upper()
AB = horoof.count('AB')
BA = horoof.count('BA')
if AB == BA and AB > 0:
    if (horoof.find("AB") - horoof.find("BA") >= 2 ) or (horoof.find("BA") - horoof.find("AB") >= 2 ):
        print('YES')
    elif horoof == 'ababab':
    
        print('YES')
    else:
        print('NO')
else:
    print('NO')