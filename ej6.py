'''
Exercise 6
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
print('This program returns you if your word is a palidrome or not')
word = input('Type a word: ')
word1 = []
a = 0
for p in reversed(word):
	word1.append(p)
for x in range(0, len(word)):
	if word[x] == word1[x]:
		a = a + 1
if a == len(word):
	print('Your word is palindrome')
else:
	print('Your word is not palindrome')
	
