class triangulo:
    def __init__(self):
             self.b = 0 # valor padrão, valor inicial do campo/
             self.h = 0
    def calc_area(self): # self é usado para o pyhton saber qual a variavel é usada na operação
              return self.b * self.h / 2
x = triangulo()
x.b - 10
x.h = 20
print(x.b,x.h, x.calc_area())

y =  triangulo()
y.b = 5 
y.h = 15
print(y.b,y.h,y.calc_area())

z = x # Faz com que a variavel z tenha acesso dos valores de x.b e x.h, podendo ser alterado
z.b = 40
z.h = 50
print(z.b,z.h,z.calc_area())