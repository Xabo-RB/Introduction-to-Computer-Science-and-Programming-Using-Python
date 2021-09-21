def isWordGuessed(secretWord, lettersGuessed):
    import numpy as np
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    contador = 0
    tamano = np.zeros(len(lettersGuessed))
    
    #Delete repeated elements
    lettersGuessed = set(lettersGuessed)
    lettersGuessed = list(lettersGuessed)
    
    #Cover all unique elements in letterGuessed and fill out the corresponding
    #item in tamano with 1. If there are letters repeated in the word, are added 1 for 
    #each repetition
    
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if secretWord[j] == lettersGuessed[i]:
                #contador = contador + 1
                tamano[i] = tamano[i] + 1
                #break
            
    #Check if all the letters in secretword were guessed        
    contador = sum(tamano)
    if contador == len(secretWord):
        return True#, contador, tamano
    else:
        return False#, contador, tamano
    

    
                
    