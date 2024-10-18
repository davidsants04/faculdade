import datetime
import os

os.system('cls')

def calcularidade(ano_nacsido):
    idade=datetime.datetime.now().year -ano_nacsido
    return idade

nacs = int(input("Digite o ano em que nasceu :"))
print(calcularidade(nacs))
