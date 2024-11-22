# SIstema conta bancaria
import time
from datetime import datetime
from abc import ABC, ABCMeta


def print_slow(text, delay=.06):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


data = datetime.now()

print_slow(f"{data.year}/{data.month}/{data.day}:{data.hour}")


class Usuario:
    def __init__(self, nome: str, senha: str,):
        self.__nome = nome  # esses __ É PROTEÇÃo privando o codigo
        self.__senha = senha
        self.__status = False
        

    @property    # com esse getter não pode ser alterado os dados.
    def nome(self):
        return self.__nome

    @property    # com esse getter não pode ser alterado os dados.
    def senha(self):
        return self.__senha

    @nome.setter  # com osetter  os atributos podem ser alterado
    def nome(self, novonome):
        self.__nome = novonome

    @senha.setter
    def senha(self, novasenha):
        self.__senha = novasenha


class Conta(ABC):
    def __init__(self, usuario: str, saldo: float, data_abertura: str, limite:float):
        self.__usuario = usuario
        self.__saldo = saldo
        self.__dataabertura = data_abertura
        self.__limite = limite


    @property
    def usuario(self):
        return self.__usuario

    @property
    def saldo(self):
        return self.__saldo

    @property
    def data(self):
        return self.__dataabertura

    @usuario.setter
    def usuario(self, novousuario):
        self.__usuario = novousuario

    @saldo.setter
    def saldo(self, novosaldo):
        self.__saldo = novosaldo

    @data.setter
    def data(self, data):
        self.__data = data

    
    def sacar(self, valor):
        pass

    
    def deposita(self, valor2):
        pass

    def data1(self):
        self.__dataabertura
        print(self.__dataabertura)


class Contacorrente(Conta):
    def __init__(self, usuario: str, saldo: float, data_abertura: str, limite: float):
        super().__init__(usuario, saldo, data_abertura, limite)
        self.limite=limite


    def deposita(self,valor):
        if valor >10:
            self.saldo+=valor

    def sacar(self,valor):
        if valor <=self.limite + self.saldo:
            self.saldo -= valor
            print(self.saldo)
        else:
            print("Ultrapassou o limite de saldo !")    
               


class ContaPoupanca(Conta):
    def deposita(self,valor):
        self.saldo+=valor
    

    def sacar(self,valor):
        if valor <=self.saldo:
            self.saldo-=valor    


cc1=Contacorrente("david",2500,"",1500)
cc1.sacar(4500)
