
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
 your program should print:
 """

#s = input('Introduce un string: ')
s = 'azcbobobegghakl'

numVocales = 0
for char in s :
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
           numVocales += 1

print('Number of vowels: ' + str(numVocales))    