#25/02/2022
#Atividade 1
#R: Nada acontece, pois nenhum dos IF são acionados

#Atividade 2
vel = int(input("Velocidade em que estava pilotando:"))
if vel > 80:
    print("Ultrapassou o limite, pague a multa devida!")
    a = vel - 80
    b = a * 5
    print("Multa: R$ %1.2f" %b)
else:
    print("Não ultrapassou o limite, não é preciso o pagamento da multa!")
print()

#Atividade 3
a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
c = float(input("Terceiro número:"))
if a > b > c:
    print(a, c)
elif b > a > c:
    print(b, c)
elif c > a > b:
    print(c, b)
elif a > c > b:
    print(a, b)
elif b > c > a:
    print(b, a)
elif c > b > a:
    print(c, a)
print()

#Atividade 4
sal = float(input("Digite seu salário:"))
if sal > 1250.00:
    des = sal * 0.10
    dess = des + sal
    print("Aumento: R$ %1.2f" %des)
    print("Novo salarío pós aumento: R$ %1.2f" %dess)
else:
    des = sal * 0.15
    dess = des + sal
    print("Aumento: R$ %1.2f" %des)
    print("Novo salarío pós aumento: R$ %1.2f" %dess)
print()

#Atividade 5
km = float(input("Digite o tanto a percorrer(km):"))
if km < 200:
    p = km * 0.50
    print("Preço: R$ %1.2f" %p)
else:
    p = km * 0.45
    print("Preço: R$ %1.2f" %p)
print()

#Atividade 6
x = 0
c = int(input("Escolha a tabuada:"))
print()
while x <= 10:
    b = x * c
    print("{} x {} = {}".format (x, c, b))
    x += 1
print()

#Atividade 7
x = 0
while x <= 100:
    print(x)
    x += 1
print()

#Atividade 8
x = 50
while x <= 100:
    print(x)
    x += 1
print()

#Atividade 9
print("Contagem regressiva para lançamento de foguete!")
x = 10
while x >= 0:
    print(x, "...")
    x -= 1
print("Fogo!")
print()

#Atividade 10
a = int(input("Digite um número:"))
b = 0
while b <= a:
    print(b)
    b += 2
