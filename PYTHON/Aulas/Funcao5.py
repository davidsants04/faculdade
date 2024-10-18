import os
import random


def semana ():
    seman=random.randint(1,7)
    match seman:
        case 1:
            print("Segunda")
        case 2:
            print("Terça")
        case 3:
            print("Quarta")
        case 4:
            print("Quinta")
        case 5:
            print("Sexta")
        case 6:
            print("Sabado")
        case 7:
            print("domingo")
    return 

semana()

