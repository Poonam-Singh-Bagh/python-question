'''Q.7 Remove duplicate keys''' 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }

for key in dic:
	if key in dic:
		del key
print(dic)

dict={}
for key, value in dic.items():
	if key in dict:
		break	
	else:
		dict[key] = value
print(dict)