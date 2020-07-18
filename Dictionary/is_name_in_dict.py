'''Q.3 Check if the user is in dict, if yes print exist if not print not exist.
if input is “name” then output will be “exist”

If input is “class” then output will be “not exists”.'''

dict={"name":"Raju", "marks":56}
user = input("Enter key name: ")
for key, value in dict.items():
	if user in dict:
		print(user,"is exist in dict")
		break
else:
	print(user,"is not exist in dict")
