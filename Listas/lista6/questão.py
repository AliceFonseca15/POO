class Categoria:
    def __init__(self,id,descricao):
        self.__id = 0
        self.__descricao = ""
    def set_id(self,id):
        if id < 0: raise ValueError("id não pode ser 0 ou negativo")
        self.__id = id
    def set_descricao(self,d):
        if d == "": raise ValueError("Informe a descrição")
        self.__descricao = d
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def Tostring(self):
        s = f"id: {self.__id} - Descrição: {self.__descricao}"
class Produto:
    def __init__(self,id,descricao,preço,estoque,idcategoria):
        self.__id = 0
        self.__descricao = "" 
        self.__preço = 0.0
        self.__estoque = 0
        self.__idcategoria = 0
    def set_id(self,id):
        if id < 0: raise ValueError("id não pode ser 0 ou negativo")
        self.__id = id
    def set_descricao(self,d):
        if d == "": raise ValueError("Informe a descrição")
        self.__descricao = d
    def set_preço(self,p):
        if p < 0.0: raise ValueError("Informa o preço")
        self.__preço = p
    def set_estoque(self,e):
        if e == 0: raise
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
