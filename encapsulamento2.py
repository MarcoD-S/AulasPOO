class Pessoa:
    def __init__(self, nome = None, CPF = 0):
        self.nome = nome
        self.__CPF = CPF

    @property
    def CPF(self):
        return self.__CPF
    
    @CPF.setter
    def CPF(self, digitos):
        if 0 <= len(digitos) > 11:
            print("Erro: Mais ou menos digitos do que o esperado!")

        else:
            self.__CPF = digitos

