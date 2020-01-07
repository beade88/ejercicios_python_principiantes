"""
Exercise 13
Write a program that asks the user how many Fibonnaci
numbers to generate and then generates them. Take this
opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence
is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the
sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
list_length = int(input('Type a number: '))


def fibonnaci_list(a):
    fibo = [1, 1]
    for i in range(0, a):
        if i > 1:
            fibo.append(fibo[i-1] + fibo[i-2])
    return fibo


print('Your Fibonnaci seqence is: ', fibonnaci_list(list_length))


# VERY GOOD!!!!
