import os

log=[]
sen=[]


os.system('cls')
print("Sistema de loguin")
print("-="*40)
print("""1-Cadastro
2-loguin""")
while True:
    op=input("DIGITE A OPÇÃO :")
    match op:
        case "1":
            while True:
                loguin_pessoa=input("DIGITE O SEU NOVO LOGUIN :")
                senha_pessoa=input("DIGITE SUA NOVA SENHA :")
                print("-="*40)
                print(f"VOCÊ FOI CADASTRADO SEU LOGUIN É {loguin_pessoa} E SUA SENHA {senha_pessoa} !")
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
                    break
                else:
                    print("ERRO")
        case _:
            print("NÃO TEMOS ESSA OPÇÃO !")
    
            
