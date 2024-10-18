import os
os.system('cls')

def funcaoSeparar(numerico:float,caracter:str):
    cont=0
    while cont <len (caracter): #len só ve comprimento de variaveis iteraveis("exemplo str ,numero só se declarar str"
        print(caracter[cont])
        cont+=1   
    if numerico %  2 ==0:
        print(f"O numero {numerico} é um numero par")
    else:
        print(f"O {numerico} é um numero é impar")    



palavra=input("DIGITE UMA FRASE :")
numeros=float(input("digite um numero :"))


funcaoSeparar(numeros, palavra)

