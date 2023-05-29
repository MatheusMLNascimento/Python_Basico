#03/03/2022
#Lista 8

#Atividade 1
n1 = float(input("Primeira nota"))
n2 = float(input("Segunda nota"))
n3 = float(input("Terceira nota"))
n4 = float(input("Quarta nota"))
n5 = float(input("Quinta nota"))
tot = (n1 + n2 + n3 + n4 + n5) / 5
print("A média das notas foi de %5.2f" % tot)
print()

#Atividade 2
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
if tot1 == 0:
    kin += 1
if tot2 == 0:
    kin += 1
if tot3 == 0:
    kin += 1
if tot4 == 0:
    kin += 1
if tot5 == 0:
    kin += 1
if tot6 == 0:
    kin += 1
if tot7 == 0:
    kin += 1
if tot8 == 0:
    kin += 1
if tot9 == 0:
    kin += 1
if tot10 == 0:
    kin += 1
print("Números pares digitados:", kin)
print()

#Atividade 3
# Nome do programa: gabarito.py
# Autor: Aprendiz de Feiticeiro
# Data: 03/03/2022

pontos = 0
questao = 1
while questao <= 3:
   resposta = input("Resposta da questão %d: " % questao)
   if questao == 1 and resposta == "b":
      pontos += 1
   if questao == 2 and resposta == "a":
      pontos += 1
   if questao == 3 and resposta == "d":
      pontos += 1

   questao += 1

print("O aluno fez %d ponto(s)" % pontos)