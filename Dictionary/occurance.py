'''Q.10 “MISSISSIPPI” count the occurancy of letter and make a dictionary 
where the letter would be key of dictionary and count would be value.'''
str = "MISSISSIPPI"
dictionary = {}
i = 0
while i < len(str):
	count = 0
	j = 0
	while j < len(str):
		if str[i] ==  str[j]:
			count = count + 1
		j=j+1
	dictionary[str[i]] = count
	i=i+1
print(dictionary)	