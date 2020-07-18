def Year():
    year = int(input("enter a year"))
    century=0
    i=0
    while i < year:
        if i % 100 == 0:
            century=century+1
        i=i+1
    return century
    
    
print (Year())