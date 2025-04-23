class Circulo:
    def __init__(self):
        self.pi = 3.14
        self.r = 3
    def mensagem(self):
        return "Valores da área e circuferência de um circulo:"
    def area(self):
        return self.pi * (self.r * self.r)
    def circuferencia(self):
        return 2 * self.pi * self.r
    
x = Circulo()
print(x.mensagem())
print(x.area())
print(x.circuferencia())