'''Q.4 fibonacci series'''
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
        print(c)