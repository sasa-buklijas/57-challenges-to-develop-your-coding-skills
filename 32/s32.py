import random

count = 0 
while True:
    count += 1
    
    if count == 1:
        print 'Let\'s play Guess the Number.'
        l = int(raw_input('Pick a difficulty level (1, 2, or 3): '))

        d = {1:10, 2:100, 3:1000}
        urn = d[l]
        rn = random.randint(1, urn)
        
        n = int(raw_input('I have my number. What\'s your guess? '))

    if n == rn:
        print 'You got it in %d guesses!' % count
        
        n = raw_input('Play again? ')
        
        if n == 'n':
            print 'Goodbye!'
            break
        else:
            count = 0
    elif n > rn:
        n = int(raw_input('Too high. Guess again: '))
    elif n < rn:
        n = int(raw_input('Too low. Guess again: '))

    
