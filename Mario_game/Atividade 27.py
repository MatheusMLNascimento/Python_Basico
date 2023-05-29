nome_arquivo = input("Digite o nome para o arquivo: ")
arquivo = open(f"{nome_arquivo}.txt", "w")

resposta1 = input("Digite o que quer na primeira linha: ")

arquivo.write(f"{resposta1}\n")
resposta2 = input("Digite o que quer na última linha: ")
arquivo.write(f"{resposta2}")

arquivo.close()