def hazf(horoof):
    horoof = horoof.lower()
    horoof = horoof.replace("a","")
    horoof = horoof.replace("o","")
    horoof = horoof.replace("i","")
    horoof = horoof.replace("e","")
    horoof = horoof.replace("u","")
    horoof = horoof.replace(" ","")
    horoof = horoof.replace("  ","")
    horoof = horoof.replace("",".")
    horoof = horoof[0:-1]
    return horoof
horoof = input()
horoof = hazf(horoof)
print(horoof)


