print("Digite dez números que vier na mente e descubra quantos são pares")
kin = 0
n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))
n4 = float(input("Digite um número:"))
n5 = float(input("Digite um número:"))
n6 = float(input("Digite um número:"))
n7 = float(input("Digite um número:"))
n8 = float(input("Digite um número:"))
n9 = float(input("Digite um número:"))
n10 = float(input("Digite um número:"))
tot1 = n1 % 2
tot2 = n2 % 2
tot3 = n3 % 2
tot4 = n4 % 2
tot5 = n5 % 2
tot6 = n6 % 2
tot7 = n7 % 2
tot8 = n8 % 2
tot9 = n9 % 2
tot10 =n10 % 2
print("Números pares digitados:", )
if tot1 == 0:
    kin += 1
    print(n1)
if tot2 == 0:
    kin += 1
    print(n2)
if tot3 == 0:
    kin += 1
    print(n3)
if tot4 == 0:
    kin += 1
    print(n4)
if tot5 == 0:
    kin += 1
    print(n5)
if tot6 == 0:
    kin += 1
    print(n6)
if tot7 == 0:
    kin += 1
    print(n7)
if tot8 == 0:
    kin += 1
    print(n8)
if tot9 == 0:
    kin += 1
    print(n9)
if tot10 == 0:
    kin += 1
    print(n10)
print("Total de pares digitados:", kin)