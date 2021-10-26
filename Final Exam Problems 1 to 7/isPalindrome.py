"""
Write a Python function that returns True if aString is a palindrome
(reads the same forwards or reversed) and False otherwise. Do not use Python's
 built-in reverse function or aString[::-1] to reverse strings.

This function takes in a string and returns a boolean.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
"""
# function define
def isPalindrome(aString):
    # take length of aString in varaible l
    l=len(aString)
    # Run loop from 0 to l/2
    for k in range(0,int(l/2)):
    # compare the string characters from both end
        if(aString[k]!=aString[l-k-1]):
            return False
        return True