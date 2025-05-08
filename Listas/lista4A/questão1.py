import random
class bingo():
    def __init__(self):
        self.__numBolas = ""
        self.__bolas = []
    def construtor(self,b):
        self.__numBolas = b   
    def proximo(self):
        s = self.__numBolas
        a = random.choice(s)
        if a not in self.__bolas:
            return self.__bolas.append(a)
    def sorteados(self):
        for i in self.__bolas:
            print(i,"foi sorteada")
    def __str__(self):
        return f"Esse {self.__bolas} foram sorteados"
        
x = bingo()
x.construtor(30)
x.proximo()
print(x)