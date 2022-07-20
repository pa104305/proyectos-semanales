# -*- coding:utf-8 -*-

# Declaramos la funcion reto() que contiene el codigo necesario para el reto
def reto():
    # generamos variables para guardar el input de las palabras ingresadas
    palabra = input("Ingrese una palabra > ")
    anagrama = input("Ingrese el anagrama de la palabra anterior > ")
    # generamos listas vacias para después almacenar el desgloce de las palabras por letra
    letras_palabra = []
    letras_anagrama = []
    # generamos la lista comparacion la cual nos permite guardar las letras que coinciden entre
    # las palabras anteriores para asi poder declarar si es un anagrama o no
    comparacion = []

    # declaramos la funcion separator() para separar mediante bucles for las letras de las palabra
    # ingresadas y agregarlas a una lista
    def separator():
        for letter in palabra:
            letras_palabra.append(letter)
        for letter in anagrama:
            letras_anagrama.append(letter)
    
    # generamos la funcion comparator que inicia un bucle for para comenzar a iterar sobre las letras
    # de la lista letras_palabra y guardarlas en una variable temporal (letter_a), y llamar a la funcion
    # qeu terminara la comparacion
    def comparator():
        for letter_a in letras_palabra:
            first(letter_a)
        if (len(letras_palabra)) == len(comparacion):
            print("{} es un anagrama de {}".format(anagrama, palabra))
        else:
            print("no es un anagrama")
    
    # declaramos la variable first la cual necesita como argumento la variable temporal del bucle que la
    # llamos para compararla con su variable temporal y ver si son letras iguales, si estas son iguales
    # se agregan a una lista si son diferentes no, hasta que se comparen dos letras iguales para, despues
    # determinar si es un anagrama o no
    def first(letter_a):
        for letter_b in letras_anagrama:
            if letter_a == letter_b:
                comparacion.append(letter_a)
                print("{} | {}".format(letter_a, letter_b))
                letras_anagrama.remove(letter_b)
                return
    
    # Llamamos a la funcion separator() para separar las letras de las palabras introducidas
    separator()
    # Llamamos a la funcion comparator() para comparar las letras anteriores
    comparator()

reto()
