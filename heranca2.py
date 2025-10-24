#Musica Herança
class Musica:
    def __init__(self, nome_music = None, duracao = None):
        self.nome_music = nome_music
        self.duracao = duracao
    
    def info(self) -> str:
        return f"O nome da musica é {self.nome_music} e tem uma duracao de {self.duracao}min."
    
class Artista(Musica):
    def __init__(self, nome_artist = None, nome_music= None, duracao = None):
        if nome_artist is None:
            nome_artist = input("Digite o nome do artista: ")
        if nome_music is None:
            nome_music = input("Digite o nome da musica: ")
        if duracao is None:
            duracao = input("Qual a duração da musica?: ")
        
        super().__init__(nome_music, duracao)
        self.nome_artist = nome_artist
    

class Compositor(Artista):
    def __init__(self, nome_artist = None, nome_comp = None):
        if nome_comp is None:
            nome_comp = input("Quem compôs a musica?: ")

        super().__init__(nome_artist)
        self.nome_comp = nome_comp

    def info(self) -> str:
        base = super().info()
        return f"O nome da musica é {self.nome_music}, o artista é {self.nome_artist} e o compositor(a) da musica é {self.nome_comp}"

artista = Artista()
compositor = Compositor()

print(artista.info())
print(compositor.info())