# -*- coding:utf-8 -*-
# Ceneeamos la funcion base
def reto():
    # Declaramos variable numeros para el conteo, t y c para multiplos de 3 y 5
    number = 1
    t = 3
    c = 5
    # Creamos el bucle y cuando numero sea mayor a 100 el bucle se detandra
    while number <= 100:
        # Iniciamos la condicional para definir si se imprime el numero actual, 
        # la palabra fizz, buzz o fizzbuzz segun sea el caso y aumentar las
        # variables segun la condicion que se apruebe
        if number == t and number == c:
            print("fizzbuzz")
            c = c + 5
            t = t + 3
        elif number == t:
            print("fizz")
            t = t + 3
        elif number == c:
            print("buzz")
            c = c + 5
        else:
            print(number)
        #print(number)
        # Siempre se aumenta la variable number, de lo contraria se generara un bucle infinito
        number += 1

# Llamamos a la funcion base
reto()