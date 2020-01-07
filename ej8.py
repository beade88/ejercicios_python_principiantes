'''
Exercise 8
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message
of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

# Very Very Very good.
# No PEP8 error, no spanish words, no english errors,
# good variables naming...no comments here :D

# But, as nothing is perfect, come on, lets thing another solution :D
# I dont know, I let it open to your imagination :D
# I just dont like to many validations here :D (I mean there are 9
# if - else sentences because the binary combinations)
# It should exist another way (I dont know exactly how to do it) :D
# But I will think about it and let you know :D
print('Lets to play Rock Paper Scissors')
print('R means Rock, P means Paper and S means Scissors')
game = 'y'
while game == 'y':
    user1 = input('Player 1 --- Type R, P, S: ')
    user2 = input('Player 2 --- Type R, P, S: ')
    if user1 == 'R' and user2 == 'R':
        print('Its a draw!!!')
    elif user1 == 'R' and user2 == 'P':
        print('Player 2 wins!!!')
    elif user1 == 'R' and user2 == 'S':
        print('Player 1 wins!!!')
    if user1 == 'P' and user2 == 'R':
        print('Player 1 wins!!!')
    elif user1 == 'P' and user2 == 'P':
        print('Its a draw!!!')
    elif user1 == 'P' and user2 == 'S':
        print('Player 2 wins!!!')
    if user1 == 'S' and user2 == 'R':
        print('Player 2 wins!!!')
    elif user1 == 'S' and user2 == 'P':
        print('Player 1 wins!!!')
    elif user1 == 'S' and user2 == 'S':
        print('Its a draw!!!')
    game = input('Play again ("y" or "n"): ')
