'''Q.2 Strong number'''
user = input("Enter a number: ")
number = list(user)
sum = 0
for i in number:
    num=int(i)
    f = 1
    for i in range(num,0,-1):
        f=f*i
    sum=sum+f
if int(user) == sum:
   print(user, "is a Strong number") 
else:
    print(user, "is not a Strong number")


