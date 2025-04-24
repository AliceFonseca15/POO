#Conta Bancária
class Ino_conta:
    def __init__(self):
        self.__titular = ""
        self.__num = ""
        self.__saldo = ""
    def set_titular(self, v):
        if v == "" : raise ValueError("Titular não pode ser vazio")
        

        
