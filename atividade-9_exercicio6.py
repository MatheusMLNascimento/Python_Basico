#Matheus Martins
#20/03/2022
#Python online
 #Atividade 1
numero = [ ]
x = 0
b = -2
print("Digite aqui os números que precisa e obtenha uma soma e média aritmética\n(Digite 0 apenas quando precisar sair)")
while x > b:
    n = int(input("Número %d: " % (x + 1)))
    if n == 0:
        break
    numero.append(n)
    x += 1print()
total = len(numero)
media = sum(numero)/len(numero)
soma = sum(numero)
print(" Total digitado: {}\n soma de todos = {}\n média aritmética = {}".format (total, soma, media))

print()

 #Atividade 2
print("Digite o código do produto e quantidade comprada:")
a = int(input("Código:"))
b = int(input("Quantidade comprada:"))
print()
if a == 1:
    c = b * 0.50
    print("Código: 1\nPreço:R$ %1.2f"%c)
elif a == 2:
    c = b * 1.00
    print("Código: 2\nPreço:R$ %1.2f"%c)
elif a == 3:
    c = b * 4.00
    print("Código: 3\nPreço:R$ %1.2f"%c)
elif a == 5:
    c = b * 7.00
    print("Código: 5\nPreço:R$ %1.2f"%c)
elif a == 9:
    c = b * 8.00
    print("Código: 9\nPreço:R$ %1.2f"%c)

print()

 #Atividade 3
tabuada = 1
numero = 1
ter = 1
while ter <= 100:
    print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
    numero += 1
    ter += 1
    if numero > 10:
        tabuada += 1
        numero = 1