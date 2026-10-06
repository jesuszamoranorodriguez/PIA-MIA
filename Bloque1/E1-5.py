# Adivina el número: bucle while con intentos limitados y pistas mayor/menor.

import random

numero = random.randint(1, 100)
max_intentos = 5
intentos = 0
while (True):
    intentos+=1
    num_user = int(input("Introduzca un número del 1 al 100: "))
    if(num_user == numero):
        print("Has acertado el número!!! Has ganado el juego!")
        break;
    elif(num_user > numero):
        print("Te has pasado... Prueba a bajar esa cifra!")
        if(max_intentos==intentos):
            print("Te has quedado sin intentos")
            break;
    elif(num_user < numero):
        print("Tiene pinta que te has quedado corto... Y si subes ese número?")
        if(max_intentos==intentos):
            print("Te has quedado sin intentos")
            break;
    