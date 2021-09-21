def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    # Python code to convert string to list character-wise
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
    # Driver code   
    wordFilling = Convert(secretWord)
    wordFilling1 = wordFilling
    
    for i in range(len(secretWord)):
        wordFilling1[i] = ' _ '
    
    #Delete repeated elements
    lettersGuessed = set(lettersGuessed)
    lettersGuessed = list(lettersGuessed)
    
    #Cover all unique elements in letterGuessed and fill out the corresponding
    #item in tamano with 1. If there are letters repeated in the word, are added 1 for 
    #each repetition
    
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if secretWord[j] == lettersGuessed[i]:
                wordFilling1[j] = secretWord[j] 
    
    wordFilling1 = ''.join(wordFilling1)
    
    return wordFilling1
