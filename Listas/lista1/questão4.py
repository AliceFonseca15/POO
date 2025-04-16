class Cinema():
    def __init__(self):
        self.d = input("Dia da semana:")
        self.ho = input("Horário:")
        self.ingresso = input("Tipo de ingresso:")
        self.preço = 0
    def dia(self):

        if self.ingresso == "Inteira" or self.ingresso == "Inteiro":
            if self.d == "Segunda" or self.d == "Terça" or self.d == "Quinta":
                 self.preço += 16
            if self.d == "Quarta":
                 self.preço += 8
            if self.d == "Sexta" or self.d == "Sábado" or self.d ==  "Domingo":
                self.preço += 20
        else:
            if self.d == "Segunda" or self.d == "Terça" or self.d == "Quinta":
                self.preço += 8
            if self.d == "Quarta":
                self.preço += 8
            if self.d == "Sexta" or self.d == "Sábado" or self.d == "Domingo":
                self.preço += 10
        return self.preço
    
    def horario(self):
        lista = []
        for letra in self.ho:
            lista.append(letra)
        h = lista[0] + lista[1]
        m = lista[3] + lista[4]
        hora = int(h)
        min = int(m)
        if hora >= 17 and min > 00 or hora >= 17 and hora <= 23 and min <= 59:
            self.preço += self.preço
        return self.preço

x = Cinema()

x.preço = x.dia()
print(x.horario())