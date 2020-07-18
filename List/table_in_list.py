'''Table in list'''
user = int(input("enter a number: "))
table = []
i=1
while i <= user:
	list = []
	j=1
	while j <= 10:
		list.append(i*j)
		j=j+1
	table.append(list)
	i=i+1

print (table)