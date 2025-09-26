class Moto:
    def __init__(self, marca, modelo, ano, cor,):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} km/h!")
    
    def detalhes(self):
        return (f"{self.marca} {self.modelo} {self.ano} -Cor: {self.cor}, Velocidade: {self.velocidade}km/h")

    
moto1 = Moto("BMW", "M 1000 XR", 2024, "Preta")
moto2 = Moto("Kawasaki", "Z 1000", 2024, "Branca")


print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(362)
moto2.acelerar(276)

moto1.frear(140)
moto2.frear(120)

print(moto1.detalhes())
print(moto2.detalhes())
    
if moto1.velocidade > moto2.velocidade:
    print("A BMW ganhou a corrida!")

    
