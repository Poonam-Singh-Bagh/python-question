'''Q.1 Pattern
1

121

12321

1234321

123454321 '''
i=0
while i < 5:
    j=1
    while j <= i:
        print(j,end="")
        j=j+1
    k=j    
    while k >= 1:
        print(k,end="")
        k=k-1
    print("\n")
    i=i+1