'''Q.15. Write a Python program that accepts a hyphen-separated sequence of words as 
input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

def paragraph():
    string = input("enter a sentence with hypen")
    sentence = string.split("-")
    sente = sorted(sentence)
    text = " "
    i=0
    R = len(sente) -1
    while i < len(sente):
        if i == R:
            text=text+sente[i]
        else:
            text=text+sente[i]+"-"
        i=i+1
    return (text)
    
    
print (paragraph())
