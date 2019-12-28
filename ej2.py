'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
n = int (input ("Ingrese un numero: "))
res = n % 2 
res2 = n % 4
if res > 0 : 
	print ('Usted ha ingresado un numero impar')
else :
	print ('Usted ha ingresado un numero par')
if res2 % 4 == 0 :
	print ('Su numero es multiplo de 4')
print ("__________________________________________________")
print ("Ahora comprobemos si dos numeros son divisibles :D")
chek = int (input ("Ingrese el primer numero (dividendo): "))
num = int (input ("Ingrese el segundo numero (divisor): "))
x = chek % num
if x > 0 :
	print ('El numero ', chek, 'no es divisible por ', num)
else : 
	print ('El numero ', chek, 'es divisible por ', num)
'''
Importante...en este ejercicio ya transforme el codigo de python2 a python3, las dos diferencias que generaban error al compilar el codigo hecho con python2 con python3 fueron que ahora en python 3 print es una funcion y hay que ponerle () y lo otro fue que en python3 input es una cadena de texto, para poder usar los numeros tuve que convertir con int antes de input")
'''
	
