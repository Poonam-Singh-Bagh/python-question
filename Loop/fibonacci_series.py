'''Q.5 if the user will give 100 it will print till the number less than 100 fibonacci series.'''
user = int(input("Enter a number: "))
a=0
b=1
if user == 1:
    print (a)
else:
    print (a)
    print (b)
    for i in range(2,user):
        c=a+b
        a=b
        b=c
        if c > user:
            break
        else:
            print(c)
