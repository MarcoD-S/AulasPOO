def jogo():
    print("Hoje nos teremos:\n")

def partida():
    print("Brasil x Chile\n")

def campeonato():
    print("Eliminatorias Copa do Mundo 2026\n")

def horario():
    print("Horario do Jogo: 21:30\n")

def placar():
    print("Jogo ainda não aconteceu...\n")

print("Noticias Futebol, tire sua duvida abaixo!")
escolha = int(input("O que você quer saber?" \
                    "\n1 - Jogos de Hoje." \
                    "\nEscolha uma opção acima: \n"))

if(escolha == 1):
    jogo()
    partida()
    campeonato()
    horario()
    placar()

    