class Tempo():
    def __init__(self):
        self.km = 0
        self.h = 0
        self.m = 0
    def velocidade_media(self):
        m = self.m / 60
        self.h = self.h + m
        return self.km / self.h

x = Tempo()
x.km = 100
x.h = 1
x.m = 20
print(x.velocidade_media())