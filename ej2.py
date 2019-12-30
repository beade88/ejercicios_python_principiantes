'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd number
react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one
    number to divide by (check). If check divides evenly into num, tell that to the user.
    If not, print a different appropriate message.
'''

# I did Enter in many lines on your initial comments.
# Always try to do it for not to have to long lines.
# Is good to see every line with not to have to scroll right.

# n = int (input ("Ingrese un numero: "))

# About variables names, use more representatives names.
# Also fix some PEP8, like int() instead of int (),
# no need extra space between int and ()
number = int(input('Enter one number: '))

#res = n % 2
#res2 = n % 4
#if res > 0 :
#	print ('Usted ha ingresado un numero impar')
#else :
#	print ('Usted ha ingresado un numero par')

#if res2 % 4 == 0 :
#	print ('Su numero es multiplo de 4')

# Is good to declare variables, but in this case
# you can make the validation directly.
# Also PEP8 in print (). Remember, always a ()
# will go without space before.
if number % 2 == 0:
    print('You have entered an even number')
else:
    print('You have entered an odd number')

# I am not sure but I think that every even number is
# also divisible by 4, if this is true you can put
# this print inside even validation, I mean after line 42
if number % 4 == 0:
    print('Your number is divisble by 4.')

#print ("__________________________________________________")
#print ("Ahora comprobemos si dos numeros son divisibles :D")

print ("__________________________________________________")
print ("Lets check if two numbers are divisible :D")

# chek = int (input ("Ingrese el primer numero (dividendo): "))
# num = int (input ("Ingrese el segundo numero (divisor): "))
# x = chek % num

# Better var names, more descriptives.
# ALso PEP8 with spaces and '' in strings
first_number = int(input('Enter first number (dividend): '))
second_number = int(input('Enter second number (divisor): '))

# if x > 0 : # PEP8, blank space after 0 and : is wrong
# I also omited declaration por extra variable
if first_number % second_number > 0:
    # print ('El numero ', chek, 'no es divisible por ', num)
    # PEP8 after print, and also better using format.
    # Use format always you can :D
    print('Number {} is not divisible by {}'.format(first_number, second_number))
# else : PEP8, space after else :
else:
    # print ('El numero ', chek, 'es divisible por ', num)
    print('Number {} is divisible by {}'.format(first_number, second_number))


'''
Importante...en este ejercicio ya transforme el codigo de python2 a python3, 
las dos diferencias que generaban error al compilar el codigo hecho 
con python2 con python3 fueron que ahora en python 3 print es una funcion 
y hay que ponerle () y lo otro fue que en python3 input es una cadena de texto, 
para poder usar los numeros tuve que convertir con int antes de input")
'''
