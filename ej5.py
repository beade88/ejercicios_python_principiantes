'''
Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''
#Este esta implementado con python3 desde el inicio :D
print("Lista 1")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
d = int(input("Ingrese un numero: "))
e = int(input("Ingrese un numero: "))
f = int(input("Ingrese un numero: "))
lista1 = [a, b, c, d, e, f]
print("La lista 1 es: ")
print(lista1)
print("Lista 2")
g = int(input("Ingrese un numero: "))
h = int(input("Ingrese un numero: "))
i = int(input("Ingrese un numero: "))
j = int(input("Ingrese un numero: "))
k = int(input("Ingrese un numero: "))
lista2 = [g, h, i, j, k]
print("La lista 2 es: ")
print(lista2)
lista3 = []
print("Los numeros que coinciden en ambas listas son: ")
for x in lista2 :
	if x in lista1 :
		lista3.append(x)
print(lista3)
