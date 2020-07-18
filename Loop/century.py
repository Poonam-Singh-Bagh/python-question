'''Century'''

year = int(input("enter a year"))
sum=0
i=0
while i < year:
    if i % 100 == 0:
        sum=sum+1
    i=i+1
print (sum)