#24/02/22
#Atividade 1
print("Digite seu salario para saber se é legível à pagar imposto ou não:")
sal = float(input("R$: "))
if sal >= 1200.00:
    print("Você é legível a pagar imposto!")
else:
    print("Você não é legível a pagar imposto!")
print()

#Atividade 2
a = 1
b = 10
c = True
d = False
print((a > b) and (c or d))
a = 10
b = 3
c = False
d = False
print((a > b) and (c or d))
a = 5
b = 1
c = True
d = True
print((a > b) and (c or d))
print()

#Atividade 3
mat1 = float(input("Nota da primeira matéria:"))
mat2 = float(input("Nota da segunda matéria:"))
mat3 = float(input("Nota da terceira matéria:"))
if mat1 <= 6:
    matre = False
else:
    matre = True
    
if mat2 <= 6:
    matre2 = False
else:
    matre2 = True
    
if mat3 <= 6:
    matre3 = False
else: 
    matre3 = True
    
print("Caso o resultado saia 'False', o aluno foi reprovado. Se sair 'True', aluno aprovado:")
print(matre or matre2 or matre3)
print()

#Atividade 4
a = "ABCDEFGHIJ"
print(len("ABCDEFGHIJ"))
print(a[5])
print(a[4])