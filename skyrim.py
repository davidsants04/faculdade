import random
import pyautogui as pa
import time
from datetime import datetime
import os
import sys


def sky():
#prota
    atk=5
    totalatk=atk
    carnejavalitotal=0



    #objetos
    espada="espada"
    espadaatk=3

    #mobs


    #personagems
    marcos="marcos".strip().title()
    patin="patin".strip().title()


    def print_slow(text,delay=.06):
        for char in text:
            print(char,end='',flush=True)
            time.sleep(delay)
        print()

    os.system('cls')
    print_slow("\033[34mEste é um mundo magico e medieval curta essa aventura jovem guerreiro......Seja bem vindo!!!\033[m")
    print("=="*60)
    print_slow("        \033[32mDIA 7 DE AGOSTO....\033[m")
    print_slow("\033[33mVoce esta acordando e existe alguem proximo...\033[m")
    print("")
    print_slow(f"Acorda jovem voce esta jogado aqui no meio desse terreno devasto....oque esta fazendo aqui??")

    print()

    print("""1-Não sei apereci aqui derrepente
    2-Eu durmi aqui...""")

    print()

    op=input("Digite :")
    print("=="*60)
    if op =="1":
        print_slow("Como assim voce esta bebado??")
    elif op =="2":
        print_slow("assim esta certo jovem.....más é meio estranho alguem dormi numa zona de guerra...")
    else:
        print_slow("Há voce é mudo não é mesmo...")
    print_slow("Alias qual seu nome??")
    nome=input("Digite seu nome :").title().strip()
    print_slow(f"Prazer em te conheçer \033[33m{nome}\033[m eu sou o \033[33m{marcos}\033[m estou indo nessa quem sabe não nos encontramos por ai.....")
    print()
    print_slow("\033[33mVoçe esta vagando sentido a cidade de\033[m \033[34mMARKELIAS\033[m \033[33me encotra uma pessoa ferida ira ajuda-la??\033[m ")

    print()

    op1=input("""1-AJUDAR
        2-NÃO AJUDAR : """)

    print()

    if  op1=="1":
        totalatk=atk+espadaatk
        print_slow(f"Ola quem é voçe? eu sou o \033[33m{patin}\033[m estou com muita fome e perdido por aqui consegue me dar um pouco de comida?......Voçe deu comida a este viajante coisas boas estão por vir.....")
        print_slow(f"Voce ganhou uma \033[31m{espada}\033[m do viajante.. e seu dano subiu para {atk+espadaatk}")
    elif op1 =="2":
        print_slow("\033[33mVoçe passou distante dele e seguiu seu rumo...\033[m")
    else:
        print_slow("\033[33mVoce é muito estranho....indecifravel....\033[m")

    print_slow("\033[mApós passa pela pessoa ferida voçe esta mais proximo da cidade.... e voce encontrou um javali pretende mata-lo\033[m??")            
    print("""1-matar
        2-Não matar""")
    print_slow("Digite sua escolha jovem")
    op2=input(":")
    print()
    if op2=="1":
        print_slow("Voçe entrou em combate com o javali")
        if totalatk>=7:
            print_slow(f"\033[32mVoçe o atacou e derrotou o javali\033[m")
            carnejavalitotal=+1
        else:
            print_slow("\033[31mVoçe não consegue vencelo sem armas..\033[m")  
    elif op2=="2":
        print_slow("\033[33mVoçe pasou pelo javali sem confrontalo\033[m")
    else:              
        print_slow("\033[33mVoce nem viu o javali e foi embora...\033[m")
    print_slow("\033[33mSeguindo sua viagem voçe chegou em \033[34mMARKELIA...\033[m onde começou a guerra civil entre os reinos e os aldeões revoltados.....\033[m")    
    print()
    print_slow("\033[33mVoçe viu uma pousada pretende descansar ou continuarar sua viagem ?\033[m")
    print("""1-Entrar na pousada para descançar
        2-não entrar e seguir viagem""")
    op3=input("digite sua escolha :")
    print()
    if op3 == "1":
        print_slow("""Voçe entrou para descansar e conversou com o atendente e ficou com o quarto numeo 34......
        ao chegar no quarto voçe viu um calendario e viu que estava no dia 7 de agosto de 1728....""")
        print_slow("""zzzzzzzzzzzzzzzzz cócóricoooo cócóricoooo cócóricoooo....Que galo miseravel ainda nem é tão cedo..
        """)
    elif op3 =="2":
        print_slow("Voçe segue viagem ..... enquanto sobe a escadaria principal de MARKELIA sua vista começa a escurecer e voçe acaba desmaiando...")
        print_slow("Ao passar da noite jogado na escadairia voçe acorda e percebe que foi roubado....")
        if espadaatk <8:
            print_slow("Voçe percebe que levaram sua espada..")
            espadaatk-6
        elif op3:
            print_slow("Roubaram algumas coisas suas mais nada de valor afinal voçe nao tem nada....")
    else:
        print_slow("voçe Desmaio de cançasso e foi roubado..")
        if espadaatk <8:
            print_slow("Voçe percebe que levaram sua espada..")
            espadaatk-5        
        else:
            print_slow("Roubaram algumas coisas suas mais nada de valor afinal voçe nao tem nada....")

    if  espadaatk <3:        
        print_slow("\033[33mAo perceber que foi roubado voçê lembra de algums flashbacks do seu passado e relembra de quando passou por varios moementos de perigos com seus pais...\033[m")        
        print()
        print_slow("\033[33mVoçe chegou em uma taberna e escutou rumores de ums assaltantes que estão pela redondeza...\033[m")
        print_slow("caleb: Caramba cara voçe esta surrado foi assaltado se quiser resolver isso eu vi algums caras suspeitos ao sul da floresta..")
        print("""1-Pergunta sobre
        2- Deixar isso de lado""")
        op4=input("digite sua opção :")
        if op4 =="1":
            print_slow("Eles estão ao sul da cidade na floresta infinita e são mais de 9 bandidos... se realmente quiser ir la tome cuidado. ")
        elif op4 == "2":
            print_slow("Okay cara eles estão em um bando grande mesmo... é melhor deixar assim mesmo")
        else:
            print_slow(".........'MELHOR DEIXAR ISSO DE LADO NÃO VOU PENSAR MAIS NISSO....'") 
    


       
