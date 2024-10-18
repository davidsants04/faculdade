from jogo import sky
import random
import pyautogui as pa
import time
from datetime import datetime
import os
import sys


def verificarlogin(login,senha):
    if login=="david":
        if senha=="1234":
            print("\033[32mENTROU NO SISTEMA\033[m")
            return True
        else:
            return False
    else:
        print("falha usuario não encontrado.")
        return False        
while True:
    loguin=input("digite seu login :")
    senh=input("digite a sua senha :")
    if verificarlogin(loguin,senh):
        break
    else:
        pass    

def print_slow(text,delay=.06):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(delay)
    print()

os.system('cls')
print("\033[34m-=\033[m"*40)
print_slow("\033[32m Seja bem vindo ao sistema de tarefas \033[m")
pare=datetime.now()
print_slow(f"\033[36mDIA {pare.day}/{pare.month}/{pare.year} {pare.hour}:{pare.minute}\033[m")
print("\033[34m-=\033[m"*40)
print("""1-\033[33mIDADE\033[m
2-\033[33mAREA DE UM QUADRADO\033[m
3-\033[33mTABUADA\033[m
4-\033[31mVER NEYMAR SKILS\033[m
5-\033[33mPESQUISE SOBRE ALGO\033[m
6-\033[33mPEQUENO QUIZ..\033[m
7-\033[33mACERTE O NUMERO\033[m
8-\033[33mSIMULADOR DE RADAR\033[m
9-\033[33mSKYRIM 2.0 TESTE\033[m
10-\033[33mCADASTRAR USUARIO\033[m
0-\033[33mDESLIGAR PC\033[m""")
print("\033[34m-=\033[m"*40)
print_slow("Digite a opção desejada a partir da lista acima! ")
print("\033[34m-=\033[m"*40)
opcao=input("\033[34mopção :\033[m ")
print("\033[34m-=\033[m"*40)
if opcao =="1":
    os.system('cls')
    ano=int(input("digite seu ano de nacsimento :"))
    anoa=datetime.now()
    idade=(anoa.year-ano)
    print_slow(f"Voçe tem \033[36m{idade}\033[m Anos de idade... ou se nao fez aniversario ainda \033[36m{idade-1}\033[m")
elif opcao =="2":
    cima=float(input("digite a altura do quadrado :"))
    baixo=float(input("digite a largura do quadrado :"))
    total=float(cima*baixo)
    print("\033[33m-=\033[m"*40)
    print_slow(f"esta é a área do quadrado {total}")
elif opcao =="3":
    tabu=int(input("digite o numero que deseja ter saber tabuada (ATÉ 10X) :"))
    for x in range(1,11):
        tt=(tabu*x)
        print(f"{tabu} X {x} = {tt}")
    time.sleep(5)    
elif opcao =="4":
    os.system('cls')
    print_slow("\033[32mAPRECIE!!!\033[m")
    time.sleep(2)
    pa.press('win')
    time.sleep(3)
    pa.write('edge')
    time.sleep(3)
    pa.press('enter')
    time.sleep(3)
    pa.write("neymar skills")
    time.sleep(2)
    pa.press("enter")
    time.sleep(5)
    pa.click(x=1114, y=426)
    time.sleep(9)
    pa.click(x=828, y=525)
    time.sleep(240)
    pa.click(x=1327, y=746)
    time.sleep(10)
    pa.click(x=609, y=748)
    time.sleep(5)
    print("\033[31m-=\033[m"*40)
    print_slow("\033[31mOBRIGADO POR ASSISTIR!!!\033[m")
elif opcao =="5":
    os.system('cls')
    assunto=input("\033[32mdigite oque deseja pesquisar bem especificado :\033[m ")
    print_slow("\033[32mAPRECIE!!!\033[m")
    time.sleep(2)
    pa.press('win')
    time.sleep(3)
    pa.write('edge')
    time.sleep(3)
    pa.press('enter')
    time.sleep(3)
    pa.write("https://chatgpt.com/")
    time.sleep(5)
    pa.press("enter")
    pa.click(x=498, y=662)
    time.sleep(5)
    pa.write(f"{assunto}")
    pa.press("enter")
