# Very good!!!!
# DEAL: think about this solution using functions please

import random
key_number = random.randint(1, 10)
on_game = 'y'
guesses = 1
while on_game == 'y':
    user_number = int(input('Type a number: '))
    if user_number == key_number:
        print('Wow Congratulations!!! Thats Exactly the number..You win in ', guesses, 'guess(es)')
        on_game = input('Play again? (y , n , exit) ')
    elif user_number < key_number:
        on_game = input('Too low...Try again? (y , n , exit) ')
        guesses = guesses + 1
    elif user_number > key_number:
        on_game = input('Too high...Try again? (y , n , exit) ')
        guesses = guesses + 1
    if on_game == 'y':
        on_game = 'y'
    elif on_game == 'n':
        on_game = 'n'
    if on_game == 'exit':
        on_game = 'n'
