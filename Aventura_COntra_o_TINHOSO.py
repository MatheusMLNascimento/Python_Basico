hp = 100
arm = 40
n = True
dano_base = 1
print("Aventura contra o tinhoso!")
nome = input("Nome do seu personagem: ")
escolha = input("O reino de Arendell está sendo atacado e você foi chamado pelo rei.\nir\nnão ir\n")
while n == True:
    while escolha != "ir":
        if escolha == "ir":
            print("{} escolheu ir,\n depois de um tempo andando, {} finalmente chega ao castelo.".format(nome, nome))
            escolha = input("(Deseja falar com o rei ou com a princesa?)")
        if escolha == "princesa":
            print("(Ela está apávorada demais para conversar...)")
        elif escolha == "rei":
            print("Nosso reino está sendo atacado por Tinhoso,\n ele ja foi derrotado uma vez, porém voltou triunfante como nunca.\n Você é descendente do antigo herói, seu objetivo de vida é derrotar Tinhoso novamente!")
            escolha = input("(O rei manda você se armar com os equipamentos do antigo herói... \nPorém uma parte do castelo caí na porta da sala do tesouro. \nSobra os equipamentos inicias.)\npegar\nnão pegar\n")
            if escolha == "pegar":
                print("GAy")
        elif escolha == "sim":
            print("Você é burro?")
            escolha = input("Voltar?\nsim\nnão.")
        else:
            print("{} escolheu ficar em casa, dormindo... \nAté um pedaço do castelo atingir sua casa... \nE matá-lo.".format(nome))
            n = False