elif opcao =="0":
    os.system('cls')
    print("\033[32mTCHAU!!!\033[m")
    time.sleep(2)
    pa.press('win')
    time.sleep(3)
    pa.click(x=11, y=704)
    time.sleep(7)
    pa.doubleClick(x=22, y=623)
elif opcao =="6":
    os.system('cls')
    print_slow("Seja bem vindo ao quiz do sabe tudo!!!")
    print_slow("Vamos começar!")
    print("-="*40)
    print_slow("\033[34mCarregando as perguntas.......\033[m")
    time.sleep(3)
    print_slow("Qual é o maior planeta do sistema solar? ")
    print("1-Saturno 2-Jupter 3-Terra 4-Marte")
    print("-="*40)
    r=input("Qual a resposta correta : ")
    if r =="2":
        print("\033[32mResposta correta!!\033[m")
    else:
        print("\033[31mResposta incorreta!!\033[m")
    print("-="*40)
    time.sleep(2)     
    print_slow("\033[34mCarregando as perguntas.......\033[m")
    time.sleep(3)
    print_slow("Qual é o elemento químico com o símbolo Au?") 
    print("1-Ouro 2-Ferro 3-Cobre 4-Niquel")  
    print("-="*40)
    r2=input("Qual a resposta correta : ")
    if r2 == "1":
        print("\033[32mResposta correta!!\033[m")
    else:
        print("\033[31mResposta incorreta!!\033[m")
    print("-="*40)     
    time.sleep(2)     
    print_slow("\033[34mCarregando as perguntas.......\033[m")
    time.sleep(3)
    print_slow("Em que ano a primeira missão Apollo aterrissou na Lua?") 
    print("1-1970 2-1983 3-1990 4-1969")  
    print("-="*40)
    r3=input("Qual a resposta correta : ")
    if r3 == "4":
        print("\033[32mResposta correta!!\033[m")
    else:
        print("\033[31mResposta incorreta!!\033[m")
    print("-="*40)   
elif opcao =="7":
    os.system('cls')
    state = True
    while True:
        adv=random.randint(1,10)
        num=int(input("digite o numero que eu estou pensando..."))
        if num >10 or num<1:
            print("\033[31mNumero escolhido não esta de acordo com as regras do jogo\033[m (somente numeros de 1 á 10)...")
            break
        if num == adv:
            print_slow(f"\033[32mVoce acertou o numero que estou pensando.... o numero éra \033[m{adv}")
            break
        else:
            print(f"\033[31mEU PENSEI NO NUMERO\033[m {adv} \033[31mESTA ERRADO CONTINUE TENTANDO....\033[m")
            time.sleep(1.2)
            os.system('cls') 
elif opcao =="8":
    os.system("cls")
    print("                        \033[32m Radar itaquacity  VEL MAX 80Km\033[m")
    print("-="*40)
    vel=int(input("digite a velocidade do veiculo : "))
    print("-="*40)
    mult=(vel-80)*25
    if vel >125:
        print("\033[31m Vai morrer !! \033[m")
    if mult >=500:
        print("\033[31m Voçe tomou 7 pontos na carteira \033[m")
    elif mult >=125 and mult <=499:
        print("\033[33m voçe tomou 4 pontos na carteira \033[m")
    elif mult >=1 and mult <=124:
        print("\033[33m Voçe tomou 3 pontos na carteira \033[m")       
    if vel <= 40:
        print("\033[31m Voçe esta muito abaixo da velocidade da via!! \033[m")
    elif vel >=41 and vel <=80:
        print("\033[32m voçe esta no limite da via!!! \033[m")
    else:
        print(f"\033[31m esta multado no valor de {mult}R$ !! voçe esta acima da velocidade {vel-80}km a mais da via!! \033[m")                            
if opcao =="9":
    sky()
else:
    print("\033[31mObrigado por usar nosso sistema!!!!\033[m")    
          
