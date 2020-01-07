"""
Exercise 11
Ask the user for a number and determine whether
the number is prime or not. (For those who have
forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer
to Exercise 4 to help you. Take this opportunity
to practice using functions, described below.
"""


def prime_number(a):  # Defining a function that return if one number is prime or not
    """The rigth PEP8 way is this.

    Using two lines literal description (I dont remember the right name)
    It says that you should always do it. When you declare a function you add
    a description like this. Describing what the function does, and what the
    parameters are for. The first line is like a tittle, and it should be short
    And then you add this description. The blank line is also important between
    the tittle and this description :D. It could seem like a 'boberia' but is
    very useful. For instance, using pycharm and other IDE, when you type
    the name of the function and you put the mouse arrow over you will see this
    description. Test it, put the mouse over the name in line 40 and you see :D
    """
    if a == 0:
        is_prime = False
    if a == 1:
        is_prime = False
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
    return is_prime


prime = int(input('Type a number: '))
prime_number(prime)
if prime_number(prime) is True:
    print('Your number is prime')
else:
    print("Your number isn't prime")
