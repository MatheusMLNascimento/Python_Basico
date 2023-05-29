#23/02/2022
categoria = int(input("Digite a categoria do produto"))
if categoria == 1:
    preço = 9
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 24
elif categoria == 4:
    preço = 32
elif categoria == 5:
    preço = 40
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preço = 0
print("O preço do produto é: RS%6.2f" % preço)