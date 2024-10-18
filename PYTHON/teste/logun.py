import os


os.system('cls')
print("Sistema de loguin")
print("-="*40)

while True:
    loguin=input("Digite seu loguin :")
    senha=input("Digite sua senha :")
    os.system('cls')
    if loguin == "david" :
        if senha == "40028922" :
            print("bem vindo!")
            break
        elif senha != "4008922":
            print("ERRO")
    else:
        print("ERRO")
        