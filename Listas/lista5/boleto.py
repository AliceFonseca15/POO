from datetime import datetime
import enum

class Boleto:
    def __init__(self,cod,emissao,vencimento,pagto,boleto,pago):
        self.__codBarras = cod
        self.__dateEmissao = emissao
        self.__dateVencimento = vencimento
        self.__pagto = pagto # data do pagamento
        self.__valorBoleto = boleto
        self.__valorPago = pago
        self.__situacaoPagamento = Pagamento()
    def pagar(self,v):
        self.__boleto = self.__ - v
        if self.__boleto == 0:
            self.__situacaoPagamento(3)
        
        


class Pagamento(enum.Enum):
    aberto = 1
    parcial = 2
    pago = 3

