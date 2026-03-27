class Time:
    def __init__(self, nomeTime = None, idadeCB = None, torcida = None):
        self.nomeTime = nomeTime
        self.idadeCB = idadeCB
        self.torcida = torcida
    
    def info(self) -> str:
        return f"\nBem vindo(a) jogador(a) {self.nomeJog} do time {self.nomeTime}, camisa {self.numero} que joga na posição de {self.posicao}. Um time que tem {self.idadeCB} anos e {self.torcida} mil torcedores!"
    
class Jogador(Time):
    def __init__(self, nomeJog = None, posicao = None, numero = None, nomeTime = None, idadeCB = None, torcida = None):
        print("------------- Jogador --------------")
        if nomeJog is None:
            nomeJog = input("Digite o nome do jogador: ")
        if posicao is None:
            posicao = input("Qual a posição do jogador?(Atacante, Ponta, Meia, Lateral, Zagueiro): ")
        if numero is None:
            numero = input("Qual o número do jogador?: ")
        
        print("------------- Time --------------")
        if nomeTime is None:
            nomeTime = input("Digite o nome do time do jogador: ")
        if idadeCB is None:
            idadeCB = input("Digite a idade do time: ")
        if torcida is None:
            torcida = input("Digite a quantidade de torcedores do time (casa dos milhares): ")
        
        super().__init__(nomeTime, idadeCB, torcida)
        self.nomeJog = nomeJog
        self.posicao = posicao
        self.numero = numero

        print("Temos uma partida para jogar, você quer jogar?\n")
        escolha = input("Digite S para sim e N para não: ")

        if escolha == "S" or "s":
            if posicao == "Atacante" or "atacante" or "ATACANTE": 
                class Atacante:
                    print("Bora pra jogo meu atacante!")

                    def __init__(self, nomeJog):
                        self.nomeJog = nomeJog

                    def chutar(self):
                        print(f"O Atacante {self.nomeJog} chutou a bola no angulo!")

                def chutar_gol(obj):
                    obj.chutar()

                a = Atacante(self.nomeJog)
                chutar_gol(a)

            if posicao == "Ponta":
                class Ponta:
                    def __init__(self, nomeJog):
                        self.nomeJog = nomeJog

                    def passar(self):
                        return f"O Jogador da ponta {self.nomeJog} driblou e passou a bola"
        if escolha == "N" "n":
            print("Jogador fraco kkkkkkkk")
            
jogador = Jogador()

