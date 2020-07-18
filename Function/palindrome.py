'''Palindrome'''

def checkPalindrome(inputString):
    i=0
    n=1
    while i < len(inputString):
        if inputString[i]!=inputString[len(inputString)-n]:
            return (False)
            break
        n=n+1
        i=i+1
    else:
        return (True)


print (checkPalindrome('aabaa'))

