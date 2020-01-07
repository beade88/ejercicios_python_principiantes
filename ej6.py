'''
Exercise 6
Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

# I think that here you learned about PEP8 because
# you dont have any PEP8 error here :D
# Also all variables are very good named :D



# Very good!!!!!
# Now, new DEAL :D (sorry)
# What about a very very long word...lets say 1000 characters.
# With this solution you loop over the hole array, but, think one moment,
# thats not necessary. Because you go from the begining and from the end,
# comparing characters, so, when you get to the middle you dont need
# to keep going because you did that comparison before.
# If you compare until the middle, yo save 50% time.
# Also, if only one fails you can stop, because the word is not palind.
# Do you understand?
# So, fix this :D

print('This program returns you if your word is a palidrome or not')
word = raw_input('Type a word: ')
a = 0
p = len(word) - 1
for i in range(len(word)):
    if word[i] == word[p - len(word)]:
        a = a + 1
    p = p - 1
if a == len(word):
    print('Your word is palindrome')
else:
    print('Your word is not palindrome')

'''
for p in reversed(word):
	word1.append(p)
for x in range(0, len(word)):
	if word[x] == word1[x]:
		a = a + 1
if a == len(word):
	print('Your word is palindrome')
else:
	print('Your word is not palindrome')

'''
# PEP8 also says that only ONE blank line at the end of a file,


# Deal for you. Is possible make it using only one loop.
# Study about slicing in strings and try to do it.
# Just a hint: if you have a list (also happens in string and in all iterables)
# For example name = "Reinaldo" and you say name[0] you have 'R' and
# if you say name[-1] you have 'o', name[-2] is 'd' and so on :D
