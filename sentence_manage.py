"""
Mira, toma este : supón la cadena
‘esta es una cadena de texto’ conviértela a
‘Esta Es Una Cadena De Texto’ todas la
letra inicial mayúscula. Simple pero usarás
tres funciones básicas para procesar strings :)
Q son split, join, list comprehension y capitalice
"""

sentence_1 = 'this is a text string'


def sentence_manage(sentence):
    list_1 = sentence.split()
    list_2 = [list_1[i].capitalize() for i in range(len(list_1))]
    list_3 = ' '.join(list_2)
    print(list_3)


sentence_manage(sentence_1)
