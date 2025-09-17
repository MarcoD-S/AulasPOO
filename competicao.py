def escola():
    print("----- Menu Cadastro Escola EEEP Onelio Porto -----\n" \
        "Escolha a sua função: \n" \
        "1 - Trabalho na Escola\n" \
        "2 - Aluno\n" \
        "3 - Pai ou Responsavel\n")
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
       sn = input("Digite S para sim e N para não: \n")

       if(sn == "s" or "S"):
           idade = int(input("Digite sua idade: "))
           if(idade > 18):
            print("Você tem mais de 18 anos e não pode se matricular nessa escola!")
           else:
            nome = input("Digite seu nome: ")
            num = int(input("Digite seu número de telefone: "))
        
           
    if(escolha == 3):
        print("----- Menu Pais ou Responsaveis -----" \
                "1 - Consultar nota aluno")      
escola()