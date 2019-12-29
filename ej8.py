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

