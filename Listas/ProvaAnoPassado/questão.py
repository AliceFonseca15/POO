from datetime import datetime
class atletas():
    def __init__(self):
        self.__nome = ""
        self.__id = 0
        self.__nascimento = datetime
    def construtor(self,nome,id,nascimento):
        self.__nome = nome
        self.__id = id
        self.__nascimento = nascimento
    def Tostring(self):
        print("Nome do atleta:")
        print(self.__nome)
        print("Identificador do atleta:")
        print(self.__id)
        print("Data de nascimento:")
        print(self.__nascimento)

class treino():
    def __init__(self):
        self.__nome = ""
        self.__id = 0
        self.__idtreino = 0
        self.__datatreino = datetime
        self.__tempo = datetime.time
    def construtor(self,nome,id,idtreino,datatreino):
        self.__nome = nome
        self.__id = id
        self.__idtreino = idtreino
        self.__datatreino = datatreino

