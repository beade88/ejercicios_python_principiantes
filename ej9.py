"""
Exercise 9
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the
very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
"""

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
