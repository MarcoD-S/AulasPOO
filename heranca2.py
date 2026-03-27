#Musica Herança
class Musica:
    def __init__(self, nome_music = None, duracao = None):
        self.nome_music = nome_music
        self.duracao = duracao
    
    def info(self) -> str:
        return f"O nome da musica é {self.nome_music} e tem uma duracao de {self.duracao}min."
    
class Artista(Musica):
    def __init__(self, nome_artist = None, nome_music= None, duracao = None, nome_comp = None):
        print("------------- Artista --------------")
        if nome_artist is None:
            nome_artist = input("Digite o nome do artista: ")
        if nome_music is None:
            print("------------- Musica --------------")
            nome_music = input("Digite o nome da musica: ")
        if duracao is None:
            duracao = input("Qual a duração da musica?: ")
        
        print("------------- Compositor --------------")
        if nome_comp is None:
            nome_comp = input("Quem compôs a musica?: ")
        
        super().__init__(nome_music, duracao)
        self.nome_artist = nome_artist
        self.nome_comp = nome_comp
    

class Album(Artista):
    def __init__(self, nome_artist = None, nome_music= None, duracao = None, nome_comp = None, nome_album = None):
        print("------------- Album --------------")
        if nome_album is None:
            nome_album = input("Digite o nome do album: ")
        
        super().__init__(nome_artist, nome_comp, nome_music, duracao)
        self.nome_album = nome_album
        
    def info(self) ->str:
        base = super().info()
        return f"{base} O artista é o(a) {self.nome_artist} e o compositor é o {self.nome_comp}, o nome do album que essa musica é {self.nome_album}."

    
album = Album()

print(album.info())