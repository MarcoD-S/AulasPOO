#Cruzeiro do Neymar
class Cruzeiro:
    def __init__(self, cor=None, tamanho=None, quartos=None, banheiros=None, restaurantes=None):
        self.cor = cor
        self.tamanho = tamanho
        self.quartos = quartos
        self.banheiros = banheiros
        self.restaurantes = restaurantes
    
    def info(self):
        self.cor = input("Qual a cor do cruzeiro?")
        self.tamanho = input("Qual o tamanho do cruzeiro em m²?")
        self.quartos = input("Quantos quartos tem o cruzeiro?")
        self.banheiros = input("Quantos banheiros tem no cruzeiro?")
        self.restaurantes = input("Quantos restaurantes tem o cruzeiro?")

        return f"Este cruzeiro é {self.cor}, tem {self.tamanho}m² de tamanho, possui {self.quartos} quartos e {self.banheiros} banheiros, No cruzeiro pode se encontrar {self.restaurantes} restaurantes."

cz = Cruzeiro()
print(cz.info())
