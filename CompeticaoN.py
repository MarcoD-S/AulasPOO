
def escola():
    count = 0
    while count < 1:
        print("----- Menu Cadastro Escola EEEP Onelio Porto -----\n" \
            "Escolha a sua função: \n" \
            "1 - Trabalho na Escola\n" \
            "2 - Aluno\n" \
            "3 - Pai ou Responsavel\n" \
            "4 - Refeitorio\n" \
            "5 - Fechar Programa")
        escolha = int(input("Digite o número para escolher a função para cadastro: "))

        #Trabalho na Escola
        if(escolha == 1):
            print("----- Menu Função -----\n" \
            "Você trabalha na escola, qual sua função aqui?: \n" \
            "1 - Diretor\n" \
            "2 - Coordenador\n" \
            "3 - Professor\n" \
                                )
            escolha = int(input("Digite o número para escolher a função: "))

            #Diretor Cadastro
            if(escolha == 1):
                print("Bem Vindo Diretor(a), preencha o formulario abaixo.")
                def diretor():
                    idade = int(input("Digite seu idade: "))
                    if(idade < 18):
                        print("Você é menor de idade, não é permitido nem trabalhar.")
                    else:
                        nome = input("Digite seu nome: ")
                        cpf = input("Digite seu cpf: ")
                        print("Cadastrado com sucesso!, bem vindo diretor(a)", nome)
                diretor()

            #Coordenador Cadastro
            if(escolha == 2):
                print("Bem Vindo Coordenador(a), preencha o formulario abaixo.")
                def coordenador():
                    idade = int(input("Digite seu idade: "))
                    if(idade < 18):
                        print("Você é menor de idade, não é permitido nem trabalhar.")
                    else:
                        nome = input("Digite seu nome: ")
                        cpf = input("Digite seu cpf: ")
                        print("Cadastrado com sucesso!, bem vindo coordenador(a)", nome)
                coordenador()

            #Professor Cadastro
            if(escolha == 3):
                print("Bem Vindo Professor(a), preencha o formulario abaixo.")
                def professor():
                    idade = int(input("Digite seu idade: "))
                    if(idade < 18):
                        print("Você é menor de idade, não é permitido nem trabalhar.")
                    else:
                        nome = input("Digite seu nome: ")
                        cpf = input("Digite seu cpf: ")
                        print("----- Menu Matéria -----\n" \
                        "Escolha a sua função: \n" \
                        "1 - Matemática\n" \
                        "2 - Português\n" \
                        "3 - Filosofia\n" \
                        "4 - Sociologia\n" \
                        "5 - Projeto de vida\n" \
                        "6 - Artes\n" \
                        "7 - Mundo do Trabalho\n" \
                        "8 - Ensino Tecnico\n")
                        escolha = int(input("Digite o número para escolher a materia: "))
                        if(escolha == 1):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de matemática", nome)
                        if(escolha == 2):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de português", nome)
                        if(escolha == 3):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de filosofia", nome)
                        if(escolha == 4):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de sociologia", nome)
                        if(escolha == 5):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de projeto de vida", nome)
                        if(escolha == 6):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de artes", nome)
                        if(escolha == 7):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de mundo do trabalho", nome)
                        if(escolha == 8):
                            print("Cadastrado com sucesso!, bem vindo professor(a) de ensino tecnico", nome)
                professor()
        if(escolha == 2):
           print("--- Menu Aluno ---" \
                 "\nDeseja se matricular na escola?")
           sn = int(input("Digite 1 para sim e 2 para não: \n"))

           if(sn == 2):
               print("Fechando programa...")
               exit()

           if(sn == 1):
               idade = int(input("Digite sua idade: "))
               if (idade > 18):
                   print("Você tem mais de 18 anos e não pode se matricular nessa escola!")
               else:
                   nome = input("Digite seu nome: ")
                   num = int(input("Digite seu número de telefone: "))
                   print("Escolha o curso que deseja fazer:\n")
                   print("----- Menu Curso -----\n" 
                        "1 - Desenvolvimento de Sistemas\n" 
                        "2 - Enfermagem\n" 
                        "3 - Finanças\n"
                        "4 - Administração\n")
                   curso = int(input("\nDigite o numero do curso desejado: "))
                   if (curso == 1):
                        print("Seja bem vindo aluno(a)", nome, "do curso de Desenvolvimento de Sistemas")
                   if (curso == 2):
                       print("Seja bem vindo aluno(a)", nome, "do curso de Enfermagem")
                   if (curso == 3):
                       print("Seja bem vindo aluno(a)", nome, "do curso de Finanças")
                   if (curso == 4):
                       print("Seja bem vindo aluno(a)", nome, "do curso de Administração")

        if(escolha == 3):
            print("----- Menu Pais ou Responsaveis -----" \
                    "1 - Cadastrar Responsavel" \
                    "2 - Consultar Aluno")
            
        if(escolha == 4):
            def refeitorio():
                    print("----- Menu Refeitorio -----\n"
                                "1 - Mistão\n"
                                "2 - Paçoca\n"
                                "3 - Frango Assado\n"
                                "4 - Não vou almocar")
                    comida = int(input("Escolha almoço de hoje: "))

                    if(comida == 1):
                            print("Comendo mistão...")
                    if (comida == 2):
                            print("Comendo paçoca...")
                    if (comida == 3):
                            print("Comendo frango assado...")
                    if (comida == 4):
                            print("Não estou comendo...")
                            exit()

            refeitorio()
            
        sn = int(input("Deseja voltar para o menu? Digite 1 para sim e 2 para não:"))
        if(sn == 2):
            exit()
             

escola()


