''' Q.6 Write a program to print  n even numbers, which number user will give.
Take a user input which number would be given by user, you have to print that many even numbers.'''
i=2
user=int(input("enter a number"))
while i <= user*2:
    if i%2==0:
        print (i)
    i=i+1
