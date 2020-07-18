for row in range (6):
    for col in range (7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print ("*",end=" ")
        elif (row==2 and col==2):
            print ("M",end=" ")
        elif row==2 and (col==3 or col==4):
            print ("A",end=" ")
        else:
            print (" ",end=" ")
    print (" ")
print ("I LOVE YOU")