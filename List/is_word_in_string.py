'''Check whether the word is present in a string.'''

user = input("enter a word: ")
text1 = "poonam is giving interview"
text=text1.split(" ")
i=0
count=0
while i < len(text):
    if user == text[i]:
        count=count+1
    i=i+1
print (user, "is coming",count, "times")
        