'''Q.4 Create a list of 10 numbers from the user and update each element.''' 
# of the list according to below rule,
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1
i = 0
list = []
updated_list = []
while i < 10:
    user = int(input("enter a no."))
    list.append(user)
    if user % 2 == 0:
        updated_list.append(user*100)
    else:
        updated_list.append(user*(-1))
    i = i + 1
print (list)
print (updated_list)