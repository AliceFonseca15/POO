class PlayList:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []
    def inserir(self, m):
        self.__musicas.append(m)  
    def listar(self):
        return self.__musicas      
    def __str__(self):
        return f"PlayList {self.__nome} tem {len(self.__musicas)} música(s)"    

class inteface: #Criar inteceface
    @staticmethod
    def menu():
        print("Selecione a figura: 1-Criar Playlist, 2- Inserir música, 3-Listar músicas, 4-Sair")

class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"    

x = PlayList("Pop", "Divas pop")
y = PlayList("MPB", "Só as melhores")
m1 = Musica("Your Power", "Billie Eilish", "Happier than ever")
m2 = Musica("Cinnamon girl", "Lana del rey", "Norman Fucking Edition")
m3 = Musica("Acenda o farol", "Tim maia", "Single")
x.inserir(m1)
x.inserir(m2)
y.inserir(m3)

print(x)
for musica in x.listar():
    print("  ", musica)
print()
print(y)
for musica in y.listar():
    print("  ", musica)

