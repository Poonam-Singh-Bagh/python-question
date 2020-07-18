'''Sorting in nested list'''
list = [[3,5,1,6,7],[8,2,9,7,4]]
i=0
while i<len(list):
	j=0
	while j<len(list[i]):
		k=0
		while k<len(list[i])-1:
			if list[i][k] < list[i][k+1]:
				list[i][k],list[i][k+1]=list[i][k],list[i][k+1]
			else:
				list[i][k],list[i][k+1]=list[i][k+1],list[i][k]
			k=k+1
		j=j+1
	i=i+1
print (list)