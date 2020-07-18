''' Q.2 Write a program to print oddd and even separately.'''
i=2
even=[]
odd = []
while i<10:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i=i+1
print (even)
print (odd)