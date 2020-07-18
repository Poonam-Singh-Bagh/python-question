'''To check an element is present in list'''
user = int(input("enter a number"))
list = [[0,1,2,3,4],[5,6,7,8,9]]
i=0
while i <= len(list)-1:
    if user  in list[i]:
        print (user,"is present")
        break
    else:
        i=i+1  
else:
    print (user,"is not present")


''' In for loop'''
user = int(input("enter a number"))
list = [[0,1,2,3,4],[5,6,7,8,9]]
for i in range(len(list)):
    if user in list[i]:
        print ("in")
        break
else:
    print ("not")
