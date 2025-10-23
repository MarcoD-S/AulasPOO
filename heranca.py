class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}, meu CPF é {self.cpf}"


class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: str) -> None:
        super().__init__(nome, cpf) # Chama o __init__ da classe Pessoa
        self.matricula = matricula


    def apresentar(self) -> str:
        base = super().apresentar() # Usa o metodo da classe Pessoa
        return f"{base} e sou aluno, matricula {self.matricula}"

class Professor(Aluno):
    def __init__(self, nome = None, matricula = None, cpf = None, materia = None):
        if nome is None:
            nome = input("Digite o seu nome: ")
        if matricula is None:
            matricula = input("Digite a sua matricula: ")
        if cpf is None:
            cpf = input("Digite o seu cpf")
        if materia is None:
            materia = input("Digite o seu materia: ")

        super().__init__(nome, matricula, cpf)
        self.materia = materia

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e eu sou professor de {self.materia}"


# Programa principal
pessoa = Pessoa("João", "123.456.789.00")
aluno = Aluno("Ana", "A123", "123.456.789.00")
professor = Professor()

print(pessoa.apresentar())
print(aluno.apresentar())
print(professor.apresentar())