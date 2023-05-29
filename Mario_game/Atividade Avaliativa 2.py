# Adicionei uma mensagem de boas vindas

print("Bem vindo, escolha o que deseja fazer a seguir")
try:
    resposta = int(input(" 1 - Criar arquivo\n 2 - Juntar arquivo\n"))
except ValueError:
    print("Adicione somente números!")
# Iniciei com IF pois é o caminho mais curto

if resposta == 1:
    # Aqui é onde peço o nome desejado para o arquivo
    nome_arquivo = input("Digite o nome para o arquivo: ")
    # Usei o format para facilitar minha vida
    arquivo = open(f"{nome_arquivo}.txt", "w")

    # Aqui registrei o que a pessoa escreveu, e mandei para dentro do arquivo
    resposta1 = input("Digite o que quer que esteja dentro do arquivo: ")
    arquivo.write(f"{resposta1}")
elif resposta == 2:
    # Usei o TRY para personalizar as mensagens de erro, para auxiliar na utilização do programa
    try:
        resposta = input("Nome escolhido para o arquivo: ")
        arquivo_fusao = open(f"{resposta}.txt", "w")

        # Neste ponto, pedi os nomes dos arquivos a serem fundidos
        nome_arquivo1 = input("Nome do primeiro arquivo: ")
        nome_arquivo2 = input("Nome do segundo arquivo: ")

        # Depois uso os nomes guardados nas variavéis para "pescar" os arquivos no computador
        filename = f'{nome_arquivo1}.txt'
        filename2 = f'{nome_arquivo2}.txt'

        # Aqui eu abro os arquivos para poder extrair a informação contida dentro deles
        with open(filename) as file_object:
            lines = file_object.readlines()
        with open(filename2) as file_object:
            lines2 = file_object.readlines()

        # Então uso este comando para poder passar o que foi escrito no outro arquivo para esse,
        # faço a mesma coisa com os dois arquivos
        for line in lines:
            arquivo_fusao.write(line)
            # Coloquei esse comando para não juntar uma linha na outra,
            # umas forma de separar os arquivos dentro do bloco de notas
            arquivo_fusao.write("\n\n")

        for line2 in lines2:
            arquivo_fusao.write(line2)

        # Logo após, finalizo com uma mensagem de confirmação
        print("\n Arquivo pronto!")

        # Termino fechando o arquivo
        arquivo_fusao.close()
    # Isto é apenas para tratar dos erros
    except FileNotFoundError:
        print("\n Arquivo não encontrado, digite novamente!")
else:
    print("Digite apenas 1 e 2.")