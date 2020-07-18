'''Q.1 Dictionary - To print table'''
user = int(input("enter a number"))
table = {}
i=1
while i <= user:
	list = []
	j=1
	while j <= 10:
		list.append(i*j)
		j=j+1
	table[i] = list
	i=i+1
print (table)
