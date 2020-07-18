'''Q.3 Armstrong number'''
user = input("Enter a number: ")
number = list(user)
sum = 0
for i in range(len(number)):
    sum=sum+int(number[i])**3
if int(user) == sum:
    print(user, "is a Armstrong number")
else:
    print(user, "is not a Armstrong number")
