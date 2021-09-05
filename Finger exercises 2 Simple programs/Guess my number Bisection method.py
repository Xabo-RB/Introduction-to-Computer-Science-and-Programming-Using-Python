#secret_number = int(eval(input('Please think of a number between 0 and 100!')))
print('Please think of a number between 0 and 100!')

high = 100
low = 0

ans = (high - low)/2

while True:
    ans = int((high + low)/2)
    rango = input('Is your secret number ' + str(ans) + '?\nEnter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    
    if rango == 'c':
        break
    elif rango == 'h':
        high = ans
    elif rango == 'l':
        low = ans
    else:
        print('Sorry, I did not understand your input.')
        
print('Game over. Your secret number was: ' + str(ans))
        





