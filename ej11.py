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
