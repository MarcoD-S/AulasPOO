class Pessoa:
    def __init__(self, nome = None, CPF = None):
        if CPF is None:
            CPF=input("Digite o CPF: ")
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

    def digitar(self, digitos):
        if 0 > len(digitos) < 11:
            self.__digitos += digitos

pessoa2 = Pessoa()
print("CPF:", pessoa2.CPF)

pessoa2.CPF = "12345678900"
print("CPF após tentativa externa:", pessoa2.CPF)

