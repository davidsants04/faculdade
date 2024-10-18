import os

os.system('cls')

def media (n1=float,n2=float):#Funçao e suas variaveis que serão usada a que vai ser chamada nos codigos
    soma=n1+n2#variaveis da função
    med=soma/2#variaveis da função,,, a que tem que ser retornada neste caso
    return med    #o resultado da função oque tem que ser chamado no caso a variavel com o resultado que voçe deseja

valor1=float(input("digite a primeira nota :")) 
valor2=float(input("digite a segunda nota :")) 

mee = media(valor1, valor2) 

print() 

if mee <7: 
    print("\033[31m Reprovado fela\033[m") 
else: 
    print("\033[32mAprovado\033[m") 






#print(media(8,7))
#print(media(n1=valor1,n2=valor2))   #Assim tambem funciona mas usando mais variaveis..
#print(media(valor1,valor2))    #mode de se usar a função... 
