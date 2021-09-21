def getAvailableLetters(lettersGuessed):
    '''
    Printing Out all Available Letters:
        
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    abecedario = string.ascii_lowercase
    
    # Python code to convert string to list character-wise
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
    # Driver code   
    abecedario_list = Convert(abecedario)
    
    for i in range(len(lettersGuessed)):
        for j in range(len(abecedario_list)):
            if abecedario_list[j] == lettersGuessed[i]:
                abecedario_list[j] = ''
    
    abecedario = ''.join(abecedario_list)
    
    return abecedario

