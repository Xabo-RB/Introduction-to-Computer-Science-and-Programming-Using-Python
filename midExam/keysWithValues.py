##Write a Python function that returns a list of keys in aDict with the value target. 
##The list of keys you return should be sorted in increasing order. 
##The keys and values in aDict are both integers. (If aDict does not contain
# the value target, 
##you should return an empty list.)

##This function takes in a dictionary and an integer and returns a list.

"""
Hallar qué llaves tienen un determinado valor (target)
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    values = aDict.values()
    keysList = []
    if target in values:
        for i in aDict.keys():

            if aDict[i] == target:
                keysList.append(i)

                keysList.sort()

        return keysList
    else:
        return []
    
