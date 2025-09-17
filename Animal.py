class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som do animal")

class Cachorro(Animal):
    def falar(self):
        print("Au Au")

class Gato(Animal):
    def falar(self):
        print("Meow!")

dog = Cachorro("Da vinci")
cat = Gato("Sheiksper")

dog.falar()
cat.falar()