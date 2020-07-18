'''Q.1 Perfect number'''
user = int(input("Enter a number: "))
sum = 0
for i in range(1,user):
    if user % i == 0:
        sum=sum+i
if user == sum:
    print(user, "is a perfect numer")
else:
    print(user, "is not a perfect number")