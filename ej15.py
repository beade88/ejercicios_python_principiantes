"""
Exercise 15
Write a program (using functions!) that asks the user for a
long string containing multiple words. Print back to the
user the same string, except with the words in backwards order.
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""

# Good, very good.
# Study the difference between use 'reverse' and 'reversed'

def reverse_sentence(sentence):
    sentence2 = sentence.split(' ')
    sentence3 = []
    for i in reversed(sentence2):
        sentence3.append(i)
    return ' '.join(sentence3)


my_sentence = input('Type a sentence: ')
print(reverse_sentence(my_sentence))
