"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
 program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've 
spent more than a few hours on this problem, we suggest that you move on to a 
different part of the course. If you have time, come back to this problem after 
you've had a break and cleared your head.
"""


s = 'azcbobobegghakl'
#s = 'abcbcd'

import numpy as np
tamano = np.zeros(len(s))

for i in range(len(s)):    
    substring = s[i]
    for j in range(i,len(s)-1,1):      
        if s[j] <= s[j+1]:
            substring = substring + s[j+1]
        else:
            break
    tamano[i] = len(substring)
    
#Posición de la primera letra donde se produce el substring
maximo = int(np.amax(tamano))
pos = np.where(tamano == maximo)
pos = int(pos[0][0])
pos_final = pos + maximo
sbstring = s[pos:pos_final]

print('Longest substring in alphabetical order is: ' + str(sbstring))