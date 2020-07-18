'''Q. 14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"'''

string = "The quick brown fox jumps over the lazy dog"
sentence = string.lower()
letter = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(letter)):
    if letter[i] not in sentence:
        print ("Is not a Pangrams")
        break
else:
    print ("Is a Pangrams")
    