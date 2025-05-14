from datetime import datetime
class atleta():
    def __init__(self):
        self.__nome = ""
        self.__nascimento = None
        self.__treino = []
    def set_nome(self,nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def get_nome(self):
        return self.__nome
class Treino():
    def __init__(self,data,distancia,treino):
        self.__data = data
        self.__distancia = distancia
        self.__tempo = treino
    def construtor(self):
        print("Digite a data:")
        self.__nome = input()
        print("Digite a distância percorrida em metros:")
        self.__distancia = int(input())
        print("Digite o tempo do treino:")  
    def set_nome(self,nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_distancia(self,distancia):
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    def set_tempo(self,tempo):
        self.__tempo = tempo
    def get_tempo(self):
        return self.__tempo
    def pace(self):
        minutos = 



