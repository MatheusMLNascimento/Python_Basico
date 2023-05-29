import random
x2 = 0
hp = 100
arm = 40
bosshp = 666
n = True
x = arm
x1 = "Armadura"
chance = 1
critico = 1
dano_base = 1
hp_ini = 45
dam_ini = random.randint(1,2)
print("Aventura contra o tinhoso!")
nome = input("Nome do seu personagem: ")
while n != False:
    escolha = input("O reino de Arendell está sendo atacado e você foi chamado pelo rei.\n Ir\n Não ir\n")
    if escolha == "ir":
        print("{} escolheu ir,\n depois de um tempo andando, {} finalmente chega ao castelo.".format(nome, nome))
        escolha = input("(Deseja falar com o rei ou com a princesa?)\n")
        if escolha == "princesa":
            print("(Ela está apávorada demais para conversar...)")
            escolha = input("Voltar?\nsim\nnão.")
            if escolha == "sim":
                escolha = input("(Deseja falar com o rei ou com a princesa?)")
        elif escolha == "rei": 
            print('"Nosso reino está sendo atacado por Tinhoso,\n ele ja foi derrotado uma vez, porém voltou triunfante como nunca.\n Você é descendente do antigo herói, seu objetivo de vida é derrotar Tinhoso novamente!"')
            escolha = input("(O rei manda você se armar com os equipamentos do antigo herói... \nPorém uma parte do castelo caí na porta da sala do tesouro. \nSobra os equipamentos inicias.)\n Pegar\n Não pegar\n")
            if escolha == "pegar":
                print("(Mano tu é?... Digo, você escolheu pegar o equipamento inicial.)")
                escolha = input("Um monstro aparece atrás de {}, uma batalha de turnos inicia-se!\n Batalhar\n Tentar fugir.\n".format(nome))
                if escolha == "batalhar":
                    print()
                    while hp_ini > 0 or hp <= 0:
                        print("Goblin saqueador aparece! Prepare-se para uma batalha sangrenta... Ou nem tanto.")
                        escolha = input(" Bater(1 á 4 de dano)\n Fugir(Cagão).\n")
                        if escolha == "bater":
                            dano_base = random.randint(1,4)
                            print("Goblin saqueador recebeu %d de dano!"% dano_base)
                            print()
                            chance = random.randint(0,100)
                            if chance <= 8:
                                critico = random.randint(2,4)
                                print("Acerto crítico! Dano %d"% critico)
                                hp_ini -= critico
                            hp_ini -= dano_base
                            print("Goblin saqueador ficou com %d de vida!"% hp_ini)
                            if hp_ini <= 0:
                                print("Você venceu o primeiro monstro, párabens")
                                break
                            print()
                            dam_ini = random.randint(1,3)
                            print("Goblin saqueador revida o ataque! Causando %d de dano!"% dam_ini)
                            if arm >= 0:
                                chance = random.randint(0,100)
                                if chance <= 8:
                                    critico = random.randint(2,3)
                                    print("Acerto crítico! Dano %d"% critico)
                                    arm -= critico
                                arm -= dam_ini
                                print()
                                print("Armadura atual {}".format(arm))
                            elif hp >= 0:
                                chance = random.randint(0,100)
                                if chance <= 8:
                                    critico = random.randint(2,3)
                                    print("Acerto crítico! Dano %d"% critico)
                                    hp -= critico
                                hp -= dam_ini
                                print()
                                if hp < 0:
                                    print("Você perdeu, mais sorte na próxima vez!")
                                    break
                                print("Vida atual {}".format(hp))
                    chance = random.randint(0,100)
                    if chance <= 89:
                        hp = 120
                        arm = 70
                        print("{} derrotou o inimigo...\nPorém, surge das sombras, uma figura gigantesca e monstruosa...\nUm BOSS SECRETO, tens o que é necessário?".format(nome))
                        print("{} ganha um buff de força, armadura e vida devido a ira que emana do monstro.".format (nome))
                        print()
                        dano_base = random.randint(10,28)
                        print("Kreiton, Bom de Coito recebeu %d de dano!"% dano_base)
                        print()
                        chance = random.randint(0,100)
                        if chance <= 8:
                            critico = random.randint(30,47)
                            print("Acerto crítico! Dano %d"% critico)
                            hp_ini -= critico
                        bosshp -= dano_base
                        print("Kreiton, Bom de Coito ficou com %d de vida!"% bosshp)
                        if bosshp <= 0:
                            print("Você venceu Kreiton, Bom de Coito, párabens")
                            print()
                            break
                        print()
                        dam_ini = random.randint(17,23)
                        print("Kreiton, Bom de Coito revida o ataque! Causando %d de dano!"% dam_ini)
                        if arm >= 0:
                            chance = random.randint(0,100)
                            if chance <= 28:
                                critico = random.randint(30,45)
                                print("Acerto crítico! Dano %d"% critico)
                                arm -= critico
                            arm -= dam_ini
                            print()
                            print("Armadura atual {}".format(arm))
                        elif hp >= 0:
                            chance = random.randint(0,100)
                            if chance <= 8:
                                critico = random.randint(60,100)
                                print("Acerto crítico! Dano %d"% critico)
                                hp -= critico
                            hp -= dam_ini
                            print()
                            if hp < 0:
                                print("Você perdeu, mais sorte na próxima vez!")
                                break
                            print("Vida atual {}".format(hp))
            elif escolha == "não pegar":
                print("Fim de jogo!... Você é burro?")
            elif escolha == "sim":
                print("Você é burro?")
                escolha = input("Voltar?\n Sim\n Não.\n")
                if escolha == "sim":
                    print("Fuck go back, i want to be monki")
