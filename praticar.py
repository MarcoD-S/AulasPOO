class Time:
    def __init__(self, nomeTime = None, idadeCB = None, torcida = None):
        self.nomeTime = nomeTime
        self.idadeCB = idadeCB
        self.torcida = torcida
    
    def info(self) -> str:
        return f"\nBem vindo(a) jogador {self.nomeJog} do time {self.nomeTime}, camisa {self.numero} que joga na {self.posicao}. Um time que tem {self.idadeCB} anos e {self.torcida} mil torcedores!"
    
class Jogador(Time):
    def __init__(self, nomeJog = None, posicao = None, numero = None, nomeTime = None, idadeCB = None, torcida = None):
        print("------------- Jogador --------------")
        if nomeJog is None:
            nomeJog = input("Digite o nome do jogador: ")
        if posicao is None:
            posicao = input("Qual a posição do jogador?: ")
        if numero is None:
            numero = input("Qual o número do jogador?: ")
        
        print("------------- Time --------------")
        if nomeTime is None:
            nomeTime = input("Digite o nome do time do jogador: ")
        if idadeCB is None:
            idadeCB = input("Digite a idade do time do jogador: ")
        if torcida is None:
            torcida = input("Digite a quantidade de torcedores do time (casa dos milhares): ")
        
        super().__init__(nomeTime, idadeCB, torcida)
        self.nomeJog = nomeJog
        self.posicao = posicao
        self.numero = numero

class Tecnico:
    def __init__(self, nomeTec = None, idadeTec = None, tatica = None):
        print("------------- Tecnico --------------")
        if nomeTec is None:
            nomeTec = input("Digite o nome do tecnico: ")
        if idadeTec is None:
            idadeTec = input("Digite a idade do tecnico: ")

    def chutar(self):
        return f"O jogador {self.nomeJog} chutou a bola!"

    def passar(self):       
        return f"O jogador {self.nomeJog} passou a bola!"

jogador = Jogador()
print(jogador.info())
