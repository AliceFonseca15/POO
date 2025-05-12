class cinema():
    def __init__(self):
        self.__dia = ""
        self.__horario = ""
        self.__preco = 0
    def set_dia(self,d):
        self.__dia = d
    def get_dia(self):
        return self.__dia
    def set_horario(self,h):
        self.__horario = h
    def get_horario(self):
        return self.__horario
    def set_preco(self,v):
        self.__preco = v
    def get_preco(self):
        return self.__preco    
    def dia(self):
        if self.__dia == "Segunda" or "segunda" or "Terça" or "terça" or "Quinta" or "quinta":
            self.__preco = 16
            v = self.__preco
            return v
        if self.__dia == "Quarta" or "quarta":
            self.__preco = 8
            v = self.__preco
            return v
        if self.__dia == "Sexta" or "sexta" or "Sábado" or "sábado" or "Domingo" or "domingo":
            self.__preco = 20
            v = self.__preco
            return v
    def preco(self):
        h = []
        for n in self.__horario:
            h.append(self.__horario[n])
        hora = h[0] + h[1]
        minuto = h[3] + h[4]
        hora = int(hora)
        min = int(minuto)
        if hora >= 17 and min > 00 or hora >= 17 and hora <= 23 and min <= 59:
            self.__preço += self.__preço
            v = self.__preco
        return v

x = cinema()
print("Digite o dia que você quer ver o filme:")
dia = input()
print("Digite o horário:")
horario = input()

x.set_dia(dia)
x.set_horario(horario)
print("Sua sessão é",dia,"e o valor do ingresso é",x.get_preco)