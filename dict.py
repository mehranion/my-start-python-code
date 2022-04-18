jomleh = 'Whether or not maxsplit was defined, the results were the same. For both the above cases only 3 inputs (not more or less can be provided corresponding to defined variables!)'

shomar = dict()
for i in jomleh:
    if i in shomar:
        shomar[i] += 1
    else:
        shomar[i] = 1
print(shomar)