'''Armstrong number'''

a=1
b=0
c=a
while(a<=999):
    while(c>0):
        digit=c%10
        b=b+digit**3
        c=c//10
    if(a==b):
       print("Armstrong")
    else:
       print("Not Armstrong ")
a=a+1
