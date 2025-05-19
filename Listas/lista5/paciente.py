from datetime import datetime
class paciente():
    def __init__(self):
        self.__nome = ""
        self.__telefone = ""
        self.__nascimento = None
        self.__d = 0
    def construtor(self,nome,telefone,nascimento):
        self.__nome = nome
        self.__telefone = telefone
        self.__nascimento = nascimento
    def idade(self,atual):
        a = atual.year - self.__nascimento.year
        self.__d = a
    def ToString(self):
        print(f"Paciente:{self.__nome}")
        print(f"Telefone:{self.__telefone}")
        print(f"Data de nascimento: {self.__nascimento}, são {self.__d}")

x = paciente()
print("Digite a data de atendimento:")
atual = input()
a = datetime.strptime(atual, "%d/%m/%y").date()
print("Digite o nome do paciente:")
nome = input()
print("Digite seu número de telefone:")
telefone = input() 
print("Digite sua data de nascimento (dd/mm/yy):")   
nascimento = input()
n = datetime.strptime(nascimento, "%d/%m/%y").date()
x.construtor(nome,telefone,n)
x.idade(a)
x.ToString