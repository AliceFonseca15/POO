#Faça um codigo que mostre todos os numeros menores que X: (Não finalizado)
def chama(num):
    num1 = 0
    if num1 == num:
        return 
    else:
       num1 += 1
       print(num1)
    chama(num1)

numero = int(input())
valor = chama(numero)
print(valor)