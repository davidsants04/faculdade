import os 

os.system('cls') 

def medianota ( lista:list ): 
    soma= 0 
    for valor in lista: 
        soma = soma + valor 
    x = soma / len(lista)  
    return x 

media= [6,7,3,9,10]

result=(medianota(media)) #Primeiro o nome da definição (DEF) e depois o nome da variavel que sera executado a definição..

if result >7:
    print( f"Sua nota foi \033[32m{result}\033[m] e voçê foi Aprovado !!" ) 
else: 
    print( f"Sua nota foi \033[31m{result}\033[m e voçê foi Reprovado !!" ) 
