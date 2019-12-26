n = input ("Ingrese un numero: ")
res = n % 2 
res2 = n % 4
if res > 0 : 
	print ('Usted ha ingresado un numero impar')
else :
	print ('Usted ha ingresado un numero par')
if res2 % 4 == 0 :
	print ('Su numero es multiplo de 4')
print "__________________________________________________"
print "Ahora comprobemos si dos numeros son divisibles :D"
chek = input ("Ingrese el primer numero (dividendo): ")
num = input ("Ingrese el segundo numero (divisor): ")
x = chek % num
if x > 0 :
	print 'El numero ', chek, 'no es divisible por ', num
else : 
	print 'El numero ', chek, 'es divisible por ', num
	
