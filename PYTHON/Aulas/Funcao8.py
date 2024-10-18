import os
os.system('cls')

def verificarlogin(login,senha):
    if login=="david":
        if senha=="1234":
            print("\033[32mENTROU NO SISTEMA\033[m")
            return True
        else:
            print("falha algo incorreto!")
            return False
    else:
        print("falha")
        return False        

while True:
    loguin=input("digite seu login :")
    senh=input("digite a sua senha :")

    if verificarlogin(loguin,senh):
        break
    else:
        pass


 