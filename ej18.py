"""
Exercise 18
Create a program that will play the “cows and bulls”
game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to
guess a 4-digit number. For every digit that the user
guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong
place is a “bull.” Every time the user makes a guess, tell
them how many “cows” and “bulls” they have. Once the user
guesses the correct number, the game is over. Keep track
of the number of guesses the user makes throughout teh game
and tell the user at the end.
Say the number generated by the computer is 1038. An example
interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull  ...
"""

import random


def cows_bulls_game(user_number):
    user_number_convert = [int(y) for y in str(user_number)]
    cows = 0
    bulls = 0
    key_number = random.randint(1000, 9999)
    str_number = [int(x) for x in str(key_number)]
    for i in range(0, len(user_number_convert)):
        if user_number_convert[i] == str_number[i]:
            cows = cows + 1
        else:
            bulls = bulls + 1
    list1 = [cows, bulls]
    return list1


number_typed = input('Type a 4 digits number: ')
print((cows_bulls_game(number_typed))[0], 'Cows and ', (cows_bulls_game(number_typed))[1], 'Bulls')
