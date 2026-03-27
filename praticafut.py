class Atacante:
    def chutar_gol(self):
        self.chutar = None
    if chutar_gol is None:
        chutar = input("O Atacante está de frente para o gol, ele deve chutar?: ")
        if chutar == "sim":
            escolha = input("Em qual lado ele deve chutar?\n Esquerda \n Direita\n Escolha: ")
            if escolha == "Direita":
                print("Golaço")

objetos = [Atacante()]

for obj in objetos:
    obj.chutar_gol()        