class empresa:
    def __init__(self,nome):
        self.__nome = nome
        self.__clientes = []
    def __str__(self):
        return f"{self.__nome} tem {len(self.__clientes)} clientes"

