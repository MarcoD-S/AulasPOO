class Atacante:
    def chutar(self):
        print("O atacante chutou no gol!")

    def assistencia(self):
        print("O atacante deu uma assistencia!")

class Ponta:
    def chutar(self):
        print("O ponta driblou e chutou no gol!")

    def assistencia(self):
        print("O ponta deu uma assistencia!")

class Meia:
    def chutar(self):
        print("O meia chutou de longe no gol!")

    def assistencia(self):
        print("O meia deu uma assistencia!")

# def chutar(obj):
#     obj.chutar()

# a = Atacante()
# p = Ponta()
# m = Meia()

# chutar(a)
# chutar(p)
# chutar(m)

objetos = [Atacante(), Ponta(), Meia()]

for obj in objetos:
    obj.chutar()
