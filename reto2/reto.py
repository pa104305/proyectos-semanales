# -*- coding:utf-8 -*-

# Declaramos la funcion principal reto(), para tener todo nuestro codigo dentro de una funcion
def reto():
    # creamos un diccionario con dos parejas clave valor, f1 (fibonacci1) con valor 0 y
    # f2 (fibonacci2) con valor 1
    fibonacci = {"f1":0, "f2":1} # diccionario
    # creamos la funcion fib() donde se situara la variable contadora y el bucle correspondiente
    # while
    def fib():
        count = 0 # variable contadora
        while count <= 50: # bucle while para llevar acabo el calculo de la serie de fibonacci
            temp = fibonacci["f1"] + fibonacci["f2"] # variable donde se guarda la suma de los
            # dos ultimos numeros de fibonacci
            if count <= 50: # condicional if (innecesaria)
                print("{}. {}".format(count, fibonacci["f1"])) # print del f1 del diccionario
                # movimiento de los ultimos dos valores de fibonacci
                fibonacci["f1"] = fibonacci["f2"] # asignando f2 a f1 para que siga su reccorrido
                fibonacci["f2"] = temp # asignando el nuevo valor mas reciente a f2
            count += 1 # aumento de unidades del contador para evitar crear un bucle infinito
    fib() # llamada a funcion secundaria fib()
reto() # llamada a funcion principal reto()