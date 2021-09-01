"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'

count = 0
palabra = 'bob'
for i in range(len(s)+1):
    if s[i:i+3] == 'bob':
        count = count + 1
    if i == (len(s)-2):
        break

print('Number of times bob occurs is: ' + str(count))
    