'''Q.9 Take 10 names of students and marks and add them in a dictionary.'''
dictionary = {}
i = 0
while i <= 10:
	Name = input("Enter student name: ")
	Marks = input("Enter student's marks: ")
	dictionary[Name] = Marks
	i=i+1

print(dictionary)
