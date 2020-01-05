"""
Exercise 16
Write a password generator in Python.
Be creative with how you generate
passwords - strong passwords have a mix
of lowercase letters, uppercase letters,
numbers, and symbols. The passwords
should be random, generating a new password
every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
    Ask the user how strong they want their
    password to be. For weak passwords,
    pick a word or two from a list...

"""

pass_length = int(input('Type the length of your password: '))


def random_password_system(length):
    import random
    password_word = []
    cont = 0
    for i in range(0, pass_length):
        char0 = random.choice('0123456789')
        char = random.choice('abcdefjhijklmnopqrstuvwxyz')
        char2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        char3 = random.choice("*./,-_!#$@%&()[]{}")
        if cont == 0:
            password_word.append(char)
            cont = cont + 1
        elif cont == 1:
            password_word.append(char2)
            cont = cont + 1
        elif cont == 2:
            password_word.append(char3)
            cont = cont + 1
        elif cont == 3:
            password_word.append(char0)
            cont = 0
    return ' '.join(password_word)


pass_system_activation = 'y'
while pass_system_activation == 'y':
    print(random_password_system(pass_length))
    pass_system_activation = input('You need a new password? (y or n): ')
    if pass_system_activation == 'n':
        break
