#Aula de introdução aos conceitos de POO
# Entidades, classificação, modelos de entidade e abstra~ção

class Triangulo:
        def __init__(self):
             self.b = 0
             self.h = 0
        def teste(self):
            return "Olá"
        def calc_area(self): # self é usado para o pyhton saber qual a variavel é usada na operação
              return self.b * self.h / 2
x = Triangulo()  # executa o método __init__
print(x)
print(x.b,x.h)
x.b = 10
x.h = 20
print(x.teste())
print(x.b,x.h)
print(x.calc_area())

y = Triangulo()
print(y)
print(y.teste())
print(y.b,y.h)
print(y.calc_area())
