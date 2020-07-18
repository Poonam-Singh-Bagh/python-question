'''Q.5 Write a program to store the names of 25 people in your classroom, in reverse order.'''
i=0
names=[]
while i<4:
    name=input("enter student name: ")
    names.append(name)
    i=i+1
b=len(names)-1
while b > -1:
    print (names[b])
    b=b-1