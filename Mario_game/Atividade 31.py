# Com isso eu pego todas as funções do outro arquivo e uso nesse,
# o que me poupa linhas
from calculador import *

# Uso um print junto com a variavél input para uma melhor aparência
print("Calculadora, escolha a operação:")
select = int(input(" 1 - Multiplicação\n 2 - Divisão\n 3 - Soma\n 4 - Subtração\n"))

# Uso o IF e ELIF para chamar as funções
if select == 1:
    multiplicacao()
elif select == 2:
    divisao()
elif select == 3:
    soma()
elif select == 4:
    subtracao()
else:
    print("Digite apenas de 1 a 4!")