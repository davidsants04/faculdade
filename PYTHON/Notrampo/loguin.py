import os
import time
log=[]
sen=[]

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

os.system('cls')
print_slow("Sistema de loguin")
print("-="*40)
while True:
    print_slow("""1-Cadastro
2-loguin""")
    op=input("DIGITE A OPÇÃO :")
    match op:
        case "1":
            while True:
                loguin_pessoa=input("DIGITE O SEU NOVO LOGUIN :")
                senha_pessoa=input("DIGITE SUA NOVA SENHA :")
                print("-="*40)
                print_slow(f"VOCÊ FOI CADASTRADO SEU LOGUIN É {loguin_pessoa} E SUA SENHA {senha_pessoa} !")
                log.append(loguin_pessoa)
                sen.append(senha_pessoa)
                print("-="*40)
                break       
        case "2":
            while True:
                loguin=input("Digite seu loguin :")
                senha=input("Digite sua senha :")
                os.system('cls')
                if loguin in log :
                    if senha in sen :
                        print("bem vindo!")
                    if True:
                        print_slow(f"Ola seja bem vindo {loguin}")
                        print_slow("""O que deseja fazer no nosso sistema temos essas opções :""")
                        break
                else:             
                    print("ERRO")
        case _:
            print("NÃO TEMOS ESSA OPÇÃO !")
            break
     
    
            