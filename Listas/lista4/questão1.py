import random
class bingo():
    def __init__(self):
        self.__numBolas = ""
        self.__bolas = []
    def construtor(self,b):
        self.__numBolas = b   
    def proximo(self):
        s = len(self.__bolas)
        a = random.choice(self.__bolas)
        if a in self.__bolas:
            a = self.proximo(s)
        else:
            self.__bolas.append(a)
    def sorteados(self):
        for i in range(0,len(self.__bolas)):
            print(i,"foi sorteada")
    
x = bingo()
x.construtor(30)
