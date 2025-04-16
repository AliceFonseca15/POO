class Conta():
    def __init__(self):
        self.nome = "José Ricardo Medeiros"
        self.n = 0
        self.s = 0
        self.saq = 0
        self.d = 0
    def mensagem(self):
        return "Status da conta:"
    def saq_dep(self):
        self.s = self.s - self.saq
        self.s = self.s + self.d
        return self.s
    
    
x = Conta()


x.n = 4879 # numero da conta
x.s = 1000 # Saldo da conta
x.saq = 200 # Dinheiro de saque
x.d = 100 # Dinheiro depósitado

print(x.mensagem())
print(x.nome)
print(x.n)
print(x.saq_dep())