class Carro:
    def __init__(self, velocidade = 0):
        self.__velocidade = velocidade

    @property
    def acelerar(self):
        return self.__velocidade
    
    @acelerar.setter
    def acelerar(self, velocidade):
        if velocidade > 180:
            print("Você está muito rapido! *Freiando automatico*")
            self.__velocidade = 180
        
        elif velocidade < 0:
            print("A velocidade não pode ser negativa.")
            self.__velocidade = 0
        else:
            self.__velocidade


carro2 = Carro(140)
print("Velocidade inicial:", carro2.acelerar)

carro2.acelerar = 200
print("Velocidade após tentaiva de freiar", carro2.acelerar)