from datetime import datetime
class atletas():
    def __init__(self):
        self.__nome = ""
        self.__id = 0
        self.__nascimento = None
    def construtor(self):
        nome = input("Digite seu nome:")
        self.__nome = nome
        id = int(input("Digite o número do seu identificador:"))
        self.__id = id
        nascimento = input("Digite sua data de nascimento no formato dd/mm/yy:")
        nascimento1 = datetime.strptime(nascimento, "%d/%m/%y").date()
        self.__nascimento = nascimento1
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
        self.__datatreino = None
        self.__tempo = None
        self.__distancia = 0
        self.__pace = 0
    def construto(self):
        nome = input("Digite seu nome:")
        self.__nome = nome

        id =  int(input("Digite o número do seu identificador:"))
        self.__id = id

        idtreino = int(input("Digite o id do seu treino:"))
        self.__idtreino = idtreino

        datatreino = input("Digite a data do seu treino (dd/mm/yy): ")
        self.__datatreino = datetime.strptime(datatreino, "%d/%m/%y").date()

        temp = input("Digite o tempo do seu treino (hh:mm:ss): ")
        self.__tempo = datetime.strptime(temp, "%H:%M:%S").time()

        distancia = int(input("Digite a distância em km da sua corrida:"))
        self.__distancia = distancia
    def pace(self):
        minutos = self.__tempo.hour * 60 + self.__tempo.minute + self.__tempo.second / 60
        p = minutos / self.__distancia
        self.__pace = p
    def Tostring(self):
        print("Nome do atleta:")
        print(self.__nome)
        print("Identificador do atleta:")
        print(self.__id)
        print("Identificador do treino:")
        print(self.__idtreino)
        print("Data do treino:")
        print(self.__datatreino)
        print("Pace:")
        print(f"Seu pace correndo {self.__distancia}km em {self.__tempo} é {self.__pace}min/km")
        print("Data de nascimento:")

x = atletas()
x.construtor()
x.Tostring()
x1 = treino ()
x1.construto()
x1.pace()
x1.Tostring()



