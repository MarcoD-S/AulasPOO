class SerVivo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def respirar(self):
        print(f"{self.nome} está respirando...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

class Pessoa(SerVivo):
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

    def andar(self, destino):
        print(f"{self.nome} está andando até {destino}")
    
    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}")

# Criando objetos
p1 = Pessoa("Marco", 17)
p2 = Pessoa("Ezequiel", 16)

# Chamando ações
p1.respirar()
p1.falar("Opa eu!")
p1.andar("o alphaville")
p1.comer("Pastel")

print("--------------")

p2.dormir()
p2.falar("Estou jogando Ready or not!")